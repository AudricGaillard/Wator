#==================================================
###  Temps de la simulation (tours/chronons)
#
# Nombre de chronons          0 = infini
MAX_CHRONONS:int = 0
# Vitesse de chronons (en millisecondes)
CHRONONS_SPEED = 300

#==================================================
### Taille de la grille monde
#
# Largeur
GRID_WIDTH:int  = 30
#
# Hauteur
GRID_HEIGHT:int = 12
#

#==================================================
### Populations de départ des poissons
#
# Thons
TUNA_START_POPULATION:int  = 100
#
# Requins
SHARK_START_POPULATION:int = 10
#

#==================================================
### Temps de reproduction des differents poissons
#
# Thons
TUNA_GESTATION_PERIOD:int  = 8          # 8 ?
#
# Requins
SHARK_GESTATION_PERIOD:int = 12         # 12 ?
#

#==================================================
### Alimentation des requins
#
# Tours avant mort de faim (Energie)
SHARK_STARVATION_TIME:int = 10
#
# Energie/Tours rendus par repas
SHARK_ENERGY_ON_FEED:int  = 6
#
