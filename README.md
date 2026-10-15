# wa-tor
## Écosystème Simulé de Requins et Poissons

### Description du projet
Ce projet vise à simuler le principe de Wator, une simulation de population dynamique représentant un écosystème de requin et de thons.

Explication complète de Wator : https://en.wikipedia.org/wiki/Wa-Tor

### Fonctionnement de Wator
Des requins et des thons se déplacent chacun sur une grille, et peuvent réaliser diverses actions après un certain nombre de chronons (unité utilisé pour contrôller le temps passé):
- Les thons et les requins peuvent se reproduire, ce qui en créer des nouveaux sur la grille
- Les requins possèdent une quantité d'énergie qui décrémente à chaque déplacement, et meurent si leur énergie atteint 0. Ils peuvent manger les thons, ce qui les retire de la grille et augmente l'énergie des requins.

### Structure du projet
Le projet est structurée ainsi :
- Le dossier classes contient les fichiers gérant les classes pour les poissons, la grille et le monde
- config.py est un fichier contenant des constantes comme la taille de la grille ou le nombre de thons au départ, servant au bon fonctionnement du projet. Ces constantes peuvent être modifiables.
- main.py est le fichier principal a exécuter

<video controls width="640" height="360" poster="image-apercu.jpg">
  <source src="./readme_assets/wator_demo.mp4" type="video/mp4" />
  Votre navigateur ne prend pas en charge la lecture de vidéos.
</video>

<p align="center">
  <img src="./readme_assets/gif" alt="GIF requin qui tourne">
</p>





