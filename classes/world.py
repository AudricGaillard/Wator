import os
import config as cfg
from classes.grid import WorldGrid

from time import sleep
from random import choice

from classes.fish import Fish
from classes.tuna import Tuna
from classes.shark import Shark

class World:

    def __init__(self):

        # Récuperation des constantes 
        self._MAX_CHRONONS = cfg.MAX_CHRONONS 
        self._SPEED = cfg.CHRONONS_SPEED
        self._chronons_counter = 0
        # Compteur de chronons

        self._GRID_WIDTH = cfg.GRID_WIDTH
        self._GRID_HEIGHT = cfg.GRID_HEIGHT
        self._TUNA_START_POPULATION = cfg.TUNA_START_POPULATION
        self._SHARK_START_POPULATION = cfg.SHARK_START_POPULATION

        # Création de l'environnement
        self._world_grid_env = WorldGrid(self._GRID_WIDTH, self._GRID_HEIGHT)
        

        self._tunas_entities = []
        self._sharks_entities = []

        # Création des premiers poissons
        self.starting_fishes(Tuna, self._TUNA_START_POPULATION)
        self.starting_fishes(Shark, self._SHARK_START_POPULATION)

    # Getter pour récupérer la grille, protégé lors de la création de World 
    @property
    def world_grid(self):
        return self._world_grid_env.world_grid

    # Fonction de placement de tous les poissons d'un type au début.
    def starting_fishes(self, fish_kind:Tuna|Shark, fish_amount:int):
        """
        Fonction permettant de créer les premiers poissons au début de Wator

        Args:
            fish_kind(Tuna|Shark): Le type de poissons que l'on veut instancier
            fish_amount(int): Le nombre de poissons que l'on veut instancier
        """
        # Liste de cases vides (là où il y a de l'eau)
        water = []

        for coordinate_y in range(self._GRID_HEIGHT):
            for coordinate_x in range(self._GRID_WIDTH):
                if self.world_grid[coordinate_y][coordinate_x] == 0: 
                    water.append((coordinate_x, coordinate_y))
        
        # La variable water contient maintenant les coordonnées de toutes les zones vides.
        
        # S'il y'a assez de cases vides pour placer tous les poissons
        if fish_amount<len(water):
            
            for fish in range(fish_amount):
                area = choice(water)
                self.fish_instanciation(fish_kind, area[0], area[1])
                water.remove(area)
                # On place chaque poisson dans une zone vide, puis on retire cette zone de la liste water.
        
        # Sinon
        else:
            print("Il n'y a pas assez de place pour mettre les poissons")


    # Fonction d'instanciation de poisson
    def fish_instanciation(self, fish_kind:Tuna|Shark, x:int, y:int):
        """
        Fonction permettant de créer une instance d'un poisson et de l'ajouter
        aux listes des poissons

        Args:
            fish_kind(Tuna|Shark): Le type de poissons que l'on veut instancier
            x(int): La coordonnée x du poisson
            y(int): La coordonnée y du poisson
        """
        self.world_grid[y][x] = fish_kind(x, y)
        # On appelle l'index Y (ligne/ordonnée) en premier, quand on manie la grille monde.
        if fish_kind==Tuna:
            self._tunas_entities.append(fish_kind(x, y))
            # Ajout d'un thon à la liste des thons
        else:
            self._sharks_entities.append(fish_kind(x, y))
            # Ajout d'un requin à la liste des requins


    # Fonction de comptage de poissons d'un type.
    def count_fish(self, fish_kind:Tuna|Shark|Fish):
        """
        Fonction permettant de compter le nombre de poissons selon le type demandé
        
        Args:
            fish_kind(Tuna|Shark|Fish):Le type de poisson que l'on veut compter. Passer Fish en paramètre permet de compter TOUS les poissons
        Returns:
            int:Le nombre de poissons
        """
        if fish_kind==Tuna:
            return len(self._tunas_entities)
        elif fish_kind==Shark:
            return len(self._sharks_entities)
        else:
            return len(self._sharks_entities)+len(self._tunas_entities)


    # Fonction de bouclage du temps qui passe (chronons/tours)
    def time_loop(self):
        """
        Fonction qui va gérer le processus de Wator en continu (ou jusqu'au maximum de chronons selon la configuration)
        """
    # On instancie la boucle de temps avec un maximum de tours.
        if self._MAX_CHRONONS > 0:
            for loop_turn in range(self._MAX_CHRONONS):
                self._chronons_counter+=1

                # S'il n'y a plus aucun thon ou requin, on arrête le script
                if self.count_fish(Tuna) == 0 or self.count_fish(Shark) == 0:
                    print("GAME OVER !")
                    break

                # Si le nombre de poisson dépasse la taille du tableau (longueur * largeur)
                elif self.count_fish(Fish)>self._GRID_HEIGHT*self._GRID_WIDTH:
                    print("GAME OVER ! Plus de place !")
                    break
                
                self.update_grid()
                self.print_grid()
                sleep(self._SPEED/1000)

        # Si MAX_CHRONONS à 0 (ou négatif) alors instancie une boucle infinie
        else: 
            while True:
                self._chronons_counter+=1

                # Même chose ici
                if self.count_fish(Tuna) == 0 or self.count_fish(Shark) == 0:
                    print("GAME OVER !")
                    break
                # Si le nombre de poisson dépasse la taille du tableau (longueur * largeur)
                elif self.count_fish(Fish)>self._GRID_HEIGHT*self._GRID_WIDTH:
                    print("GAME OVER ! Plus de place !")
                    break

                # Mise à jour de l'état des poissons
                self.update_grid()

                # Affichage de la grille
                self.print_grid()

                # sleep permet de mettre en pause la boucle pendant une certaine durée
                sleep(self._SPEED/1000)


    # Fonction pour récupérer les éléments adjacents à un thon dans la grille
    def neighbours(self, grid:list, fish:Tuna|Shark):
        """
        Fonction qui renvoie les cases adjacentes à un poisson

        Args:
            grid(list):La grille de Wator, permettant de récupérer les éléments à l'intérieur de la grille
            fish(Tuna|Shark):Le poisson, permettant de récupérer ses coordonnées
        Returns:
            dict:Le dictionnaire avec les directions comme clés et les éléments dans les cases adjacentes comme valeurs
        """
        los = {
            "U": grid[(fish.y - 1) % self._GRID_HEIGHT][fish.x],
            "R": grid[fish.y][(fish.x+1) % self._GRID_WIDTH],
            "D": grid[(fish.y + 1) % self._GRID_HEIGHT][fish.x],
            "L": grid[fish.y][(fish.x-1) % self._GRID_WIDTH]
        }

        # Pour chaque direction et instance dans le dictionnaire
        # Si l'instance n'est pas une case vide, on récupère le type de l'instance (Tuna ou Shark)
        for direction, instance in los.items():
            if instance != 0 : los[direction] = type(instance)
        return los
    
        # U --> Up
        # R --> Right 
        # D --> Down
        # L --> Left 

        # Les valeurs sont égales à ce que contient la case (0 ou une classe)
        # Le modulo permet de gerer les dépassements du tableau
        # Exemple avec la coordonnée x: -1 % 5 = 4 --> on revient à droite,
        # ce qui permet d'aller cherche la case au bout de la ligne avant que le
        # poisson puisse revenir à droite
    

    # Fonction pour vérifier les déplacements et la reproduction d'un requin
    def sharks_status(self, shark:Shark):
        """
        Fonction permettant de contrôler les déplacements, les reproductions et l'état d'un requin

        Args:
            shark(Shark):Le requin que l'on souhaite contrôller
        """
        if shark._energy <= 0:

            # Si le requin meurt de faim, on l'enlève de la liste des requins
            self._sharks_entities.remove(shark)
            
            # On met à jour la grille en remplacant la case du requin par une case eau
            self.world_grid[shark.y][shark.x] = 0
        else:
                        
            # On récupère les anciennes coordonnées du requin
            old_x = shark.x
            old_y = shark.y
        
            # On récupère les cases adjacentes au requin
            surroundings = self.neighbours(self.world_grid, shark)
        
            # Si le requin a pu se déplacer
            if shark.move(surroundings):
        
                # On récupère l'élément là où le requin s'est déplacé
                space = self.world_grid[shark.y][shark.x]

                # Si l'élément est un thon qui se trouve dans la liste des thons
                # --> le requin le mange
                if space in self._tunas_entities:

                    # On récupère l'index du thon mangé

                    # On retire le thon à la liste des thons
                    self._tunas_entities.remove(space)

                # On met à jour à la grille
                self.world_grid[shark.y][shark.x] = shark
                self.world_grid[old_y][old_x] = 0

                # On récupère à nouveau les cases autours du requin
                surroundings = self.neighbours(self.world_grid, shark)

                # On vérifie si le requin peut se reproduire autour de lui
                can_reproduce = shark.reproduce(surroundings)

                # Si la fonction reproduce ne renvoie pas False
                if can_reproduce != False:

                    # On crée les variables représentant les coordonnées du nouveau requin
                    # Le modulo va corriger les coordonnées si le nouveau requin est hors du tableau
                    # Si x = 30 --> 30 % 30 = 0 --> on revient à gauche
                    new_shark_x = (can_reproduce['x'] + shark.x) % self._GRID_WIDTH
                    new_shark_y = (can_reproduce['y'] + shark.y) % self._GRID_HEIGHT

                    # On crée un nouveau requin avec les coordonnées calculées
                    self.fish_instanciation(Shark, new_shark_x, new_shark_y)


    # Fonction pour vérifier les déplacements et la reproduction d'un thon
    def tunas_status(self, tuna:Tuna):
        """
        Fonction permettant de contrôler les déplacements et les reproductions d'un thon
        
        Args:
            tuna(Tuna):Le thon que l'on souhaite contrôller
        """
        # On récupère les anciennes coordonnées du thon
        old_x=tuna.x
        old_y=tuna.y

        # On récupére les cases adjacentes du thon
        surroundings = self.neighbours(self.world_grid, tuna)

        # Si le thon a pu se déplacer
        if tuna.move(surroundings):

            # On met à jour la grille pour mettre le thon sur les nouvelles coordonnées
            self.world_grid[tuna.y][tuna.x]=tuna
            self.world_grid[old_y][old_x]=0

            # On mets à jour les cases adjacentes du thons
            surroundings = self.neighbours(self.world_grid, tuna)

            # On vérifie si le thon peut se reproduire
            can_reproduce = tuna.reproduce(surroundings)

            # Si la fonction reproduce ne renvoie pas False
            if can_reproduce != False:
                
                # On crée les variables représentant les coordonnées du nouveau requin
                # Le modulo va corriger les coordonnées si le nouveau requin est hors du tableau
                # Si x = 30 --> 30 % 30 = 0 --> on revient à gauche
                new_tuna_x = (can_reproduce['x'] + tuna.x) % self._GRID_WIDTH
                new_tuna_y = (can_reproduce['y'] + tuna.y) % self._GRID_HEIGHT

                # On crée un nouveau thon avec les coordonnées calculées
                self.fish_instanciation(Tuna, new_tuna_x, new_tuna_y)


    # Fonction pour mettre à jour la grille après les actions effectués par tous les poissons    
    def update_grid(self):
        """
        Fonction permettant mettre à jour l'état de tous les poissons
        """
        # Pour chaque requin
        for sharks in self._sharks_entities:

            # Appel de la fonction sharks_status pour vérifier son déplacement, sa reproduction et son état
            self.sharks_status(sharks)

        # Pour chaque thon
        for tunas in self._tunas_entities:

            # Appel de la fonction tunas_status pour vérifier son déplacement et sa reproduction
            self.tunas_status(tunas)


    # Fonction pour afficher la grille
    def print_grid(self):
        """
        Fonction permettant d'afficher la grille
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # efface le terminal
        for lines in self.world_grid:
            for element in lines:
                
                # Pour chaque élément d'une ligne
                # match va vérifier le type de l'élément
                match element:

                     # Affiche ceci si l'élément est une instance de la classe Tuna
                    case x if isinstance(x, Tuna): 
                        print("\033[42m  \033[0m", end="")
                        # \033[42m --> permet d'afficher sur un fond vert

                     # Affiche ceci si l'élément est une instance de la classe Shark

                    case x if isinstance(x, Shark): 
                        print("\033[41m  \033[0m", end="")
                        # \033[41m --> affiche sur un fond rouge

                    # Affiche ceci si l'élément ne respecte aucune des deux conditions

                    case _: 
                        print("\033[44m  \033[0m", end="")
                        # \033[41m --> affiche sur un fond bleu
                    
                    # \033[0m" --> permet de réinitialiser le mode d'écriture de la console 

            print("")
        print(f"\nNombre de thons : {self.count_fish(Tuna):<6}|  Nombre de requins : {self.count_fish(Shark):<6}|  Nombre total de poissons : {self.count_fish(Fish)}")
        print(f"Chronons : {self._chronons_counter}")

#~test local temporaire
if __name__ == "__main__":
    wator_env = World()
    wator_env.time_loop()



