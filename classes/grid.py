import config as cfg


# Classe instanciant la grille monde contenant les poissons
class WorldGrid:
    """
    Classe permettant de gérer la grille (qui sera au départ remplie avec des 0) qui servira
    à placer les entités (thons et requins)
    """
    def __init__(self, grid_width:int, grid_height:int):
        self._grid_width = grid_width
        self._grid_height = grid_height
        self.__grid_creation()

        # On corrige les coordonnée sorties hors des frontières
        recup_x, recup_y = self.coordinate_correction(grid_width, grid_height)
        # Variables inutilisées dans l'immédiat


    # Création de la grille dans objet
    def __grid_creation(self):
        """
        Fonction permettant de créer la grille, qui pourra alors être réutilisée par les autres
        classes
        """
        if self._grid_width < 1:
            raise Exception ("Largeur de grille impossible")
        if self._grid_height < 1:
            raise Exception ("Hauteur de grille impossible")

        #Création de la grille
        self.__world_grid = []
        for line in range(self._grid_height):
            self.__world_grid.append([])
            for colonne in range(self._grid_width):
                self.__world_grid[line].append(0)


    # Getter qui retourne la grille, attribut privée dans la classe.
    @property
    def world_grid(self):
        return self.__world_grid


    # Fonction de correction de coordonées hors limites (inutilisé dans l'immédiat)
    def coordinate_correction(self, x:int, y:int):
        """
        Retourne un tuple des deux coordonnées X et Y dans les limites du tableau.
        
        Arg:
            x (`int`): coordonnée X
            y (`int`): coordonnée Y

        Returns:
            `tuple[int, int]` : Retourne les valeurs X et Y corrigées dans un tuple
        """
        wid = self._grid_width
        hei = self._grid_height

        if not (0 <= x < wid): x %= wid
        if not (0 <= y < hei): y %= hei
            
        return x, y





#~test local temporaire
if __name__ == "__main__":

    my_grid = WorldGrid(cfg.grid_width, cfg.grid_height)

    for i in range(len(my_grid.world_grid)):
        print(my_grid.world_grid[i])
