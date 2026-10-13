
from random import randint, choice


# Classe parente pour gérer tous les poissons (thons et requins)
class Fish:

    def __init__(self, x:int, y:int, grid_size:tuple):
        self.x = x  # Cordonnées du  poisson
        self.y = y
        self._GRID_WIDTH = grid_size[0]
        self._GRID_HEIGHT = grid_size[1]


    # Fonction de déplacement 
    def move(self, surroundings:dict):

        if 0 in list(surroundings.values()):
            # S'il y a un moins une case vide
            space = choice(list(surroundings.keys()))
            # Choice va choisir une clé au hasard, correspondant au type de déplacement
            # (voir la fonctione neighbours dans la classe world)
            while surroundings[space]!=0:
                surroundings.pop(space)
                space = choice(list(surroundings.keys()))

            # Le poisson effectue le déplacement dans sa tête
            match space:
                case 'U':
                    self.y-=1
                case 'D':
                    self.y+=1
                case 'L':
                    self.x-=1
                case 'R':
                    self.x+=1

            # Correction si sorti de grille
            if not (0 <= self.x < self._GRID_WIDTH): self.x %= self._GRID_WIDTH
            if not (0 <= self.y < self._GRID_HEIGHT): self.y %= self._GRID_HEIGHT

            # Le poisson prévient World qu'il se déplace
            return True
        else:
            # Le poisson prévient World qu'il ne s'est pas déplacé
            return False





#test move à supprimer
if __name__ == "__main__":
    coord = {
        "U": Fish,
        "R": Fish,
        "D": 0,
        "L": Fish
    }
    test = Fish(5,5,(10,10))
    print( test.move(coord) )