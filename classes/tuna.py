from classes.fish import Fish
class Tuna(Fish):
    def __init__(self, x, y, grid_size):
        super().__init__(x,y, grid_size)
        self._GRID_WIDTH = grid_size[0]
        self._GRID_HEIGHT = grid_size[1]