import numpy.random


def coin():
   return numpy.random.randint(2) == 0


def roll_dices(dice_number):
    total = 0
    if dice_number > 0:
        for i in range(0, dice_number):
            roll = numpy.random.randint(6)+1
            if roll == 5:
                total += 1
            if roll == 6:
                total += 2
    return total


if __name__ == '__main__':
    for i in range(100):
        print(roll_dices(1000))
