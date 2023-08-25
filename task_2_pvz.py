# Растения против зомби

def pvz(zombies: list, plants: list):
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


print(pvz([1, 3, 5, 7], [2, 4, 6, 8]))
print(pvz([1, 3, 5, 7], [2, 4, 0, 8]))
print(pvz([2, 1, 1, 1], [1, 2, 1, 1]))
print(pvz([1, 3, 5, 7], [2, 4]))


def test_true_1():
    assert pvz([1, 3, 5, 7], [2, 4, 6, 8])


def test_true_2():
    assert pvz([1, 3, 5, 7], [2, 4, 0, 8])


def test_true_3():
    assert pvz([2, 1, 1, 1], [1, 2, 1, 1])


def test_false():
    assert not pvz([1, 3, 5, 7], [2, 4])
