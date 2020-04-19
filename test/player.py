from roll import roll_dices

class Player:

    def __init__(self, intel, dext, const, char, attack_bonus, defense_bonus):
        self.intel = intel
        self.dext = dext
        self.const = const
        self.char = char
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.life = dext + const
        self.damage = 0

    def roll_attack(self):
        return roll_dices(self.dext + self.attack_bonus - self.damage)

    def roll_defense(self):
        return roll_dices(self.dext + self.defense_bonus - self.damage)

    def roll_initiative(self):
        return roll_dices(self.dext)

if __name__ == '__main__':
    p1 = Player(intel = 0, const=6, dext=6, char=0, attack_bonus=0, defense_bonus=0)

    print("Roll : %d"%(p1.roll_attack()))