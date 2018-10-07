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
    sprite_width = 30
    sprite_height = 30
    type = None
    COLON = ":"

    def __init__(self, image, army_x, army_y, global_min_x, global_min_y, global_max_x, global_max_y):
        # formation based on army coordinates
        self.x = random.randint(army_x - 70, army_x + 70)
        self.y = random.randint(army_y - 70, army_y + 70)
        self.global_min_x, self.global_min_y, self.global_max_x, self.global_max_y = global_min_x, global_min_y, global_max_x, global_max_y
        self.image = image
        img = pygame.image.load(self.image)   # sprite
        self.sprite_width = img.get_width()
        self.sprite_height = img.get_height()

    def update(self, army_list_coord_list):
        # update position
        if self.direction == 0 and (self.x + self.step * self.sprite_height + self.sprite_width) <= self.global_max_x:
            for i in range(self.sprite_height*2 + 1):
                if (str(self.x + i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
                elif (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list or (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
            self.x = self.x + self.step * self.sprite_height
            army_list_coord_list.append((str(self.x + self.step * self.sprite_height) + self.COLON + str(self.y)))


        if self.direction == 1 and (self.x - self.step * self.sprite_height) >= self.global_min_x:
            for i in range(self.sprite_height*2 + 1):
                if (str(self.x + i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
                elif (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list or (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
            self.x = self.x - self.step * self.sprite_height
            army_list_coord_list.append((str(self.x - self.step * self.sprite_height) + self.COLON + str(self.y)))

        if self.direction == 2 and (self.y - self.step * self.sprite_height) >= self.global_min_y:
            for i in range(self.sprite_height*2 + 1):
                if (str(self.x + i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
                elif (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list or (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
            self.y = self.y - self.step * self.sprite_height
            army_list_coord_list.append((str(self.x) + self.COLON + str(self.y - self.step * self.sprite_height)))

        if self.direction == 3 and (self.y + self.step * self.sprite_height) <= self.global_max_y:
            for i in range(self.sprite_height*2 + 1):
                if (str(self.x + i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y)) in army_list_coord_list or (str(self.x) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
                elif (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list or (str(self.x + i) + self.COLON + str(self.y + i)) in army_list_coord_list  or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list or (str(self.x - i) + self.COLON + str(self.y - i)) in army_list_coord_list:
                    return ['0:0']
            self.y = self.y + self.step * self.sprite_height
            army_list_coord_list.append(str(self.x) + self.COLON + (str(self.y + self.step * self.sprite_height)))

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