import random
import time
import sys
# MAGLEO, Simon Benedict A.
# 11 - A 
# LG 2.1 Classes and Objects

# Exercise Section 1 - Class for pokemons
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

    # method for normal attacks
    def normal_attack(self, enemy):
        accuracy = random.randint(0, 100) 
        damage = (((((2*50)/5)+2)*65*(self.atk/enemy.defense))/50)+2
        effect_table = {}
        if self.type == 'Fire':
            effect_table = {"Fire":0., "Water":0.75, "Normal":1.0, "Grass":1.25}

        elif self.type == 'Water':
            effect_table = {"Fire":1.25, "Water":0.75, "Normal":1.0, "Grass":0.75}

        elif self.type == 'Normal':
            effect_table = {"Fire":1.0, "Water":1.0, "Normal":1.0, "Grass":1.0}

        elif self.type == 'Grass':
            effect_table = {"Fire":0.75, "Water":1.25, "Normal":1.0, "Grass":0.75}

        if accuracy < 30:
            print("- Attack missed {}!".format(enemy.name))

        elif accuracy < 90:
            print("- Attack hit {} for {} dmg points!".format(enemy.name, damage * effect_table[enemy.type]))
            enemy.hp = max(0,round(enemy.hp - (damage * effect_table[enemy.type])))
            if effect_table[enemy.type] == 1.25:
                print("- It's super effective")
            elif effect_table[enemy.type] == 1:
                print("- It's effective")
            else:
                print("- It's not very effective")

        else:
            print("- Attack hit {} for {} dmg points!".format(enemy.name, damage * effect_table[enemy.type]))
            print("- Critical hit on {}!".format(enemy.name))
            enemy.hp = max(0,round(enemy.hp - (damage * effect_table[enemy.type] * 1.25)))
            if effect_table[enemy.type] == 1.25:
                print("- It's super effective")
            elif effect_table[enemy.type] == 1:
                print("- It's effective")
            else:
                print("- It's not very effective")

        print("- HP of {}: {}/{}\n".format(enemy.name, enemy.hp, enemy.max_hp))

    # method for special attacks
    def special_attack(self, enemy):
        damage = (((((2*50)/5)+2)*100*(self.sp_atk/enemy.sp_def))/50)+2
        effect_table = {}
        if self.type == 'Fire':
            effect_table = {"Fire":0.75, "Water":0.75, "Normal":1.0, "Grass":1.25}

        elif self.type == 'Water':
            effect_table = {"Fire":1.25, "Water":0.75, "Normal":1.0, "Grass":0.75}

        elif self.type == 'Normal':
            effect_table = {"Fire":1.0, "Water":1.0, "Normal":1.0, "Grass":1.0}

        elif self.type == 'Grass':
            effect_table = {"Fire":0.75, "Water":1.25, "Normal":1.0, "Grass":0.75}

        if effect_table[enemy.type] == 1.25:
            print("- It's super effective")
        elif effect_table[enemy.type] == 1:
            print("- It's effective")
        else:
            print("- It's not very effective")

        print("- Attack hit {} for {} dmg points!".format(enemy.name, damage * effect_table[enemy.type]))
        enemy.hp = max(0,round(enemy.hp - (damage * effect_table[enemy.type])))
        print("- HP of {}: {}/{}\n".format(enemy.name, enemy.hp, enemy.max_hp))

    # method for resorting health
    def full_restore(self):
        self.hp = self.max_hp
        print("\n{} - HP has been restored back to {}\n".format(self.name, self.hp))

# Exercise Section 2 - Classes for players (made to store power points for the special move)
class Player:
    def __init__(self, pokemon, special_pp):
        self.pokemon = pokemon
        self.special_pp = special_pp

# Kinds of pokemons
Kyogre = Pokemon('Kyogre', 200, 'Water', 94, 139, 110, 125, 'Aqua Tail', 'Hydro Pump')
Reshiram = Pokemon('Reshiram', 200, 'Fire', 121, 139, 121, 121, 'Fire Fang', 'Blue Flare')
Virizion = Pokemon('Virizion', 220, 'Grass', 156, 189, 110, 120, 'Razor Leaf', 'Leaf Storm')
Regigigas = Pokemon('Regigigas', 300, 'Normal', 148, 76, 103, 103, 'Tackle', 'Hyper Beam')
pokemon_list = [Kyogre, Reshiram, Virizion, Regigigas]

red = Player(pokemon_list[0], 5)
blue = Player(pokemon_list[0], 5)

# Gameplay interface

## function for survial mode (fight as much pokemons as you can before dying)
def random_match():
    opponent = pokemon_list.pop(random.randint(0,len(pokemon_list)-1))
    blue.pokemon = opponent
    print("\nYour opponent is {}!\n".format(opponent.name))

    while True:
        # Player's turn
        print("It's your turn. What do you want to do?")
        print("1. Normal Move")
        print("2. Special Move (PP: {})".format(red.special_pp))
        try:
            choice = int(input("What do you choose?: "))
        except ValueError:
            print("\nChoose a valid option.\n")
            continue
        if choice == 1:
            time.sleep(2)
            print("- You used {}!".format(red.pokemon.normal_move))
            red.pokemon.normal_attack(opponent)
        elif choice == 2:
            if red.special_pp > 0:
                time.sleep(2)
                print("- You used {}!".format(red.pokemon.special_move))
                red.pokemon.special_attack(opponent)
                red.special_pp-=1
            else:
                 print("- You don't have any PP left for this move!\n")
                 continue
        else:
            print("\nChoose a valid option.\n")
            continue

        # check if opponent's hp is 0
        if opponent.hp <= 0:
            break
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

        if red.pokemon.hp <= 0:
            break

    if red.pokemon.hp <= 0:
        print("\nYou Lost...\n")
        prologue()
    elif blue.pokemon.hp <= 0:
        print("\nYou Won! You move on to the next round...")
        random_match()

# Choosing pokemon
def prologue():
    print("Welcome to Pokemon: Hot Trash! To begin, choose what pokemon you would like to start with!")
    print("1. {}\n2. {}\n3. {}\n4. {}".format(Kyogre.name, Reshiram.name, Virizion.name, Regigigas.name))
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

# Start survival mode, restore the health of your pokemon, or quit the game
def matchmaking():
    global Kyogre, Reshiram, Virizion, Regigigas, red, blue
    Kyogre = Pokemon('Kyogre', 200, 'Water', 94, 139, 110, 125, 'Aqua Tail', 'Hydro Pump')
    Reshiram = Pokemon('Reshiram', 171, 'Fire', 121, 139, 121, 121, 'Fire Fang', 'Blue Flare')
    Virizion = Pokemon('Virizion', 220, 'Grass', 156, 189, 110, 120, 'Razor Leaf', 'Leaf Storm')
    Regigigas = Pokemon('Regigigas', 300, 'Normal', 148, 76, 103, 103, 'Tackle', 'Hyper Beam')
    red = Player(red.pokemon, 5)
    blue = Player(blue.pokemon, 5)

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
