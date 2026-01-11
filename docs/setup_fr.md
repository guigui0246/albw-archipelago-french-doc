# A Link Between Worlds Guide d'Installation

## ATTENTION
Il y a un problème connu actuellement où si vous fermez Archipelago puis le rouvrez, le client pourrait ne pas apparaître.
Si cela arrive, fermez complètement Archipelago, attendez quelques secondes pour être sûr qu'il est bien fermé (vous pouvez vérifier dans le Gestionnaire des Tâches), supprimez le dossier `albwrandomizer_0.1.4` dans le dossier `%temp%` (vous pouvez entrer ce chemin dans la barre d'adresse de l'explorateur de fichiers ou dans la boîte de dialogue Exécuter en appuyant sur Win+R pour les utilisateurs Windows), puis rouvrez Archipelago.

## Software Nécessaire

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases).
- Une ROM décryptée de A Link Between Worlds d'Amérique du Nord en `.3ds` jusqu'à la 0.1.3 et `.cci` à partir de la 0.1.4. Les instructions pour dump la ROM peuvent être trouvées (en anglais) [ici](https://wiki.hacks.guide/wiki/3DS:Dump_titles_and_game_cartridges). **Faîtes bien attention à selectionner "decrypt" lors du dump.** Si vous avez un fichier en `.cci` ou `.3ds` renommez le juste au format voulu et si vous avez un fichier en `.cia` utilisez [makerom.exe packagé dans ctrtool (attention installez makerom pas ctrtool)](https://github.com/3DSGuy/Project_CTR/releases) ou ce [script](https://github.com/davFaithid/CIA-to-3DS-Rom-Converter/releases)
- Pour jouer sur émulateur: [Azahar](https://azahar-emu.org/pages/download/) (ou une archive [Lime3DS](https://github.com/Lime3DS/lime3ds-archive) ou [Citra](https://github.com/PabloMK7/citra/releases)). Note: Si vous utilisez l'émulateur Azahar, le fichier de ROM doit être en `.cci` et sinon en `.3ds` pour qu'il soit accepté par l'émulateur. Ces fichiers sont identiques, c'est juste l'extension qui change.
- Pour jouer sur 3ds: [Luma3DS](https://3ds.hacks.guide/) et le [plugin.3gx](https://github.com/LittleCube-hax/albw-ap-plugin/releases/latest) de LittleCube.

- **Le jeu doit être joué en langue ANGLAISE.** *RIP le français. 😞* (si vous le faîtes pas vous allez casser le jeu et softlock)

## Installation

1. Installer la dernière version d'Archipelago.
2. Télécharger `albw.apworld` et le mettre dans le dossier `Archipelago/custom_worlds/` (double-cliquer dessus devrais aussi fonctionner).

## Setup (Émulateur)

3. Dans l'emulateur, sélectionner `Fichier > Ouvrier dossier <nom de l'émulateur>` (ou `File > Open <émulateur> Folder` en anglais). Créer un dossier `load` dans le dossier de l'émulateur et un dossier `mods` dans le dossier `load`.
4. **Pour les utilisateurs de Azahar uniquement**: Sélectionner `Émulation > Configuration` (ou `Emulation > Configure` en anglais). Puis sélectionner l'onglet `Debug` et tout en bas cochez (si c'est pas dajà fait) l'option `Activer le serveur RPC` (ou `Enable RPC Server` en anglais).

## Setup (3DS)

3. Installer Luma3DS, en suivant le guide (en anglais) à https://3ds.hacks.guide/
4. Sur l'écran de configuration de Luma3DS après l'allumage (si cet écran n'apparait pas, maintenir SELECT en allumant la console):
    1. _Vérifier_ que `Activer le chargement des FIRMs et modules externes` (ou `Enable loading external FIRMs and modules` en anglais) **N'EST PAS** coché. Si c'est le cas, le désactiver.
    2. Activer `Activer le patching de jeu` (ou `Enable game patching` en anglais) et s'assurer qu'il **EST** coché.
    3. Appuyer sur Start ou sélectionner `Sauvegarder et quitter` (ou `Save and exit` en anglais).
5. Appuyer sur L+DPadBas+Select pour ouvrir le menu Rosalina, et s'assurer que `Chargeur de plugin` (ou `Plugin loader` en anglais) est sur `[Activé]` (ou `[Enabled]` en anglais).
6. Télécharger le fichier [plugin.3gx](https://github.com/LittleCube-hax/albw-ap-plugin/releases/latest) et le copier dans `/luma/plugins/00040000000EC300/` sur votre carte SD.

## Mise à jour

1. **Jusqu'à la 0.1.3 inclue**: Supprimer le dossier albwrandomizer du dossier `Archipelago/lib/`.
2. Faire l'étapes 2 de l'[Installation](#installation)

## Générer une partie

1. Créer le fichier YAML d'option du joueur. Un exemple est inclus et peut être généré avec le bouton `Generate Yaml Templates` dans le launcher d'Archipelago.
2. (Hôte uniquement, identique pour tous les jeux): Récupérer les YAMLs de tous les joueurs de la partie dans le dossier `Archipelago/Players`.
3. (Hôte uniquement, identique pour tous les jeux): Exécuter le launcher d'Archipelago est sélectionner `Generate` ("Générer").
4. (Hôte uniquement, identique pour tous les jeux): Un fichier zip va être créé dans le dossier `Archipelago/output`. Téléverser ce fichier sur [le site d'Archipelago](https://archipelago.gg/uploads) pour héberger la partie.
5. Dans le fichier zip se trouvera un fichier en `.apalbw`. Ce fichier **est nécessaire** pour jouer au jeu.

# Jouer au jeu

1. L'hôte (celui qui génère la partie) vous donnera le fichier `.apalbw` qui aura été créé. Glisser le fichier sur le launcher d'Archipelago ou appuyer sur `Open Patch` dans la launcher et sélectionner le fichier `.apalbw`.
2. Entrer le chemin vers votre ROM A Link Between Worlds (première fois uniquement, il est sauvegardé dans `Archipelago/host.yaml`). Attendre environ 20 seconds pour que le jeu soit patché.
3. Celà fera 2 choses. D'abord ouvrir le client A Link Between World et ensuite créer un fichier zip dans le même dossier que le patch et avec le même nom. Dézipper ce fichier pour récupérer le dossier `00040000000EC300` dedans.

## Jouer au jeu (Émulateur)

4. Mettre le dossier `00040000000EC300` dans le dossier `load/mods/` créé à l'installation. (Si il y a déjà un dossier avec le même nom dedans supprimer, déplacer ou renommer l'ancien avant de mettre le nouveau.)
5. Éxécuter A Link Between Worlds dans l'émulateur. Le client devrait se connecter automatiquement à l'émulateur (sinon fermer tout puis se référer à [Continuer une partie](#continuer-une-partie)).
6. Entrer l'URL du serveur hébergant la partie dans le client et appuyer sur `Connect`.

## Jouer au jeu (3DS)

4. Copier le dossier `00040000000EC300` dans `/luma/titles/` sur votre carte SD.
5. Réinsérer la carte SD dans votre 3DS et allumer la console.
6. Éxécuter A Link Between Worlds. À la fin de l'écran de chargement rouge de la 3DS, vous devriez voir un flash bleu. Cela signifie que le plugin s'est bien chargé.
7. Éxécuter la commande sur l'écran dans le client ALBW.
8. Entrer l'URL du serveur hébergant la partie dans le client et appuyer sur `Connect`.

## Continuer une partie

1. Éxécuter le launcher d'Archipelago et sélectionner le client A Link Between Worlds.
2. Éxécuter les étapes 5 et 6 de la section [Jouer au jeu (Émulateur)](#jouer-au-jeu-émulateur) ou les étapes 4 à 8 de la section [Jouer au jeu (3DS)](#jouer-au-jeu-3ds).
