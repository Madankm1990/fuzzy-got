from pygame.locals import *
from game.Goblin import Goblin
from random import randint
import pygame
import sys
import time


class BattleField:
    base_path = "/media/sai/New Volume/NUS/IVLE/CI2/CA/Fuzzy"
    _running = True
    _display_surf = None
    global_army_group = []
    goblin_army = 100
    ogre_army = 5
    troll_army = 3
    windowWidth = 1200
    windowHeight = 1000


    def on_init(self):
        pygame.init()
        # global army group - consists of all warriors
        for goblin_idx in range(self.goblin_army):
            goblin = Goblin(self.base_path + "/images/goblin.png", 150, 150, 0, 0, self.windowHeight, self.windowWidth)
            self.global_army_group.append(goblin)

        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        for bot in self.global_army_group:
            bot.create_avatar()

        pygame.display.set_caption('Goblins Ogres & Trolls - The Grand GOT War')
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill((0, 0, 0))

        army_list_coord_list = []

        # to ensure bots do not overlap
        for bot in self.global_army_group:
            if bot.type == "Goblin":
                bot.fuzzy_move()

            army_list_coord_list = bot.update(army_list_coord_list)
            print(army_list_coord_list)
            bot.draw(self._display_surf, bot._image_surf)

        #self.apple.draw(self._display_surf, self._apple_surf)
        #self.computer.draw(self._display_surf, self._image_surf)
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.key_based_movement()
            self.on_render()

            time.sleep(50.0 / 1000.0)
        self.on_cleanup()


    def key_based_movement(self):
        #pygame.event.pump()
        pygame.event.wait()
        keys = pygame.key.get_pressed()
        for bot in self.global_army_group:
            if keys[K_UP]:
                bot.moveUp()
            if keys[K_DOWN]:
                bot.moveDown()
            if keys[K_RIGHT]:
                bot.moveRight()
            if keys[K_LEFT]:
                bot.moveLeft()
            if keys[K_ESCAPE]:
                self._running = False

if __name__ == "__main__":
    battlefield_instance = BattleField()
    battlefield_instance.on_execute()