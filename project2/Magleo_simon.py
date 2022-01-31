# MAGLEO, Simon Benedict A.
# 11 - A
# 2nd Quarter Project
import sys
import random
import time

multipliers = {'super_effective': 2, 'effective': 1, 'not_effective': 0.5}
type_matchups = {
        'water': {
            'fire': multipliers['super_effective'],
            'grass': multipliers['not_effective'],
            'electric': multipliers['effective'],
            'normal': multipliers['effective'],
            'water': multipliers['not_effective']
            },
        'fire': {
            'fire': multipliers['not_effective'],
            'grass': multipliers['super_effective'],
            'electric': multipliers['effective'],
            'normal': multipliers['effective'],
            'water': multipliers['not_effective']
            },
        'grass': {
            'fire': multipliers['not_effective'],
            'grass': multipliers['not_effective'],
            'electric': multipliers['effective'],
            'normal': multipliers['effective'],
            'water': multipliers['super_effective']
            },
        'electric': {
            'fire': multipliers['effective'],
            'grass': multipliers['not_effective'],
            'electric': multipliers['not_effective'],
            'normal': multipliers['effective'],
            'water': multipliers['super_effective']
            },
        'normal': {
            'fire': multipliers['effective'],
            'grass': multipliers['effective'],
            'electric': multipliers['effective'],
            'normal': multipliers['effective'],
            'water': multipliers['effective']
            }
        }

