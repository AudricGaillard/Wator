import config as cfg
from classes.fish import Fish
class Tuna(Fish):
    """
    
    """
    def __init__(self, x, y):

        super().__init__(x,y)
        self._SPAWN_DELAY = cfg.TUNA_GESTATION_PERIOD