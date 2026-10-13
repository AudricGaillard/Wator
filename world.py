import os
import config as cfg
import grid

from time import sleep
from random import choice

from classes.fish  import Fish
from classes.tuna  import Tuna
from classes.shark import Shark


class World:

    def __init__(self):

        # Récuperation des constantes 
        self._MAX_CHRONONS = cfg.MAX_CHRONONS  
        self._chronons_counter = 0

        self._GRID_WIDTH = cfg.GRID_WIDTH
        self._GRID_HEIGHT = cfg.GRID_HEIGHT
        
        self._TUNA_START_POPULATION = cfg.TUNA_START_POPULATION
        self._SHARK_START_POPULATION = cfg.SHARK_START_POPULATION

        # Création de l'environnement
        self._world_grid_env = grid.WorldGrid(self._GRID_WIDTH, self._GRID_HEIGHT)
        self.world_grid = self._world_grid_env.world_grid

        self._tunas_entities = []
        self._sharks_entities = []

        # Création des premiers poissons
        self.starting_fishes(Tuna, self._TUNA_START_POPULATION)
        self.starting_fishes(Shark, self._SHARK_START_POPULATION)


         


    # Fonction de placement de tous les poissons d'un type au début.
    def starting_fishes(self, fish_kind:Tuna|Shark, fish_amount):

        water = []
        for coordinate_y in range(self._GRID_HEIGHT):
            for coordinate_x in range(self._GRID_WIDTH):

                if self.world_grid[coordinate_y][coordinate_x] == 0: 
                    water.append((coordinate_x, coordinate_y))
                    # La variable water contient maintenant les coordonnées de toutes les zones vides.

        for fish in range(fish_amount):
            area = choice(water)
            self.fish_instanciation(fish_kind, area[0], area[1], (self._GRID_WIDTH,self._GRID_HEIGHT))
            water.remove(area)
            # On place chaque poisson dans une zone vide, puis on retire cette zone de la liste water.



    # 
    def fish_instanciation(self, fish_kind:Tuna|Shark, x, y, grid_size):

        self.world_grid[y][x] = fish_kind(x, y, grid_size)
        # on appelle l'index Y (ligne/ordonnée) en premier, quand on manie la grille monde.
        if fish_kind==Tuna:
            self._tunas_entities.append(fish_kind(x, y, grid_size))
        else:
            self._sharks_entities.append(fish_kind(x, y, grid_size)) 
        #Ajout du thon à la liste des thons



    # Fonction de comptage de poissons d'un type.
    def count_fish(self, fish_kind:Tuna|Shark|Fish):
        if fish_kind==Tuna:
            return len(self._tunas_entities)
        elif fish_kind==Shark:
            return len(self._sharks_entities)
        else:
            return len(self._sharks_entities)+len(self._tunas_entities)



    # Fonction de bouclage du temps qui passe (chronons/tours)
    def time_loop(self):

        # On instancie la boucle de temps avec un maximum de tours.
        if self._MAX_CHRONONS > 0:
            for loop_turn in range(self._MAX_CHRONONS):
                self.print_grid()
                if self.count_fish(Tuna) >= (self._GRID_HEIGHT*self._GRID_WIDTH):
                    print("Plus de place !")
                    break
                # Si le nombre de poissons dépasse la longueur fois la largeur de la grille
                # --> plus de place = on arrête le script
                sleep(0.8)
            
        # Si MAX_CHRONONS à 0 (ou négatif) alors instancie une boucle infinie
        else: 
            while True:
                self.print_grid()
                if self.count_fish(Tuna) >= (self._GRID_HEIGHT*self._GRID_WIDTH):
                    print("Plus de place !")
                    break
                # Même chose ici
                sleep(0.8)

    # Fonction pour récupérer les éléments adjacents à un thon dans la grille
    def neighbours(self, grid, fish):
                return{
                    "U": grid[(fish.y - 1) % self._GRID_HEIGHT][fish.x],
                    "R": grid[fish.y][(fish.x+1) % self._GRID_WIDTH],
                    "D": grid[(fish.y + 1) % self._GRID_HEIGHT][fish.x],
                    "L": grid[fish.y][(fish.x-1) % self._GRID_WIDTH]   
                }
                # U --> Up
                # R --> Right 
                # D --> Down
                # L --> Left 
                
                # Les valeurs sont égales à ce que contient la case (0 ou une classe)
                # Le modulo permet de gerer les dépassements du tableau
                # Exemple avec la coordonnée x: -1 % 5 = 4 --> on revient à droite,
                # ce qui permet d'aller cherche la case au bout de la ligne avant que le
                # poisson puisse revenir à dori
    
    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # efface le terminal
        for lines in self.world_grid:
            for element in lines:
                # Pour chaque élément d'une ligne
                match element:
                    case x if isinstance(x, Tuna): 
                        print("\033[92m◀▶\033[0m", end="")
                        # Affiche ceci si l'élément est une instance de la classe Tuna
                    case x if isinstance(x, Shark): 
                        print("\033[94m▲▲\033[0m", end="")
                        # Affiche ceci si l'élément est une instance de la classe Shark
                    case _: 
                        print("\033[96m░░\033[0m", end="")
            print("")
                        # Affiche ceci si l'élément n'est une instance de la classe Tuna
        print(f"Nombre de thons : {self.count_fish(Tuna)}")
        print(f"Nombre de requins : {self.count_fish(Shark)}")
        # Affiche le nombre de poissons

        for sharks in self._sharks_entities:
            if sharks._energy==0:
                self._sharks_entities.pop(self._sharks_entities.index(sharks))
                self.world_grid[sharks.y][sharks.x]=0
            else:
                old_x=sharks.x
                old_y=sharks.y
                surroundings = self.neighbours(self.world_grid, sharks)
                if sharks.move(surroundings):
                    space = self.world_grid[sharks.y][sharks.x]
                    if isinstance(space, Tuna) and space in self._tunas_entities:
                        self._tunas_entities.remove(space)
                    self.world_grid[sharks.y][sharks.x]=sharks
                    self.world_grid[old_y][old_x]=0



        
        for tunas in self._tunas_entities:
            old_x=tunas.x
            old_y=tunas.y
            # Pour chaque thon, on enregistre ses anciennes coordonnées
            surrounding = self.neighbours(self.world_grid, tunas)
            # On récupére les cases adjacentes du thon
            if tunas.move(surrounding):
                # Si le thon s'est déplacé
                self.world_grid[tunas.y][tunas.x]=tunas
                # On met à jour la grille pour mettre le thon sur les nouvelles
                # coordonnées
                self.world_grid[old_y][old_x]=0
                # On remplace les anciennes coordonnées par une case vide


        


    



#~test local temporaire
if __name__ == "__main__":
    wator_env = World()
    wator_env.time_loop()

# os.system('cls' if os.name == 'nt' else 'clear')  # efface le terminal
