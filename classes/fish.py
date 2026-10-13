import config as cfg
from random import choice

# Classe parente pour gérer tous les poissons (thons et requins)
class Fish:
    def __init__(self, x:int, y:int):
        self.x = x 
        self.y = y
        # Cordonnées des poissons

    # Fonction de déplacement 
    def move(self, surroundings:dict):
        if 0 in list(surroundings.values()):
            # S'il y a un moins une case vide
            space = choice(list(surroundings.keys()))
            # Choice va choisir une clé au hasard, correspondant au type de déplacement
            # (voir la fonction neighbours dans la classe world)
            while surroundings[space]!=0:
                # Si la valeur de la clé choisie n'est pas une case vide
                space = choice(list(surroundings.keys()))
                # On rapelle choice pour prendre 
            match space:
                case 'U':
                    self.y-=1
                case 'D':
                    self.y+=1
                case 'L':
                    self.x-=1
                case 'R':
                    self.x+=1

            if not (0 <= self.x < cfg.GRID_WIDTH): self.x %= cfg.GRID_WIDTH

            if not (0 <= self.y < cfg.GRID_HEIGHT): self.y %= cfg.GRID_HEIGHT
            return True
        else:
            return False

        
        
        
        
        
        
        
        # new_x = 0
        # new_y = 0

        # while new_x==0 and new_y==0:
        #     new_x = randint(-1,1)
        #     new_y = randint(-1,1)
        #     # On instancie au hasard deux valeurs valant soit 1,
        #     # soit -1 ou 0 (on continue la boucle tant que 0 les deux vallent 0 pour que le
        #     # poisson ne reste pas sur place)
        
        # self.x += new_x
        # self.y += new_y
        # # On incrémente/décrémente les coordonnées du poissons selon les valeurs obtenues
        # # avec randint

        

        # # Dans les conditions, on vérifie si x ou y sont plus petit que 0 ou dépasse la
        # # longueur/largeur du tableau.

        # # Si c'est le cas, on utilise le modulo pour calculer les nouvelles coordonées