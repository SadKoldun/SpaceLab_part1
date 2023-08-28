# Растения против зомби
import logging

from init_log import init_log


def pvz(zombies: list, plants: list):
    for health in zombies:
        if health < 0:
            raise Exception("Health can't be lower than 0 (Zombies)")
    for health in plants:
        if health < 0:
            raise Exception("Health can't be lower than 0 (Plants)")
    step = min(len(zombies), len(plants))
    for index in range(step):
        if zombies[index] == plants[index]:
            zombies[index] = 0
            plants[index] = 0
        elif zombies[index] > plants[index]:
            plants[index] = 0
        elif zombies[index] < plants[index]:
            zombies[index] = 0
    zombies_hp = sum(zombies)
    plants_hp = sum(plants)
    if zombies_hp == plants_hp:
        return True
    return zombies_hp < plants_hp


init_log()

logging.info(pvz([1, 3, 5, 7], [2, 4, 6, 8]))
logging.info(pvz([1, 3, 5, 7], [2, 4, 0, 8]))
logging.info(pvz([2, 1, 1, 1], [1, 2, 1, 1]))
logging.info(pvz([1, 3, 5, 7], [2, 4]))


def test_true_1():
    assert pvz([1, 3, 5, 7], [2, 4, 6, 8])


def test_true_2():
    assert pvz([1, 3, 5, 7], [2, 4, 0, 8])


def test_true_3():
    assert pvz([2, 1, 1, 1], [1, 2, 1, 1])


def test_false():
    assert not pvz([1, 3, 5, 7], [2, 4])
