from random import randrange

from game.Skeleton import Skeleton

class Troll(Skeleton):

    def __init__(self, up_image, down_image, left_image, right_image, attack_image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y, idx):
        Skeleton.__init__(self, up_image, down_image, left_image, right_image, attack_image, army_x,army_y, global_min_x, global_min_y, global_max_x, global_max_y)
        self.attack = "high"
        self.speed = "slow"
        self.type = "T"
        self.scan_range = 9
        self.unique_id = "T" + str(idx)
        self.max_charge = 3


    def fuzzy_move(self, FuzzyRules, grid, _display_surf, temp_bot_coord_dict):
        try:
            # scan the stage
            goblin_count, ogre_count, troll_count = self.scan_stage(grid)
            motive = None

            if ogre_count == 0 and goblin_count == 0:
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
                    grid,enemy_bot, temp_bot_coord_dict = self.update(grid, _display_surf, True, "left", enemy_bot, temp_bot_coord_dict)
                    temp_bot_coord_dict[str(self.gridx - 1) + ":" + str(self.gridy)] = enemy_bot
                elif self.gridx + 1 < len(grid[0]) and grid[self.gridx + 1][self.gridy] != self.type and grid[self.gridx + 1][self.gridy] != '0':
                    enemy_bot = temp_bot_coord_dict[str(self.gridx + 1) + ":" + str(self.gridy)]
                    grid,enemy_bot, temp_bot_coord_dict = self.update(grid, _display_surf, True, "right", enemy_bot, temp_bot_coord_dict)
                    temp_bot_coord_dict[str(self.gridx + 1) + ":" + str(self.gridy)] = enemy_bot
                elif self.gridy + 1 < len(grid) and grid[self.gridx][self.gridy + 1] != self.type and grid[self.gridx][self.gridy + 1] != '0':
                    enemy_bot = temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy + 1)]
                    grid,enemy_bot, temp_bot_coord_dict = self.update(grid, _display_surf, True, "down", enemy_bot, temp_bot_coord_dict)
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy + 1)] = enemy_bot
                elif self.gridy - 1 >= 0 and grid[self.gridx][self.gridy - 1] != self.type and grid[self.gridx][self.gridy - 1] != '0':
                    enemy_bot = temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy - 1)]
                    grid,enemy_bot, temp_bot_coord_dict = self.update(grid, _display_surf, True, "up", enemy_bot, temp_bot_coord_dict)
                    temp_bot_coord_dict[str(self.gridx) + ":" + str(self.gridy - 1)] = enemy_bot
                else:  # move towards enemy
                    motive = "towards"
                    decision = "move"

            if decision == "move":
                proximity, side = self.get_status_of_enemy(grid, motive)

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

                grid, enemy_bot, temp_bot_coord_dict = self.update(grid, _display_surf, False, None, None, temp_bot_coord_dict)

            return grid, temp_bot_coord_dict
        except:
            return grid, temp_bot_coord_dict


    def get_status_of_enemy(self, grid, motive):
        proximity = 1
        side = "up"
        if motive is not None and motive == "explore":
            # either make a random move or
            # group together and move in unison
            random_decision = int(randrange(1, 5))
            if random_decision == 1:
                return 1, "up"
            elif random_decision == 2:
                return 1, "left"
            elif random_decision == 3:
                return 1, "right"
            elif random_decision == 4:
                return 1, "down"
        for proximity in range(2):
            side = self.find_others(grid, ["O", "G"], proximity + 1)
            if side and motive is not None and motive == "towards":
                print(self.unique_id + " SAYS \"ME GONNA CRUSH YOU!!\"")
                return proximity + 1, side
            elif side and motive is None:  # run away in opposite direction!!
                if side == "up":
                    return 1, "down"
                elif side == "down":
                    return 1, "up"
                elif side == "left":
                    return 1, "right"
                elif side == "right":
                    return 1, "left"

        return proximity, side


    def find_others(self, grid, person_type, proximity):
        count_list = [0,0,0,0]  # left, right, down, up
        for person in person_type:
            if self.gridx - proximity >= 0 and grid[self.gridx - proximity][self.gridy] == person:
                count_list[0]+=1
            elif self.gridx + proximity < len(grid[0]) and grid[self.gridx + proximity][self.gridy] == person:
                count_list[1]+=1
            elif self.gridy + proximity < len(grid) and grid[self.gridx][self.gridy + proximity] == person:
                count_list[2]+=1
            elif self.gridy + proximity >= 0 and grid[self.gridx][self.gridy - proximity] == person:
                count_list[3]+=1

        max_others = count_list.index(max(count_list))
        if max(count_list) > 0:
            if max_others == 0:
                return "left"
            elif max_others == 1:
                return "right"
            elif max_others == 2:
                return "down"
            elif max_others == 3:
                return "up"
        else:
            return None