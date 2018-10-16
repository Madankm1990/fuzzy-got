from pygame.locals import *
from game import Goblin, Ogre, Troll
from random import randrange
import pygame
from os.path import dirname as up
import time

from fuzzy import FuzzyRules


class BattleField:
    base_path = up(up(__file__))
    _running = True
    _display_surf = None
    global_army_group = []
    goblin_army = 10
    ogre_army = 5
    troll_army = 3
    windowWidth = 1000
    windowHeight = 1000
    sprite_height = 60
    sprite_width = 60
    army_list_coord_list = ['0:0']
    grid = None
    attack_image = None

    def on_init(self):
        pygame.init()

        # create the stage
        self.grid = [['0' for x in range(int(self.windowHeight/self.sprite_height))] for y in range(int(self.windowWidth/self.sprite_width))]
        #print(len(grid))  # 40*33

        # global army group - consists of all warriors
        for goblin_idx in range(self.goblin_army):
            while True:
                random_army_starting_coord_x = randrange(self.goblin_army, len(self.grid))
                random_army_starting_coord_y = randrange(self.goblin_army, len(self.grid[0]))
                if self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
            goblin = Goblin.Goblin(self.base_path + "/images/goblin_up.png",self.base_path + "/images/goblin_down.png",self.base_path + "/images/goblin_left.png",self.base_path + "/images/goblin_right.png", self.base_path + "/images/attack_goblin.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), goblin_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = goblin.type
            self.global_army_group.append(goblin)

            # init Fuzzy rules
            self.fuzzy_rules = FuzzyRules.FuzzyRules()


        for ogre_idx in range(self.ogre_army):
            while True:
                random_army_starting_coord_x = randrange(self.ogre_army, len(self.grid))
                random_army_starting_coord_y = randrange(self.ogre_army, len(self.grid[0]))
                if self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
            ogre = Ogre.Ogre(self.base_path + "/images/ogre_up.png",self.base_path + "/images/ogre_down.png",self.base_path + "/images/ogre_left.png",self.base_path + "/images/ogre_right.png", self.base_path + "/images/attack_ogre.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), ogre_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = ogre.type
            self.global_army_group.append(ogre)


        for troll_idx in range(self.troll_army):
            while True:
                random_army_starting_coord_x = randrange(self.troll_army, len(self.grid))
                random_army_starting_coord_y = randrange(self.troll_army, len(self.grid[0]))
                if self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
            troll = Troll.Troll(self.base_path + "/images/troll_up.png",self.base_path + "/images/troll_down.png",self.base_path + "/images/troll_left.png",self.base_path + "/images/troll_right.png", self.base_path + "/images/attack_troll.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), troll_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = troll.type
            self.global_army_group.append(troll)


        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        for bot in self.global_army_group:
            bot.create_avatar()

        pygame.display.set_caption('Goblins Ogres & Trolls - The Grand GOT War')
        self._running = True


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill((160, 184, 255))
        #self._display_surf.fill((0,0,0))
        # track all coords of all bots
        temp_bot_coord_dict = {}
        for bot in self.global_army_group:
            temp_bot_coord_dict[str(bot.gridx) + ":" + str(bot.gridy)] = bot

        # render all bots - may actors play their role!!
        for bot in self.global_army_group:
            self.grid, temp_bot_coord_dict = bot.fuzzy_move(self.fuzzy_rules, self.grid, self._display_surf, temp_bot_coord_dict)

        self.global_army_group = []
        for key, value in temp_bot_coord_dict.items():
            if value.dead is False:
                self.global_army_group.append(value)
            else:
                self.grid[value.gridx][value.gridy] = '0'
                if value.type == 'G':
                    self.goblin_army -= 1
                elif value.type == 'O':
                    self.ogre_army -= 1
                elif value.type == 'T':
                    self.troll_army -= 1

        print("****************")
        print("GOBLINS:" + str(self.goblin_army) if self.goblin_army >=0 else 0)
        print("OGRES:" + str(self.ogre_army) if self.ogre_army >=0 else 0)
        print("TROLLS:" + str(self.troll_army) if self.troll_army >=0 else 0)
        print("****************")

        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()
        # https://orig00.deviantart.net/9c46/f/2010/117/d/7/t8bit___character_sprite_by_ricardo_o_terrivel.png
        # https://orig00.deviantart.net/0588/f/2011/229/5/e/hypon_and_scorch__aura_sphere_by_scorchth-d46vme4.png


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.on_render()

            # TO CHANGE DELAY
            time.sleep(900.0 / 1000.0)
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