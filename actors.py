import random

class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print("The wizard {} attacks the {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('You roll {}...'.format(my_roll))
        print('The {} rolls {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("{} has handily triumphed over the {}".format(self.name, creature.name))
            self.level = self.level + creature.level
            print('Our hero has now reached level {}.'.format(self.level))
            if 300 > self.level >= 200:
                self.level = self.level + 200
                print()
                print('LEVEL UP!!!')
                print('Through great effort and experience, our hero has unlocked a power hidden within himself.')
                print('You are now {} the Knower of Secrets of level {}.'.format(self.name, self.level))
            elif 800 > self.level >= 700:
                self.level = self.level + 300
                print()
                print('LEVEL UP')
                print("The hero's path is long and treacherous, and you have triumphed over many evils.")
                print("Chief among them, you have slain the beast of your own fear and trembling.")
                print("You have become {} the Fearless of level {}".format(self.name, self.level))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll/2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier