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
    goblin_army = 0
    ogre_army = 0
    troll_army = 3
    windowWidth = 1000
    windowHeight = 1000
    sprite_height = 60
    sprite_width = 60
    army_list_coord_list = ['0:0']
    grid = None
    attack_image = None
    _mountain_surf = None
    seconds = 30

    def on_init(self):
        pygame.init()
        self.title_font = pygame.font.SysFont('Sans', 20)
        self.ending_font = pygame.font.SysFont('Sans', 50)
        self.sprite_font = pygame.font.SysFont('Sans', 15)
        self.clock = pygame.time.Clock()

        # set video mode
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        # create the stage
        self.grid = [['0' for x in range(int(self.windowHeight/self.sprite_height))] for y in range(int(self.windowWidth/self.sprite_width))]

        # init Fuzzy rules
        self.fuzzy_rules = FuzzyRules.FuzzyRules()

        # build mountain
        self.center_x = int(len(self.grid[0]) / 2)
        self.center_y = int(len(self.grid) / 2)
        self._mountain_surf = pygame.transform.scale(pygame.image.load(self.base_path + "/images/mountain.png"), (self.sprite_width, self.sprite_height)).convert()
        self._forest_surf = pygame.transform.scale(pygame.image.load(self.base_path + "/images/forest.png"),
                                                     (self.sprite_width, self.sprite_height)).convert()

        for mountain_idx_x in range(len(self.grid[0])):
            self._display_surf.blit(self._mountain_surf, ((mountain_idx_x * self._mountain_surf.get_width()),0))
            self.grid[mountain_idx_x][0] = 'M'

        for mountain_idx_x in range(len(self.grid[0])):
            self._display_surf.blit(self._mountain_surf, ((mountain_idx_x * self._mountain_surf.get_width()), self._mountain_surf.get_height() * len(self.grid) - 1))
            self.grid[mountain_idx_x][len(self.grid) - 1] = 'M'

        for mountain_idx_y in range(len(self.grid)):
            self._display_surf.blit(self._mountain_surf, (len(self.grid[0]) * self._mountain_surf.get_width(), mountain_idx_y * self._mountain_surf.get_height()))
            self.grid[len(self.grid[0]) - 1][mountain_idx_y] = 'M'

        for mountain_idx_y in range(len(self.grid)):
            self._display_surf.blit(self._mountain_surf, (0, mountain_idx_y * self._mountain_surf.get_height()))
            self.grid[0][mountain_idx_y] = 'M'


        for mountain_idx_x in range(-4, 4):
            for mountain_idx_y in range(-4, 4):
                if mountain_idx_x % 2 ==0 and mountain_idx_x == mountain_idx_y or abs(mountain_idx_x - mountain_idx_y) > 2:
                    self._display_surf.blit(self._forest_surf, ((self.center_x * self.sprite_width) + (mountain_idx_x * self._mountain_surf.get_width()), (self.center_y * self.sprite_height) + (mountain_idx_y * self._mountain_surf.get_height())))
                    self.grid[self.center_x + mountain_idx_x][self.center_y + mountain_idx_y] = 'M'

        # global army group - consists of all warriors
        for goblin_idx in range(self.goblin_army):
            temp_num = 1
            while True:
                random_army_starting_coord_x = randrange(len(self.grid[0]) - temp_num * 2, len(self.grid[0]) - temp_num)
                random_army_starting_coord_y = randrange(len(self.grid) - temp_num * 2, len(self.grid) - temp_num)
                if random_army_starting_coord_x < len(self.grid[0]) and random_army_starting_coord_y < len(self.grid) and self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
                temp_num += 1
            goblin = Goblin.Goblin(self.base_path + "/images/goblin_up.png",self.base_path + "/images/goblin_down.png",self.base_path + "/images/goblin_left.png",self.base_path + "/images/goblin_right.png", self.base_path + "/images/attack_goblin.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), goblin_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = goblin.type
            self.global_army_group.append(goblin)


        for ogre_idx in range(self.ogre_army):
            temp_num = 1
            while True:
                random_army_starting_coord_x = randrange(0 + temp_num, 0 + temp_num * 2)
                random_army_starting_coord_y = randrange(0 + temp_num, 0 + temp_num * 2)
                if random_army_starting_coord_x < len(self.grid[0]) and random_army_starting_coord_y < len(self.grid) and self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
                temp_num += 1
            ogre = Ogre.Ogre(self.base_path + "/images/ogre_up.png",self.base_path + "/images/ogre_down.png",self.base_path + "/images/ogre_left.png",self.base_path + "/images/ogre_right.png", self.base_path + "/images/attack_ogre.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), ogre_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = ogre.type
            self.global_army_group.append(ogre)


        for troll_idx in range(self.troll_army):
            temp_num = 1
            while True:
                random_army_starting_coord_x = randrange(self.center_x - temp_num, self.center_x + temp_num)
                random_army_starting_coord_y = randrange(self.center_y - temp_num, self.center_y + temp_num)
                if random_army_starting_coord_x < len(self.grid[0]) and random_army_starting_coord_y < len(self.grid) and self.grid[random_army_starting_coord_x][random_army_starting_coord_y] == '0':
                    break
                temp_num += 1
            troll = Troll.Troll(self.base_path + "/images/troll_up.png",self.base_path + "/images/troll_down.png",self.base_path + "/images/troll_left.png",self.base_path + "/images/troll_right.png", self.base_path + "/images/attack_troll.png", random_army_starting_coord_x, random_army_starting_coord_y, 0, 0, len(self.grid), len(self.grid[0]), troll_idx)
            self.grid[random_army_starting_coord_x][random_army_starting_coord_y] = troll.type
            self.global_army_group.append(troll)


        for bot in self.global_army_group:
            bot.create_avatar()

        pygame.display.set_caption('Ninjas, Samurais & Mages - The Grand N.S.M. War')
        self._running = True


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill((120, 100, 25))  # ground

        # mountains and forest
        for mountain_idx_x in range(len(self.grid[0])):
            self._display_surf.blit(self._mountain_surf, ((mountain_idx_x * self._mountain_surf.get_width()),0))
            self.grid[mountain_idx_x][0] = 'M'

        for mountain_idx_x in range(len(self.grid[0])):
            self._display_surf.blit(self._mountain_surf, ((mountain_idx_x * self._mountain_surf.get_width()), self._mountain_surf.get_height() * len(self.grid) - 1))
            self.grid[mountain_idx_x][len(self.grid) - 1] = 'M'

        for mountain_idx_y in range(len(self.grid)):
            self._display_surf.blit(self._mountain_surf, (len(self.grid[0]) * self._mountain_surf.get_width(), mountain_idx_y * self._mountain_surf.get_height()))
            self.grid[len(self.grid[0]) - 1][mountain_idx_y] = 'M'
        self._display_surf.blit(self._mountain_surf, (len(self.grid[0]) * self._mountain_surf.get_width(), len(self.grid) * self._mountain_surf.get_height()))

        for mountain_idx_y in range(len(self.grid)):
            self._display_surf.blit(self._mountain_surf, (0, mountain_idx_y * self._mountain_surf.get_height()))
            self.grid[0][mountain_idx_y] = 'M'

        for mountain_idx_x in range(-4, 4):
            for mountain_idx_y in range(-4, 4):
                if mountain_idx_x % 2 ==0 and mountain_idx_x == mountain_idx_y or abs(mountain_idx_x - mountain_idx_y) > 2:
                    self._display_surf.blit(self._forest_surf, ((self.center_x * self.sprite_width) + (mountain_idx_x * self._mountain_surf.get_width()), (self.center_y * self.sprite_height) + (mountain_idx_y * self._mountain_surf.get_height())))

        # heading and timer
        text = self.title_font.render('Ninjas Samurais & Mages - The Grand NSM War', True, (255, 255, 255), (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = int(len(self.grid[0]) / 2) * self.sprite_width
        textrect.centery = int(self.sprite_height / 2)
        self._display_surf.blit(text, textrect)

        # top right - count of agents
        text = self.sprite_font.render("Ninja: " + str(self.goblin_army), True, (255, 255, 255), (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = len(self.grid[0]) * self.sprite_width
        textrect.centery = int(self.sprite_height / 2 - 20)
        self._display_surf.blit(text, textrect)
        text = self.sprite_font.render("Samurai: " + str(self.ogre_army) , True, (255, 255, 255), (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = len(self.grid[0]) * self.sprite_width
        textrect.centery = int(self.sprite_height / 2)
        self._display_surf.blit(text, textrect)
        text = self.sprite_font.render("Mage: " + str(self.troll_army), True, (255, 255, 255), (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = len(self.grid[0]) * self.sprite_width
        textrect.centery = int(self.sprite_height / 2 + 20)
        self._display_surf.blit(text, textrect)

        # bottom right - clock
        self.clock.tick(4)
        text = self.title_font.render("Time Remaining: " + str(int(self.seconds)), True, (255, 255, 255), (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = (len(self.grid[0]) * self.sprite_width) - 100
        textrect.centery = (len(self.grid) * self.sprite_height) + 25
        self._display_surf.blit(text, textrect)
        self.seconds -= 0.25


        # track all coords of all bots
        temp_bot_coord_dict = {}
        for bot in self.global_army_group:
            temp_bot_coord_dict[str(bot.gridx) + ":" + str(bot.gridy)] = bot

        # render all bots - may actors play their role!!
        for bot in self.global_army_group:
            self.grid, temp_bot_coord_dict = bot.fuzzy_move(self.fuzzy_rules, self.grid, self._display_surf, temp_bot_coord_dict, highlighter=True)

        self.global_army_group = []
        self.goblin_army = 0
        self.ogre_army = 0
        self.troll_army = 0

        set_sprites = set()
        for key, value in temp_bot_coord_dict.items():
            set_sprites.add(value)

        for value in set_sprites:
            if value.dead is False:
                self.global_army_group.append(value)
                if value.type == 'G':
                    self.goblin_army += 1
                elif value.type == 'O':
                    self.ogre_army += 1
                elif value.type == 'T':
                    self.troll_army += 1
            else:
                self.grid[value.gridx][value.gridy] = '0'

        #print("****************")
        #print("NINJAS:" + str(self.goblin_army) if self.goblin_army >=0 else 0)
        #print("SAMURAIS:" + str(self.ogre_army) if self.ogre_army >=0 else 0)
        #print("MAGES:" + str(self.troll_army) if self.troll_army >=0 else 0)
        #print("****************")

        winner_decided = False
        winner = 'Draw'
        war = False  # True if multi-agents wage war; else False

        # only one army standing - declare winner
        if war:
            if self.goblin_army == 0 and self.ogre_army == 0:
                winner_decided = True
                winner = 'Mage'
            elif self.goblin_army == 0 and self.troll_army == 0:
                winner_decided = True
                winner = 'Samurai'
            if self.troll_army == 0 and self.ogre_army == 0:
                winner_decided = True
                winner = 'Ninja'

        # time's up
        if self.seconds <= 0 or winner_decided:
            text = self.ending_font.render("Game Over! Winner: " + winner, True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = (self.center_x * self.sprite_width)
            textrect.centery = (self.center_y * self.sprite_height)
            self._display_surf.blit(text, textrect)
            pygame.display.flip()
            time.sleep(5)
            self._running = False

        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.on_render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
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