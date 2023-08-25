# Проверка треугольника по теореме Пифагора
import logging

logging.basicConfig(level=logging.INFO)


def pythagoras(length_of_sides: list):
    hypotenuse = max(length_of_sides)
    length_of_sides.remove(hypotenuse)
    return length_of_sides[0] ** 2 + length_of_sides[1] ** 2 == hypotenuse ** 2


logging.info("Start")
print(pythagoras([5, 3, 4]))
print(pythagoras([6, 8, 10]))
print(pythagoras([100, 1, 65]))


def test_true_1():
    result = pythagoras([5, 3, 4])
    assert result


def test_true_2():
    result = pythagoras([6, 8, 10])
    assert result


def test_false():
    result = pythagoras([100, 3, 65])
    assert not result
