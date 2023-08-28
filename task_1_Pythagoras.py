# Проверка треугольника по теореме Пифагора
from init_log import init_log
import logging


def pythagoras(length_of_sides: list):
    for side_len in length_of_sides:
        if side_len == 0:
            raise Exception("Side can't be 0 or lower")
    hypotenuse = max(length_of_sides)
    length_of_sides.remove(hypotenuse)
    return length_of_sides[0] ** 2 + length_of_sides[1] ** 2 == hypotenuse ** 2


init_log()

logging.info(pythagoras([5, 3, 4]))

logging.info(pythagoras([6, 8, 10]))

logging.info(pythagoras([100, 1, 65]))


def test_true_1():
    result = pythagoras([5, 3, 4])
    assert result


def test_true_2():
    result = pythagoras([6, 8, 10])
    assert result


def test_false():
    result = pythagoras([100, 3, 65])
    assert not result
