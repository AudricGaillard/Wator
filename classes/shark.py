import config as cfg
from classes.fish import Fish
from classes.tuna import Tuna
from random import randint, choice

class Shark(Fish):
    """
    
    """
    def __init__(self, x:int, y:int, grid_size:tuple):
        super().__init__(x, y, grid_size)
        self._GRID_WIDTH = grid_size[0]
        self._GRID_HEIGHT = grid_size[1]
        self.__ENERGY_ON_FEED = cfg.SHARK_ENERGY_ON_FEED
        self.__ENERGY_MAX = cfg.SHARK_STARVATION_TIME

        self._energy = self.__ENERGY_MAX

        self._ALL_FOOD = [Tuna]


    # Fonction de déplacement 
    def move(self, surroundings:dict):
        moved=False
        """
        
        """
        # Le requin brule des calorie
        self._energy -= 1
            
        # La boucle cherche un Thon à manger (en se déplacant) en premier, sinon le fait se balader
        for action in (self._ALL_FOOD + [0]):    

            # Travaille sur une copy du dictionnaire car on utilise .pop plus bas
            surroundings_copy = surroundings.copy()
            if type(action)!=int:
                element_exist=any(type(space)==Tuna for space in surroundings_copy.values())
            else:
                element_exist=any(type(space)==int for space in surroundings_copy.values())
            

            # Recherche de cible, le(s) proie(s) sinon un emplacement une case vide
            if element_exist:

                # S'il y a un moins une case avec la cible
                space = choice(list(surroundings_copy.keys()))

                # Choice va choisir une clé au hasard, correspondant à l'action
                # (voir la fonction neighbours dans la classe world)
                if action==0:
                    while surroundings_copy[space] != 0:
                        surroundings_copy.pop(space)
                        space = choice(list(surroundings_copy.keys()))
                else:
                    while type(surroundings_copy[space])!=Tuna:
                        surroundings_copy.pop(space)
                        space = choice(list(surroundings_copy.keys()))

                # Le requin effectue le déplacement dans sa tête
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

                # Le requin se nourri
                if action != 0:
                    self._energy += self.__ENERGY_ON_FEED

                    # on recrache le troplus dans l'estomac
                    if self._energy > self.__ENERGY_MAX :
                          self._energy = self.__ENERGY_MAX

                # Le requin prévient World qu'il se déplace pour manger ou se balader
                moved=True
                break
        return moved





#test local - à retirer
if __name__ == "__main__":
    coord = {
        "U": 0,
        "R": 0,
        "D": 0,
        "L": 0
    }
    test = Shark(5,5)
    print(test.move(coord))

        