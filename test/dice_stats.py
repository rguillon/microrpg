import dice


def print_success_chances(dices, success_range):
    results = {}
    for nb_success in success_range:
        tot = 0.0
        for roll in dices.rolls:
            if roll >= nb_success:
                tot = tot + dices.get_rolls()[roll]
        results[nb_success]= tot / dices.total()
        print ("&%2.f\\%%" % (100 * tot/dices.total()) , end='')

    print("\\\\")

def main():
    d = dice.De()
    for i in range(1,21):
        print_success_chances(d, (1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20))
        d = d + dice.De()


main()
