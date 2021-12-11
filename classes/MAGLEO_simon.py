import random
import time
import sys
# MAGLEO, Simon Benedict A.
# 11 - A 
# LG 2.1 Classes and Objects

class Pokemon:
    def __init__(self, name, hp, type, atk, sp_atk, defense, sp_defense, normal_move, special_move):
        self.name = name
        self.hp = hp
        self.type = type
        self.atk = atk
        self.sp_atk = sp_atk
        self.defense = defense
        self.sp_def = sp_defense
        self.normal_move = normal_move
        self.special_move = special_move
        self.max_hp = hp

    def normal_attack(self, enemy):
        accuracy = random.randint(0, 100) 
        if accuracy < 30:
            print("- Attack missed {}!".format(enemy.name))

        elif accuracy < 90:
            print("- Attack hit {}!".format(enemy.name))
            enemy.hp = enemy.hp - self.atk

        else:
            print("- Critical hit on {}!".format(enemy.name))
            enemy.hp = enemy.hp - (self.atk*2)

        # print("\n{} used {}!".format(self.name, self.normal_move))
        print("- HP of {}: {}/{}\n".format(enemy.name, enemy.hp, enemy.max_hp))

    def special_attack(self, enemy):
        if self.type == 'Fire':
            effect_table = {"Fire":0.5, "Water":0.5, "Normal":1.0, "Grass":2.0}
            enemy.hp = enemy.hp - (self.sp_atk * effect_table[enemy.type])

        elif self.type == 'Water':
            effect_table = {"Fire":2, "Water":0.5, "Normal":1.0, "Grass":0.5}
            enemy.hp = enemy.hp - (self.sp_atk * effect_table[enemy.type])

        elif self.type == 'Normal':
            effect_table = {"Fire":1.0, "Water":1.0, "Normal":1.0, "Grass":1.0}
            enemy.hp = enemy.hp - (self.sp_atk * effect_table[enemy.type])

        elif self.type == 'Grass':
            effect_table = {"Fire":0.5, "Water":2.0, "Normal":1.0, "Grass":0.5}
            enemy.hp = enemy.hp - (self.sp_atk * effect_table[enemy.type])

        # print("\n{} used {}!".format(self.name, self.special_move))
        print("- HP of {}: {}/{}\n".format(enemy.name, enemy.hp, enemy.max_hp))

    def full_restore(self):
        self.hp = self.max_hp
        print("\n{} - HP has been restored back to {}\n".format(self.name, self.hp))

class Player:
    def __init__(self, pokemon, special_pp):
        self.pokemon = pokemon
        self.special_pp = special_pp

Kyogre = Pokemon('Kyogre', 500, 'Water', 100, 150, 90, 140, 'Aqua Tail', 'Hydro Pump')
Reshiram = Pokemon('Reshiram', 500, 'Fire', 120, 150, 100, 120, 'Fire Fang', 'Blue Flare')
Torterra = Pokemon('Torterra', 450, 'Grass', 109, 75, 105, 85, 'Razor Leaf', 'Leaf Storm')
Porygon = Pokemon('Porygon-Z', 425, 'Normal', 80, 135, 70, 75, 'Tackle', 'Hyper Beam')
pokemon_list = [Kyogre, Reshiram, Torterra, Porygon]

red = Player(pokemon_list[0], 3)
blue = Player(pokemon_list[0], 3)

# sample gameplay
def random_match():
    opponent = pokemon_list[random.randint(0,2)]
    blue.pokemon = opponent
    print("\nYour opponent is {}!\n".format(opponent.name))

    while red.pokemon.hp > 0 and opponent.hp > 0:

        # Player's turn
        print("It's your turn. What do you want to do?")
        print("1. Normal Move")
        print("2. Special Move (PP: {})".format(red.special_pp))
        choice = int(input("What do you choose?: "))
        if choice == 1:
            time.sleep(2)
            print("- You used {}!".format(red.pokemon.normal_move))
            red.pokemon.normal_attack(opponent)
        if choice == 2:
            if red.special_pp > 0:
                time.sleep(2)
                print("- You used {}!".format(red.pokemon.special_move))
                red.pokemon.special_attack(opponent)
                red.special_pp-=1
            else:
                 print("- You don't have any PP left for this move!\n")
                 continue

        # Opponent's Turn
        print("Opponent's turn: ")
        time.sleep(1)
        opponent_choice = random.randint(1, 2)
        if opponent_choice == 1:
            time.sleep(1)
            print("- Blue used {}!".format(blue.pokemon.normal_move))
            opponent.normal_attack(red.pokemon)
        else:
            if blue.special_pp > 0:
                time.sleep(1)
                print("- Blue used {}!".format(blue.pokemon.special_move))
                opponent.special_attack(red.pokemon)
                blue.special_pp-=1
            else:
                time.sleep(1)
                print("- Blue used {}!".format(blue.pokemon.normal_move))
                opponent.normal_attack(red.pokemon)
    if blue.pokemon.hp <= 0:
        print("\nYou Won! You move on to the next round...")
        random_match()
    else:
        print("\nYou Lost...\n")
        matchmaking()

def prologue():
    print("Welcome to Pokemon: Hot Trash! To begin, choose what pokemon you would like to start with!")
    print("1. {}\n2. {}\n3. {}\n4. {}".format(Kyogre.name, Reshiram.name, Torterra.name, Porygon.name))
    try:
        choice = int(input("Who do you choose?: "))
        if choice > 4 or choice < 1:
            print("\nChoose something from 1-4.\n")
            prologue()
        else:
            red.pokemon = pokemon_list.pop(choice-1)
            print("\nYou've chosen {}!".format(red.pokemon.name))
    except:
        print("\nWrong Input, Try Again.\n")
        prologue()

    print("Congratulations! You now have your first pokemon.")

def matchmaking():
    print("\nYou now have to test your pokemon! What do you want to do?")
    print("1. Survival Mode\n2. Heal Pokemon (Health is currently at {}/{})\n3. Exit".format(red.pokemon.hp, red.pokemon.max_hp))
    try:
        choice = int(input("What do you choose?: "))
        if choice == 1:
            random_match()
        elif choice == 2:
            red.pokemon.full_restore()
            matchmaking()
        elif choice == 3:
            sys.exit()
        else:
            print("\nChoose a valid option.")
            matchmaking()
    except ValueError:
        print("\nChoose a valid option.")
        matchmaking()

prologue()
matchmaking()
