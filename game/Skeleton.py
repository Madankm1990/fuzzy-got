from random import randrange
import pygame

class Skeleton:
    x = 0
    y = 0
    direction = -1
    step = 1
    image = None
    attack_image = None
    health = 0
    attack = None
    attack_rate = 0
    attack_charge_full = True
    speed = None
    _image_surf = None
    _attack_surf = None
    sprite_width = 30
    sprite_height = 30
    type = None
    COLON = ":"
    scan_range = None
    dead = False
    unique_id = None

    def __init__(self, image, attack_image, army_x, army_y, global_min_x, global_min_y, global_max_x, global_max_y):
        # formation based on army coordinates
        self.global_min_x, self.global_min_y, self.global_max_x, self.global_max_y = global_min_x, global_min_y, global_max_x, global_max_y
        self.image = image
        self.attack_image = attack_image
        img = pygame.image.load(self.image)   # sprite

        self.sprite_width = img.get_width()
        self.sprite_height = img.get_height()
        self.gridy = army_y
        self.gridx = army_x
        self.x = army_x * self.sprite_width
        self.y = army_y * self.sprite_height

    def update(self, grid, display_surf, to_attack, direction, enemy_bot, temp_bot_coord_dict):
        if to_attack and self.attack_charge_full:
            enemy_bot = self.attack_enemy(display_surf, direction, enemy_bot)
            if enemy_bot.dead:
                grid[enemy_bot.gridx][enemy_bot.gridy] = '0'
        else:
            self.attack_charge_full = True
            # update position
            if self.direction == 0 and (self.gridx + self.step) < self.global_max_x:
                if grid[(self.gridx + self.step)][self.gridy] == '0':
                    grid[(self.gridx)][self.gridy] = '0'
                    self.x = self.x + self.step * self.sprite_width
                    if str(self.gridx) + ":" + str(self.gridy) in temp_bot_coord_dict:
                        temp_bot_coord_dict.pop(str(self.gridx) + ":" + str(self.gridy), None)
                    self.gridx += self.step
                    grid[(self.gridx)][self.gridy] = self.type
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy)] = self

            if self.direction == 1 and (self.gridx - self.step) > self.global_min_x:
                if grid[(self.gridx - self.step)][self.gridy] == '0':
                    grid[(self.gridx)][self.gridy] = '0'
                    self.x = self.x - self.step * self.sprite_width
                    if str(self.gridx) + ":" + str(self.gridy) in temp_bot_coord_dict:
                        temp_bot_coord_dict.pop(str(self.gridx) + ":" + str(self.gridy), None)
                    self.gridx -= self.step
                    grid[(self.gridx)][self.gridy] = self.type
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy)] = self

            if self.direction == 2 and (self.gridy - self.step) > self.global_min_y:
                if grid[(self.gridx)][self.gridy - self.step] == '0':
                    grid[(self.gridx)][self.gridy] = '0'
                    self.y = self.y - self.step * self.sprite_height
                    if str(self.gridx) + ":" + str(self.gridy) in temp_bot_coord_dict:
                        temp_bot_coord_dict.pop(str(self.gridx) + ":" + str(self.gridy), None)
                    self.gridy -= self.step
                    grid[(self.gridx)][self.gridy] = self.type
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy)] = self

            if self.direction == 3 and (self.gridy + self.step) < self.global_max_y:
                if grid[(self.gridx)][self.gridy + self.step] == '0':
                    grid[(self.gridx)][self.gridy] = '0'
                    self.y = self.y + self.step * self.sprite_height
                    if str(self.gridx) + ":" + str(self.gridy) in temp_bot_coord_dict:
                        temp_bot_coord_dict.pop(str(self.gridx) + ":" + str(self.gridy), None)
                    self.gridy += self.step
                    grid[(self.gridx)][self.gridy] = self.type
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy)] = self

        self.draw(display_surf, self._image_surf)
        return grid, enemy_bot, temp_bot_coord_dict


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def create_avatar(self):
        self._image_surf = pygame.image.load(self.image).convert()
        self._attack_surf = pygame.image.load(self.attack_image).convert()

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


    def sense_range(self, rang, grid):
        step_path = int(rang/2)
        goblin_count = 0
        ogre_count = 0
        troll_count = 0

        for i in range(-step_path, step_path):
            for j in range(-step_path, step_path):
                if i >= 0 and self.gridx + i < len(grid) and j >=0 and self.gridy + j < len(grid[0]):
                    if grid[self.gridx + i][self.gridy + j] == 'G':
                        goblin_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'O':
                        ogre_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'T':
                        troll_count+=1

                elif i >=0 and self.gridx + i < len(grid) and j<0 and self.gridy + j >= 0:
                    if grid[self.gridx + i][self.gridy + j] == 'G':
                        goblin_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'O':
                        ogre_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'T':
                        troll_count+=1

                elif i<0 and self.gridx + i >= 0 and j>=0 and self.gridy + j < len(grid[0]):
                    if grid[self.gridx + i][self.gridy + j] == 'G':
                        goblin_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'O':
                        ogre_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'T':
                        troll_count+=1

                elif i<0 and self.gridx - i >= 0 and j<0 and self.gridy +j >= 0:
                    if grid[self.gridx + i][self.gridy + j] == 'G':
                        goblin_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'O':
                        ogre_count+=1
                    elif grid[self.gridx + i][self.gridy + j] == 'T':
                        troll_count+=1
        return goblin_count, ogre_count, troll_count


    def attack_enemy(self, surface, direction, enemy_bot):
        self.attack_charge_full = False
        if direction == "up":
            surface.blit(self._attack_surf, (self.x, self.y - 1 * self.sprite_height))
        elif direction == "down":
            surface.blit(self._attack_surf, (self.x, self.y + 1 * self.sprite_height))
        elif direction == "left":
            surface.blit(self._attack_surf, (self.x - 1 * self.sprite_width, self.y))
        elif direction == "right":
            surface.blit(self._attack_surf, (self.x + 1 * self.sprite_width, self.y))

        enemy_bot.health-=self.attack_rate
        print(self.unique_id + " ATTACKS " + enemy_bot.unique_id + " WITH A FORCE OF " + str(self.attack_rate) + " LEAVING ENEMY HEART AT " + str(enemy_bot.health))
        if enemy_bot.health <= 0:
            enemy_bot.is_dead()
            print(enemy_bot.unique_id + " HAS DIED!")

        return enemy_bot


    def is_dead(self):
        self.dead = True

    def scan_stage(self, grid):
        goblin_count, ogre_count, troll_count = self.sense_range(self.scan_range,grid)
        print("*******" + self.unique_id + "*********")
        print("Goblin Count: " + str(goblin_count))
        print("Ogre Count: " + str(ogre_count))
        print("Troll Count: " + str(troll_count))
        print("****************")
        return goblin_count, ogre_count, troll_count
