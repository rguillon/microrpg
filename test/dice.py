class Dice():

    def __init__(self, rolls):
        self.rolls = rolls


    def __add__(self, other):
        new_rolls = {}

        for i in self.rolls:
            for j in other.rolls:
                v = i+j
                p = self.rolls[i] * other.rolls[j]

                try:
                    new_rolls[v] = new_rolls[v] + p
                except KeyError:
                    new_rolls[v] = p
        return Dice(new_rolls)

    def __str__(self):
        return str(self.rolls) + " " + str(self.total())

    def total(self):
        total = 0.0
        for val in self.rolls:
            total = total + self.rolls[val]
        return total

    def normalize(self):
        total = self.total()

        for val in self.rolls:
            self.rolls[val] = self.rolls[val]/total
        return self

    def get_rolls(self):
        return self.rolls

def D(face):
    rolls = {}
    for i in range (1,face+1):
        rolls[i] = 1.0
    return Dice(rolls)

def De():
    #return Dice({1:0,2:0,3:0,4:0,5:1,6:2})
    return Dice({0:4,1:1,2:1})

def main():
    d = De()
    for i in range(1,16):
        print("=================================== %d Dices roll:"%(i))
        print(d)
        d = d + De()
if __name__ == '__main__':
    main()
