from typing import Optional
import enum
import socket
import struct

class ConnectionError(Exception):
    pass

class RequestType(enum.IntEnum):
    Ping = 0
    Read = 1
    Write = 2
    ProcessList = 3
    SetGetProcess = 4

class N3DSInterface:
    PACKET_VERSION: int = 1
    HEADER_SIZE: int = 0x10
    MAX_PACKET_SIZE: int = 0x410

    sock: socket.socket
    max_request_size: int
    id: int

    def __init__(self):
        self.id = 0
        self.max_request_size = 32
    
    def _max_read_size(self) -> int:
        return self.max_request_size
    
    def _max_write_size(self) -> int:
        return self.max_request_size - 8
    
    def _send_packet(self, request_type: RequestType, request_data: bytes, response_size: Optional[int] = None) -> bytes:
        for _ in range(4):
            try:
                request_id = self.id
                self.id = (self.id + 1) & 0xffffffff
                request = struct.pack("=IIII", self.PACKET_VERSION, request_id, request_type, len(request_data))
                request += request_data
                self.sock.sendall(request)
                for _ in range(16):
                    response = self.sock.recv(self.MAX_PACKET_SIZE)
                    if not response or len(response) < self.HEADER_SIZE:
                        break
                    version, id, response_type, size = struct.unpack("=IIII", response[:self.HEADER_SIZE])
                    if version == self.PACKET_VERSION and id == request_id and response_type == request_type:
                        return response[self.HEADER_SIZE:]
            except Exception as e:
                continue
        raise ConnectionError("Lost connection to game")

    def _set_process(self, title: int) -> bool:
        start_process = 0
        while True:
            request_data = struct.pack("=II", start_process, 0x7fffffff)
            try:
                response = self._send_packet(RequestType.ProcessList, request_data)
                count = struct.unpack("=I", response[0:4])[0]
                if count == 0:
                    return False
                start_process += count
                for i in range(count):
                    proc_id, title_id = struct.unpack("=IQ", response[i * 0x14 + 4 : i * 0x14 + 0x10])
                    if title_id == title:
                        request_data = struct.pack("=II", 1, proc_id)
                        self._send_packet(RequestType.SetGetProcess, request_data, 0)
                        self.max_request_size = 1024
                        return True
            except ConnectionError:
                # if no response, assume we are on an older version
                self.max_request_size = 32
                return True

    def connect(self, address: str, title: int) -> bool:
        self.disconnect()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((address, 45987))
        self.sock.settimeout(0.25)
        try:
            self._send_packet(RequestType.Ping, b"", 0)
            return self._set_process(title)
        except ConnectionError:
            return False

    def disconnect(self):
        if hasattr(self, 'sock'):
            self.sock.close()

    def read(self, address: int, size: int) -> bytes:
        mem = b""
        while size > 0:
            request_size = min(size, self._max_read_size())
            request_data = struct.pack("=II", address, request_size)
            mem += self._send_packet(RequestType.Read, request_data, request_size)
            address += request_size
            size -= request_size
        return mem

    def write(self, address: int, data: bytes) -> None:
        start = 0
        while start < len(data):
            end = min(start + self._max_write_size(), len(data))
            request_data = struct.pack("=II", address + start, end - start)
            request_data += data[start:end]
            self._send_packet(RequestType.Write, request_data, 0)
            start += self._max_write_size()

    def read_u32(self, address: int) -> int:
        return int.from_bytes(self.read(address, 4), "little")
    
    def write_u32(self, address: int, value: int) -> None:
        self.write(address, value.to_bytes(4, "little"))
