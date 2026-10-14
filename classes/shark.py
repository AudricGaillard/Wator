import config as cfg
from classes.fish import Fish
from classes.tuna import Tuna
from random import choice

class Shark(Fish):
    """
    Classe Requin (Shark), un requin est une espèce de Poisson (Fish).
    """
    def __init__(self, x:int, y:int):

        super().__init__(x, y)

        # Constante(s) sur le métabolisme du requin.
        self.__ENERGY_ON_FEED = cfg.SHARK_ENERGY_ON_FEED
        self.__ENERGY_MAX = cfg.SHARK_STARVATION_TIME
        self._ALL_FOOD = [Tuna]

        # Constante pour la reproduction du requin,
        # SURCHARGE la même constante de la classe parent poisson (Fish) mais utilise la même fonction de reproduction.
        self._SPAWN_DELAY = cfg.SHARK_GESTATION_PERIOD

        # La jauge d'energie est rempli au maximum dès le depart.
        self._energy = self.__ENERGY_MAX
       

    # Fonction de déplacement du requin.
    def move(self, surroundings:dict):
        """
        
        """
        # En bougeant le requin brule des calories.
        self._energy -= 1
            
        # Le requin cherche à se déplace vers la nourriture an premier, sinon il se balader.
        for action in self._ALL_FOOD+[0]:    

            # Travaille sur une copie du dictionnaire car .pop sera utilisé dessus.
            surroundings_copy = surroundings.copy()

            # Recherche de cible, le(s) proie(s) sinon un emplacement une case vide.
            if action in list(surroundings_copy.values()):

                # Choix aléatoire d'une case adjacente
                space = choice(list(surroundings_copy.keys()))               
                # Si la case n'est pas libre, alors l'oublier et en choisir une autre jusqu'à en trouver une libre.
                while surroundings_copy[space] != action:
                    surroundings_copy.pop(space)
                    space = choice(list(surroundings_copy.keys()))

                # Le requin va se déplacer (et en previent le monde plus bas au retour de la fonction).
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

                # Le requin avertit au monde qu'il se déplace bien pour manger ou se balader
                return True
            
            elif action == 0:

                # Le requin avertit au monde qu'il ne s'est pas déplacé
                return False
