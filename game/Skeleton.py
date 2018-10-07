import random
import pygame

class Skeleton:
    x = 0
    y = 0
    direction = -1
    step = 1
    image = None
    health = 0
    attack = None
    speed = None
    _image_surf = None
    sprite_width = 0
    sprite_height = 0
    type = None
    COLON = ":"

    def __init__(self, image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y):
        # formation based on army coordinates
        self.x = random.randint(army_x -50, army_x + 50)
        self.y = random.randint(army_y - 50, army_y + 50)
        self.global_min_x, self.global_min_y, self.global_max_x, self.global_max_y = global_min_x, global_min_y, global_max_x, global_max_y
        self.image = image
        img = pygame.image.load(self.image)   # sprite
        self.sprite_width = img.get_width()
        self.sprite_height = img.get_height()

    def update(self, army_list_coord_list):
        # update position
        if self.direction == 0 and (self.x + self.step + self.sprite_width) <= self.global_max_x and (str(self.x + self.step) + self.COLON + str(self.y)) not in army_list_coord_list:
            self.x = self.x + self.step
            army_list_coord_list.append((str(self.x + self.step) + self.COLON + str(self.y)))

        if self.direction == 1 and (self.x - self.step) >= self.global_min_x and (str(self.x - self.step) + self.COLON + str(self.y)) not in army_list_coord_list:
            self.x = self.x - self.step
            army_list_coord_list.append((str(self.x - self.step) + self.COLON + str(self.y)))

        if self.direction == 2 and (self.y - self.step) >= self.global_min_y and (str(self.y - self.step) + self.COLON + str(self.x)) not in army_list_coord_list:
            self.y = self.y - self.step
            army_list_coord_list.append((str(self.y - self.step) + self.COLON + str(self.x)))

        if self.direction == 3 and (self.y + self.step + self.sprite_height) <= self.global_max_y and (str(self.y + self.step) + self.COLON + str(self.x)) not in army_list_coord_list:
            self.y = self.y + self.step
            army_list_coord_list.append((str(self.y + self.step) + self.COLON + str(self.x)))

        return army_list_coord_list


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

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))