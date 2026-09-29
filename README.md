# Puff City — Edition Shop / Custom / Plugins locaux

## Ce qui a ete ajoute
- Bouton **Shop** fonctionnel depuis l'ordinateur.
- Achat de meubles avec une taille qui s'adapte aux dimensions de la maison.
- Les meubles ne sont plus fixes a une seule echelle : leur taille et leur espacement suivent le niveau de la maison.
- Atelier de creation de styles fictifs : nom, deux couleurs, forme et halo.
- Bouton **Essayer** pour tester visuellement une creation personnalisee.
- Inventaire compatible avec les creations personnalisees.
- Plugin Mod Menu local dans `Plugins/`, touche **P**.
- Le plugin ne publie rien sur Internet.
- Lanceur local avec ecran de chargement et credits pendant 5 secondes.

## Construire PuffCity.exe sous Windows
1. Ouvre ce dossier sur Windows.
2. Verifie Python 3.13 : `py -3.13 --version`
3. Installe PyInstaller si besoin : `py -3.13 -m pip install pyinstaller`
4. Double-clique `build_PuffCity_EXE.bat`.
5. Le fichier final sera `PuffCity.exe`.

Le lanceur ouvre le jeu sur `127.0.0.1` uniquement : le jeu et ses plugins restent locaux.

## Commandes
- ZQSD / WASD : marcher
- Souris : regarder
- E : interagir
- P : Mod Menu
- F5 : sauvegarder
