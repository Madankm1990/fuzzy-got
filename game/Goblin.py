
from game.Skeleton import Skeleton
from fuzzy import FuzzyRules

class Goblin(Skeleton):

    def __init__(self, image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y):
        Skeleton.__init__(self, image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y)
        self.health = 50
        self.attack = "Low"
        self.speed = "Fast"
        self.type = "Goblin"


    def fuzzy_move(self):
        self.step = FuzzyRules.get_fuzzy_value_for_speed(self.speed)
