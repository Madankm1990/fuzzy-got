from random import randrange

from game.Skeleton import Skeleton

class Goblin(Skeleton):

    def __init__(self, image,attack_image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y, idx):
        Skeleton.__init__(self, image, attack_image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y)
        self.health = 100
        self.attack = "low"
        self.speed = "fast"
        self.type = "G"
        self.scan_range = 5
        self.unique_id = "G" + str(idx)


    def fuzzy_move(self, FuzzyRules, grid, _display_surf, temp_bot_coord_dict):
        # scan the stage
        goblin_count, ogre_count, troll_count = self.scan_stage(grid)
        motive = None

        if ogre_count == 0 and troll_count == 0:
            decision = "move"
            motive = "explore"
        else:
            decision = FuzzyRules.make_fuzzy_decision(goblin_count, ogre_count, troll_count, self.type)

        if decision == "stay":
            pass

        elif decision == "attack":
            self.attack_rate = FuzzyRules.get_fuzzy_value_for_attack(self.attack)
            # decide where to attack
            if self.gridx - 1 >= 0 and grid[self.gridx - 1][self.gridy] != self.type and grid[self.gridx - 1][self.gridy] != '0':
                enemy_bot = temp_bot_coord_dict[str(self.gridx - 1) + ":" + str(self.gridy)]
                grid,enemy_bot = self.update(grid, _display_surf, True, "left", enemy_bot)
                temp_bot_coord_dict[str(self.gridx - 1) + ":" + str(self.gridy)] = enemy_bot
            elif self.gridx + 1 <= len(grid[0]) and grid[self.gridx + 1][self.gridy] != self.type and grid[self.gridx + 1][self.gridy] != '0':
                enemy_bot = temp_bot_coord_dict[str(self.gridx + 1) + ":" + str(self.gridy)]
                grid,enemy_bot = self.update(grid, _display_surf, True, "right", enemy_bot)
                temp_bot_coord_dict[str(self.gridx + 1) + ":" + str(self.gridy)] = enemy_bot
            elif self.gridy + 1 <= len(grid) and grid[self.gridx][self.gridy + 1] != self.type and grid[self.gridx][self.gridy + 1] != '0':
                enemy_bot = temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy + 1)]
                grid,enemy_bot = self.update(grid, _display_surf, True, "down", enemy_bot)
                temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy + 1)] = enemy_bot
            elif self.gridy - 1 >= 0 and grid[self.gridx][self.gridy - 1] != self.type and grid[self.gridx][self.gridy - 1] != '0':
                enemy_bot = temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy - 1)]
                grid,enemy_bot = self.update(grid, _display_surf, True, "up", enemy_bot)
                temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy - 1)] = enemy_bot
            else:  # move towards enemy
                motive = "towards"
                decision = "move"

        if decision == "move":
            self.speed = "fast"
            proximity, side = self.get_status_of_enemy(grid, motive)
            if proximity == 1:
                self.speed = "slow"
            elif proximity == 2:
                self.speed = "medium"

            # determine fuzzy speed step
            self.step = FuzzyRules.get_fuzzy_value_for_speed(self.speed)
            if side == "up":
                self.moveUp()
            elif side == "left":
                self.moveLeft()
            elif side == "right":
                self.moveRight()
            elif side == "down":
                self.moveDown()

            grid, enemy_bot = self.update(grid, _display_surf, False, None, None)

        return grid, temp_bot_coord_dict

    def get_status_of_enemy(self, grid, motive):
        proximity = 3
        side = "up"
        if motive is not None and motive == "explore":
            # either make a random move or
            # group together and move in unison
            random_decision = int(randrange(1, 6))
            if random_decision % 5 == 0:
                for proximity in range(2):
                    side = self.find_others(grid, [self.type], proximity + 1)
                    if side:
                        return proximity + 1, side
            else:  # random pick
                if random_decision == 1:
                    return 3, "up"
                elif random_decision == 2:
                    return 3, "left"
                elif random_decision == 3:
                    return 3, "right"
                elif random_decision == 4:
                    return 3, "down"
        for proximity in range(2):
            side = self.find_others(grid, ["O", "T"], proximity + 1)
            if side and motive is not None and motive == "towards":
                return proximity + 1, side
            elif side and motive is None:  # run away in opposite direction!!
                if side == "up":
                    return 3, "down"
                elif side == "down":
                    return 3, "up"
                elif side == "left":
                    return 3, "right"
                elif side == "right":
                    return 3, "left"

        return proximity, side


    def find_others(self, grid, person_type, proximity):
        for person in person_type:
            if self.gridx - proximity >= 0 and grid[self.gridx - proximity][self.gridy] == person:
                return "left"
            elif self.gridx + proximity <= len(grid[0]) and grid[self.gridx + proximity][self.gridy] == person:
                return "right"
            elif self.gridy + proximity <= len(grid) and grid[self.gridx][self.gridy + proximity] == person:
                return "down"
            elif self.gridy + proximity >= 0 and grid[self.gridx][self.gridy - proximity] == person:
                return "up"
        return None