bulbasaur_attr = {
        'name': 'Bulbasaur',
        'type': 'Grass',
        'hp': 45,
        'atk': 49,
        'sp_atk': 65,
        'defense': 49,
        'sp_defense': 65,
        'move': {'move_name': 'Tackle', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Razor Leaf', 'move_power': 55},
        'spd': 45
        }

ivysaur_attr = {
        'name': 'Ivysaur',
        'type': 'Grass',
        'hp': 60,
        'atk': 62,
        'sp_atk': 80,
        'defense': 63,
        'sp_defense': 80,
        'move': {'move_name': 'Tackle', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Magical Leaf', 'move_power': 60},
        'spd': 60
        }

venesaur_attr = {
        'name': 'Venesaur',
        'type': 'Grass',
        'hp': 80,
        'atk': 82,
        'sp_atk': 100,
        'defense': 83,
        'sp_defense': 100,
        'move': {'move_name': 'Takedown', 'move_power': 90, 'move_acc': 85},
        'sp_move': {'move_name': 'Solar Beam', 'move_power': 120},
        'spd': 80
        }

charmander_attr = {
        'name': 'Charmander',
        'type': 'Fire',
        'hp': 39,
        'atk': 52,
        'sp_atk': 60,
        'defense': 43,
        'sp_defense': 50,
        'move': {'move_name': 'Scratch', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Ember', 'move_power': 40},
        'spd': 65
        }

charmeleon_attr = {
        'name': 'Charmeleon',
        'type': 'Fire',
        'hp': 58,
        'atk': 64,
        'sp_atk': 80,
        'defense': 64,
        'sp_defense': 65,
        'move': {'move_name': 'Slash', 'move_power': 70, 'move_acc': 100},
        'sp_move': {'move_name': 'Fire Fang', 'move_power': 65},
        'spd': 80
        }

charizard_attr = {
        'name': 'Charizard',
        'type': 'Fire',
        'hp': 78,
        'atk': 84,
        'sp_atk': 109,
        'defense': 78,
        'sp_defense': 85,
        'move': {'move_name': 'Mega Punch', 'move_power': 80, 'move_acc': 85},
        'sp_move': {'move_name': 'Flamethrower', 'move_power': 90},
        'spd': 100
        }

squirtle_attr = {
        'name': 'Squirtle',
        'type': 'Water',
        'hp': 44,
        'atk': 48,
        'sp_atk': 50,
        'defense': 65,
        'sp_defense': 64,
        'move': {'move_name': 'Tackle', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Water Gun', 'move_power': 40},
        'spd': 43
        }

wartortle_attr = {
        'name': 'Wartortle',
        'type': 'Water',
        'hp': 59,
        'atk': 63,
        'sp_atk': 65,
        'defense': 80,
        'sp_defense': 80,
        'move': {'move_name': 'Rapid Spin', 'move_power': 50, 'move_acc': 100},
        'sp_move': {'move_name': 'Water Pulse', 'move_power': 60},
        'spd': 58
        }

blastoise_attr = {
        'name': 'Blastoise',
        'type': 'Water',
        'hp': 79,
        'atk': 83,
        'sp_atk': 85,
        'defense': 100,
        'sp_defense': 105,
        'move': {'move_name': 'Rapid Spin', 'move_power': 50, 'move_acc': 100},
        'sp_move': {'move_name': 'Hydro Pump', 'move_power': 110},
        'spd': 78
        }

eevee_attr = {
        'name': 'Eevee',
        'type': 'Normal',
        'hp': 55,
        'atk': 55,
        'sp_atk': 45,
        'defense': 50,
        'sp_defense': 65,
        'move': {'move_name': 'Covet', 'move_power': 60, 'move_acc': 100},
        'sp_move': {'move_name': 'Hyper Voice', 'move_power': 90},
        'spd': 75
        }

porygonz_attr = {
        'name': 'Ditto',
        'type': 'Normal',
        'hp': 85,
        'atk': 80,
        'sp_atk': 135,
        'defense': 75,
        'sp_defense': 75,
        'move': {'move_name': 'Facade', 'move_power': 70, 'move_acc': 100},
        'sp_move': {'move_name': 'Hyper Beam', 'move_power': 150},
        'spd': 90
        }

snorlax_attr = {
        'name': 'Snorlax',
        'type': 'Normal',
        'hp': 160,
        'atk': 110,
        'sp_atk': 65,
        'defense': 65,
        'sp_defense': 110,
        'move': {'move_name': 'Covet', 'move_power': 60, 'move_acc': 100},
        'sp_move': {'move_name': 'Last Resort', 'move_power': 140},
        'spd': 30
        }

pichu_attr = {
        'name': 'Pichu',
        'type': 'Electric',
        'hp': 20,
        'atk': 40,
        'sp_atk': 35,
        'defense': 15,
        'sp_defense': 35,
        'move': {'move_name': 'Quick Attack', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Thunder Shock', 'move_power': 40},
        'spd': 60
        }

pikachu_attr = {
        'name': 'Pikachu',
        'type': 'Electric',
        'hp': 35,
        'atk': 55,
        'sp_atk': 50,
        'defense': 30,
        'sp_defense': 40,
        'move': {'move_name': 'Quick Attack', 'move_power': 40, 'move_acc': 100},
        'sp_move': {'move_name': 'Thunderbolt', 'move_power': 90},
        'spd': 120
        }

raichu_attr = {
        'name': 'Raichu',
        'type': 'Electric',
        'hp': 60,
        'atk': 90,
        'sp_atk': 50,
        'defense': 55,
        'sp_defense': 80,
        'move': {'move_name': 'Slam', 'move_power': 80, 'move_acc': 75},
        'sp_move': {'move_name': 'Thunder', 'move_power': 110},
        'spd': 110
        }

# pokedex and the count
dex_count = 0
pokedex = []

def quick_sort(args, param):
    quicksort_helper(args, 0, len(args)-1, param)

def quicksort_helper(args, start, end, param):
    # recursive case
    if start < end:
        # recursive definition
        # use parition function to find the splitpoint
        splitpoint = partition(args, start, end, param)
        # sort the smaller arrays recursively
        quicksort_helper(args, start, splitpoint-1, param)
        quicksort_helper(args, splitpoint+1, end, param)
    # base case
    else:
        # base definition
        return
def partition(args, start, end, param):
    # designate first element as pivot value
    pivot = args[start]
    leftmark = start+1
    rightmark = end
    done = False
    
    while not done:
        # while loop to check for values less than pivot
        while rightmark >= leftmark and getattr(args[rightmark], param) >= getattr(pivot, param):
            rightmark-=1
        # while loop to check for values greater than pivot
        while leftmark <= rightmark and getattr(args[leftmark], param) <= getattr(pivot, param):
            leftmark+=1
        # if the rightmark is now less than the leftmark, we can end the loop
        if rightmark < leftmark:
            done = True
        # else, swap the values of the array at rightmark and leftmark
        else:
            temp = args[rightmark]
            args[rightmark] = args[leftmark]
            args[leftmark] = temp
    
    # swap the value of the first element with element at index rightmark
    temp = args[start]
    args[start] = args[rightmark]
    args[rightmark] = temp
    # return rightmark as splitpoint
    return rightmark

def binary_search(alist, param, element, bottom, top):
    if top >= bottom:
        middle = (top + bottom) // 2
        # recursive case
        if getattr(alist[middle], param) < element:
            # recursive definition
            return binary_search(alist, param, element, middle+1, top)
        # recursive case
        elif getattr(alist[middle], param) > element:
            # recursive definition
            return binary_search(alist, param, element, bottom, middle-1)
        # base case
        else:
            # base definition
            return middle
    # base case
    else:
        # base definition
        return False

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

def define_matrix(height, width):
    matrix = []
    for i in range(height):
        temp_list = []
        for i in range(width):
            temp_list.append(0)
        matrix.append(temp_list)
    matrix[0][0] = 1
    return matrix

maze = [[ 1, 0, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1 ],
        [ 0, 1, 0, 1, 1 ],
        [ 1, 1, 0, 1, 9 ]]

maze2 = [[ 1, 0, 1, 1, 0 ],
         [ 1, 1, 1, 0, 9 ],
         [ 0, 1, 0, 1, 1 ],
         [ 1, 1, 1, 1, 1 ]]

def maze_path(maze, curr_pokemon):

    print("\n{} entered the maze!\n".format(curr_pokemon.name))
    [print(i) for i in maze]
    print()

    x = 0
    y = 0

    path = Stack()

    start = [x, y]
    path.push(start)

    visited = define_matrix(len(maze), len(maze[0]))

    while path:
        
        loc = path.pop()
        print("Current Coordinates: ", loc)
        
        xloc = loc[0]
        yloc = loc[1]

        if maze[xloc][yloc] == 9:
            print("\n{} found the item at the end of the maze!".format(curr_pokemon.name))
            return True

        path.push(loc)

    
        if (xloc - 1) >= 0 and maze[xloc-1][yloc] and visited[xloc-1][yloc] != 1:
            nxtloc = [xloc - 1, yloc]
            print(curr_pokemon.name, 'went up')
            visited[xloc-1][yloc] = 1
            path.push(nxtloc)

        elif (yloc + 1) < len(maze[0]) and maze[xloc][yloc + 1] and visited[xloc][yloc + 1] != 1:
            nxtloc = [xloc, yloc + 1]
            print(curr_pokemon.name, 'went right')
            visited[xloc][yloc + 1] =  1
            path.push(nxtloc)
                
        elif (xloc + 1) < len(maze) and maze[xloc+1][yloc] and visited[xloc+1][yloc] != 1:
            nxtloc = [xloc + 1, yloc]
            print(curr_pokemon.name, 'went down')
            visited[xloc+1][yloc] = 1
            path.push(nxtloc)
        
        elif (yloc - 1) >= 0 and maze[xloc][yloc - 1] and visited[xloc][yloc - 1] != 1:
            nxtloc = [xloc, yloc - 1]
            print(curr_pokemon.name, 'went left')
            visited[xloc][yloc - 1] =  1
            path.push(nxtloc)    

        else:
            visited[xloc][yloc] = 1
            path.pop()

            if path.size() == 0:
                break
        
            print("Backtracking")

        print()

    return False

# class for pokemon
class pokemon():

    def __init__(self, attr):
        global dex_count
        global pokedex
        dex_count += 1
        setattr(self, 'index', dex_count)
        for key in attr:
            setattr(self, key, attr[key])
        setattr(self, 'max_hp', attr['hp'])
        pokedex.append(self)

    def view(self):
        print(
                ('%03d' % (self.index)).ljust(10),
                self.name.ljust(15),
                self.type.ljust(10),
                str(self.hp).rjust(10),
                str(self.atk).rjust(10),
                str(self.sp_atk).rjust(10),
                str(self.defense).rjust(10),
                str(self.sp_defense).rjust(10)
                )

    def attack(self, opponent):
        accuracy = random.randint(1,100)

        if accuracy <= self.move['move_acc']:
            damage = round(0.3 * (self.atk/opponent.defense) * self.move['move_power'], 0)

            if opponent.hp - damage >= 0:
                opponent.hp -= damage
            else:
                opponent.hp = 0

            return damage
        else:
            print("\n{} missed the attack!".format(self.name))
            return 0


    def special_attack(self, opponent):
        damage = round(type_matchups[self.type.lower()][opponent.type.lower()] * 0.3 * (self.sp_atk / opponent.sp_defense) * self.sp_move['move_power'], 0)

        if opponent.hp - damage >= 0:
            opponent.hp -= damage
        else:
            opponent.hp = 0

        return damage

    def full_restore(self):
        self.hp = self.max_hp

def view_dex(alist):
    print(
            "Index".ljust(10),
            "Pokemon".ljust(15),
            "Type".ljust(10),
            "HP".rjust(10),
            "ATK".rjust(10),
            "SP. ATK".rjust(10),
            "DEF".rjust(10),
            "SP. DEF".rjust(10),
            "\n"
            )
    for i in range(len(alist)):
        alist[i].view()
        if (i+1)%3 == 0:
            print("")

def search_dex(alist):
    param = input("What type of pokemon are you looking for? ")
    param = param.title()
    print("")

    
    quick_sort(alist, 'type')
    found = binary_search(alist, 'type', param, 0, len(alist)-1)

    if found:
        results = [pokemon for pokemon in alist if pokemon.type == param]
        view_dex(results)
    else:
        print("\nSorry, we can't any pokemons of that type.")

bulbasaur = pokemon(bulbasaur_attr)
ivysaur = pokemon(ivysaur_attr)
venesaur = pokemon(venesaur_attr)

charmander = pokemon(charmander_attr)
charmeleon = pokemon(charmeleon_attr)
charizard = pokemon(charizard_attr)

squirtle = pokemon(squirtle_attr)
wartortle = pokemon(wartortle_attr)
blastoise = pokemon(blastoise_attr)

eevee = pokemon(eevee_attr)
porygonz = pokemon(porygonz_attr)
snorlax = pokemon(snorlax_attr)

pichu = pokemon(pichu_attr)
pikachu = pokemon(pikachu_attr)
raichu = pokemon(raichu_attr)

def main():
    print("\nWelcome to Pseudo-mon!\nWhat would you like to do?")
    print("1: Open pokedex\n2: Pick Pokemon\n3: Exit Program")
    choice = int(input("Your choice: "))

    if choice == 1:
        open_dex()
    elif choice == 2:
        print("\nHere's a list of all the pokemon!\n")

        quick_sort(pokedex, "index")
        view_dex(pokedex)

        choice = int(input("Please input the index of your pokemon: "))

        curr_pokemon = pokedex[binary_search(pokedex, 'index', choice, 0, len(pokedex)-1)]
        print("You chose {}!".format(curr_pokemon.name))

        use_pokemon(curr_pokemon)
    elif choice == 3:
        print("\nThank you for playing!")
        sys.exit()

def open_dex():
        print("\nPseudo-dex Opened.\nWhat would you like to do?")
        print("1: View All Pokemon\n2: Sort Pokemon\n3: Search\n4: Go Back to Main")
        choice = int(input("Your choice: "))
        if choice == 1:
            view_dex(pokedex)
            open_dex()
        elif choice == 2:
            print("\nChoose your sort Criteria:")
            print("1: Pokemon Index")
            print("2: Pokemon Name")
            print("3: HP")
            print("4: ATK")
            print("5: SP. ATK")
            print("6: DEF")
            print("7: SP. DEF.")
            choice_table = ['index','name','hp','atk','sp_atk','defense','sp_defense']
            choice = int(input("Your choice: "))
            if choice > 0 and choice <= 7:
                quick_sort(pokedex, choice_table[choice-1])
                view_dex(pokedex)
        elif choice == 3:
            search_dex(pokedex)
            open_dex()
        elif choice == 4:
            main()

def use_pokemon(curr_pokemon):
    print("\nNow what would you like {} to do?".format(curr_pokemon.name))
    print("1: Battle Pokemon")
    print("2: Find Treasure in a Maze")
    print("3: Sleep")
    print("4: Go Back to Main")

    choice = int(input("Your choice: "))

    if choice == 1:
        opponent = pokedex[random.randint(0, len(pokedex)-1)]
        print("\n{}'s opponent is {}!".format(curr_pokemon.name, opponent.name))
        battle_pokemon(curr_pokemon, opponent)
    elif choice == 2:
        maze_path(maze2, curr_pokemon)
    elif choice == 3:
        print("\n{} went to sleep.".format(curr_pokemon.name))
        curr_pokemon.full_restore()
        print("{}'s health was restored to {}".format(curr_pokemon.name, curr_pokemon.max_hp))
        use_pokemon(curr_pokemon)
    elif choice == 4:
        main()

def battle_pokemon(curr_pokemon, opp):

    def player_attacks():
        print("\nMoves:")
        print("1: Use {}".format(curr_pokemon.move['move_name']))
        print("2: Use {}".format(curr_pokemon.sp_move['move_name']))
        print("3: Nap (Restores 20% hp)")

        choice = int(input("Pick your move: "))

        if choice == 1:
            print("\n{} used {} against {}".format(curr_pokemon.name, curr_pokemon.move['move_name'], opp.name))
            print("\n{} recieved {} damage".format(opp.name, curr_pokemon.attack(opp)))

        elif choice == 2:
            print("\n{} used {} against {}".format(curr_pokemon.name, curr_pokemon.sp_move['move_name'], opp.name))
            print("\n{} recieved {} damage".format(opp.name, curr_pokemon.special_attack(opp)))

        elif choice == 3:
            curr_pokemon.hp += curr_pokemon.max_hp * 0.20
            if curr_pokemon.hp > curr_pokemon.max_hp:
                curr_pokemon.hp = curr_pokemon.max_hp
            print("Health of {} was restorted by {} HP".format(curr_pokemon.name, curr_pokemon.max_hp * 0.20))

        print("\n{}: {}/{}".format(curr_pokemon.name, curr_pokemon.hp, curr_pokemon.max_hp))
        print("{}: {}/{}".format(opp.name, opp.hp, opp.max_hp))

    def opp_attacks():
        print("\n{} used {} against {}".format(opp.name, opp.move['move_name'], curr_pokemon.name))

        print("\n{} recieved {} damage".format(curr_pokemon.name, opp.attack(curr_pokemon)))

        print("\n{}: {}/{}".format(curr_pokemon.name, curr_pokemon.hp, curr_pokemon.max_hp))
        print("{}: {}/{}".format(opp.name, opp.hp, opp.max_hp))


    if curr_pokemon.spd >= opp.spd:
        while True:
            print("\n-----Your Turn-----")
            time.sleep(2.4)
            player_attacks()

            if opp.hp == 0:
                print("\n-----Winner-----")
                print("\n{} is the winner".format(curr_pokemon.name))
                break

            print("\n-----Opponent's Turn-----")
            time.sleep(2.4)
            opp_attacks()
            
            if curr_pokemon.hp == 0:
                print("\n-----Winner-----")
                print("\n{} is the winner".format(opp.name))
                break
    else:
        while True:
            print("\n-----Opponent's Turn-----")
            time.sleep(2.4)
            opp_attacks()

            if curr_pokemon.hp == 0:
                print("\n-----Winner-----")
                print("\n{} is the winner".format(opp.name))
                break

            print("\n-----Your Turn-----")
            time.sleep(2.4)
            player_attacks()

            if opp.hp == 0:
                print("\n-----Winner-----")
                print("\n{} is the winner".format(curr_pokemon.name))
                break

    use_pokemon(curr_pokemon)

main()
