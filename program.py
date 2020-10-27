import time
from actors import Wizard, Creature, SmallAnimal, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------------')
    print('         Wizard Battle')
    print('-----------------------------------')
    print()
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 2),
        Creature('Tiger', 13),
        SmallAnimal('Bat', 5),
        Creature('Minotaur', 50),
        Creature('Python', 20),
        Creature('Gargoyle', 35),
        Creature('Skeleton Warrior', 65),
        Creature('Dark Knight', 60),
        Dragon('Wyvern', 80, 0, False),
        Dragon('Fiery Dragon', 50, 25, True),
        Dragon('Hard Scaled Dragon', 65, 100, False),
        Wizard('Evil Wizard', 1000)
    ]
    evil_wizard = creatures[-1]
    hero_name = input("You have entered a land filled with danger, who dares step foreward? ")
    hero = Wizard(hero_name, 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'.format(active_creature.name,
                                                                                     active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                print()
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, exiting game... bye!')
            break

        if evil_wizard not in creatures:
            print()
            print()
            print("The Evil Wizard slumps to the floor. A final gasp escapes his darkened hood.")
            staff = input("The legendary Staff of Ages lies on the floor beside him, what should you do? [g]et or [d]estroy ")
            if staff == 'g':
                print("You claim the staff for your own, he certainly won't be using it anymore.")
                print("Staff in hand, it's power courses through you. What wonders you might achieve with such a gift!")
            elif staff == 'd':
                print("You conjur a mistic blue flame and destroy the Staff of Ages so it's power will never fall into the wrong hands again.")
            print()
            print("You have defeated creature after creature, and with the fall of the Evil Wizard, ")
            print("you have cut off the head of the great evil gripping this land!")
            print()
            print("Well done {}!!!".format(hero.name))
            print()
            print()
            break

        print()
        print()


if __name__ == '__main__':
    main()
