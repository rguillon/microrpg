from player import Player
from roll import coin
from statistic import Statistic


class Fight:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.winner_stat = Statistic()
        self.nb_round_stat = Statistic()
        self.first_player_stat = Statistic()
        self.damage_stat = Statistic()

    def fight(self):
        print("-" * 20)
        self.p1.damage = 0
        self.p2.damage = 0

        attacker = None
        defender = None
        r1 = self.p1.roll_initiative()
        r2 = self.p2.roll_initiative()

        if r1 > r2:
            attacker = self.p1
            defender = self.p2
        else:
            attacker = self.p2
            defender = self.p1

        if r1 == r2 and coin():
            attacker = self.p1
            defender = self.p2

        #attacker = self.p1
        #defender = self.p2

        #if coin():
        #    attacker = self.p2
        #    defender = self.p1

        first_player = attacker
        Is_Done = False
        first_player = attacker
        Is_Done = False

        nb_round = 1
        while not Is_Done:
            print("Round %d : " % nb_round)
            if attacker == self.p1:
                print("    P1 attack")
            else:
                print("    P2 attack")

            print("    P1: life %d damage %d" % (p1.life, p1.damage))
            print("    P2: life %d damage %d" % (p2.life, p2.damage))
            ra = attacker.roll_attack()
            rd = defender.roll_defense()
            print("    Ra %d Rd %d" % (ra, rd))
            result = ra - rd
            if result > 0:
                defender.damage += result
                if defender.damage >= defender.life:
                    Is_Done = True
            if not Is_Done:
                tmp = attacker
                attacker = defender
                defender = tmp
                nb_round += 1
        result = ""
        if self.p1 == attacker:
            result = "P1 win in round"
        else:
            result = "P2 win in round"
        print(result)
        self.winner_stat.add_event(result)
        self.nb_round_stat.add_event(nb_round)

        if first_player == attacker:
            self.first_player_stat.add_event("First player win")
        else:
            self.first_player_stat.add_event("First player lose")

        if self.p1.damage == 0:
            self.damage_stat.add_event("P1 ONLY")
        else:
            if self.p2.damage == 0:
                self.damage_stat.add_event("P2 ONLY")
            else:
                self.damage_stat.add_event("P1 and P2")

        return result


if __name__ == '__main__':
    p1 = Player(intel=0, dext=8, const=6, char=0, attack_bonus=0, defense_bonus=0)
    p2 = Player(intel=0, dext=6, const=6, char=0, attack_bonus=0, defense_bonus=0)

    fight = Fight(p1, p2)
    for i in range(10000):
        fight.fight()

    fight.winner_stat.display_events()
    fight.nb_round_stat.display_events()
    fight.first_player_stat.display_events()
    fight.damage_stat.display_events()
