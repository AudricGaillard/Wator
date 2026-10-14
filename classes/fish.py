
from random import randint, choice


# Classe parente pour gérer tous les poissons (thons et requins).
class Fish:

    def __init__(self, x:int, y:int, grid_size:tuple):

        # Cordonnées du poisson.
        self.x = x
        self.y = y

        # Constante(s) de la grille monde.
        self._GRID_WIDTH = grid_size[0]
        self._GRID_HEIGHT = grid_size[1]

        # Constante du delai de reproduction, sera surchargé par les classes enfants.
        self._SPAWN_DELAY = int() 

        self._gestation = 0


    # Fonction de déplacement
    def move(self, surroundings:dict):

        if 0 in list(surroundings.values()):
            # Choix aléatoire d'une case adjacente.
            space = choice(list(surroundings.keys()))
            # Si la case n'est pas libre, alors l'oublier et en choisir une autre jusqu'à en trouver une libre.
            while surroundings[space]!=0:
                surroundings.pop(space)
                space = choice(list(surroundings.keys()))

            # Le poisson a choisi une case et en retient la direction.
            match space:
                case 'U':
                    self.y-=1
                case 'D':
                    self.y+=1
                case 'L':
                    self.x-=1
                case 'R':
                    self.x+=1

            # Correction si sorti de grille.
            if not (0 <= self.x < self._GRID_WIDTH): self.x %= self._GRID_WIDTH
            if not (0 <= self.y < self._GRID_HEIGHT): self.y %= self._GRID_HEIGHT

            # Le poisson avertit au monde qu'il se déplace.
            return True
        else:
            # Le poisson avertit au monde qu'il ne s'est pas déplacé.
            return False


    # Fonction de reproduction du poisson.
    def reproduce(self, surroundings:dict):
        """

        """
        # Si la gestation est arrivé à terme ET qu'il y a une case libre autour du poisson, alors mettre à bas.
        if self._gestation >= self._SPAWN_DELAY and 0 in list(surroundings.values()):
          
            # Choix aléatoire d'une case adjacente.
            space = choice(list(surroundings.keys()))
            # Si la case n'est pas libre, alors l'oublier et en choisir une autre jusqu'à en trouver une libre.
            while surroundings[space] != 0:
                surroundings.pop(space)
                space = choice(list(surroundings.keys()))

            # Le poisson a choisi une case et en retient la direction.
            spawning = { "x":0, "y":0 }
            match space:
                case 'U':
                    spawning['y'] -=1
                case 'R':
                    spawning['x'] +=1
                case 'D':
                    spawning['y'] +=1
                case 'L':
                    spawning['x'] -=1

            # Correction si sorti de grille.
            if not (0 <= spawning['x'] < self._GRID_WIDTH): spawning['x'] %= self._GRID_WIDTH
            if not (0 <= spawning['y'] < self._GRID_HEIGHT): spawning['y'] %= self._GRID_HEIGHT

            # La naissance remet la gestation à 0.
            self._gestation = 0
          
            # Le poisson avertit au monde la direction de la mise à bas.
            return spawning # dict{'x','y'}
          
        else:
            # A defaut, le poisson avertit au monde qu'il n'a pas pu mettre à bas.
            return False
