import random


def get_fuzzy_value_for_speed(speed):
    if speed == "Fast":
        return random.randint(4,5)
    elif speed == "Medium":
        return random.randint(2,3)
    elif speed == "Slow":
        return random.randint(1,1)
