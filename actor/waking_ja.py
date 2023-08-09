import random

import pygame

from actor.actor import WalkSoldier


class JapaneseWalkSoldier(WalkSoldier):
    def __init__(self, x, y):
        soldier_id = random.randint(1, 4)
        work_path = "./resources/images/japanese/soldier{0}.png".format(soldier_id)

        super(JapaneseWalkSoldier, self).__init__(work_path, x, y,
                                                  "小日本" + str(soldier_id), 100)
        self.count = 5
        self.key = pygame.K_DOWN

    def run(self):
        if self.count == 0:
            key = random.randint(0, 3)
            self.count = 5
            if key == 0:
                self.key = pygame.K_DOWN
            elif key == 1:
                self.key = pygame.K_UP
            elif key == 2:
                self.key = pygame.K_LEFT
            elif key == 3:
                self.key = pygame.K_RIGHT
        else:
            self.count -= 1

        super(JapaneseWalkSoldier, self).run(self.key)
