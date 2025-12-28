import orjson
import os
import shutil
import sys
import tempfile
import zipfile
from Utils import is_frozen, local_path

def setup_lib():
    # clean up any files from old versions of the apworld
    for path in [local_path("."), local_path("lib")]:
        for entry in os.scandir(path):
            if entry.name.startswith("albwrandomizer"):
                fullpath = os.path.join(path, entry.name)
                if entry.is_dir():
                    shutil.rmtree(fullpath)
                else:
                    os.remove(fullpath)

    if is_frozen():
        path = os.path.dirname(__file__)
        dirname = os.path.basename(path)
        apworld_path = os.path.dirname(path)
        with zipfile.ZipFile(apworld_path, "r") as apworld:
            with apworld.open(os.path.join(dirname, "archipelago.json"), "r") as manifest_file:
                manifest = orjson.loads(manifest_file.read())
            version = manifest["world_version"]
            tmp_path = os.path.join(tempfile.gettempdir(), f"albwrandomizer_{version}")
            if os.getenv("ALBW_DEBUG", 0):
                shutil.rmtree(tmp_path)
            if not os.path.exists(tmp_path):
                os.mkdir(tmp_path)
                randomizer_path = os.path.join(tmp_path, "albwrandomizer")
                os.mkdir(randomizer_path)
                world_lib_path = os.path.join(dirname, "albwrandomizer")
                for info in apworld.infolist():
                    if not info.is_dir() and info.filename.startswith(world_lib_path):
                        info.filename = os.path.basename(info.filename)
                        apworld.extract(info, randomizer_path)
            if not tmp_path in sys.path:
                sys.path.append(tmp_path)
    else:
        path = os.path.dirname(__file__)
        if not path in sys.path:
            sys.path.append(path)