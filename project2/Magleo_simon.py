# MAGLEO, Simon Benedict A.
# 11 - A
# 2nd Quarter Project

bulbasaur_attr = {
        'name': 'Bulbasaur',
        'type': 'Grass',
        'hp': 45,
        'atk': 49,
        'sp_atk': 65,
        'defense': 49,
        'sp_defense': 65,
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
        'spd': 75
        }

ditto_attr = {
        'name': 'Ditto',
        'type': 'Normal',
        'hp': 48,
        'atk': 48,
        'sp_atk': 48,
        'defense': 48,
        'sp_defense': 48,
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
        'spd': 48
        }

snorlax_attr = {
        'name': 'Snorlax',
        'type': 'Normal',
        'hp': 160,
        'atk': 110,
        'sp_atk': 65,
        'defense': 65,
        'sp_defense': 110,
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
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
        'move': ['Tackle', 40],
        'sp_move': ['Solar Beam', 120],
        'spd': 110
        }

# pokedex and the count
dex_count = 0
pokedex = []

# current pokemon
current_pokemon = None

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

def binary_search(alist, param, bottom, top):
    if top >= bottom:
        middle = (top + bottom) // 2
        # recursive case
        if getattr(alist[middle], 'type').lower() < param.lower():
            # recursive definition
            return binary_search(alist, param, middle+1, top)
        # recursive case
        elif getattr(alist[middle], 'type').lower() > param.lower():
            # recursive definition
            return binary_search(alist, param, bottom, middle-1)
        # base case
        else:
            # base definition
            return True
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

def maze_path(maze):

    print(current_pokemon.name, ' entered the maze!\n')

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
            print(current_pokemon.name, ' found the item at the end of the maze!')
            return True

        path.push(loc)

    
        if (xloc - 1) >= 0 and maze[xloc-1][yloc] and visited[xloc-1][yloc] != 1:
            nxtloc = [xloc - 1, yloc]
            print(current_pokemon.name, ' went up')
            visited[xloc-1][yloc] = 1
            path.push(nxtloc)

        elif (yloc + 1) < len(maze[0]) and maze[xloc][yloc + 1] and visited[xloc][yloc + 1] != 1:
            nxtloc = [xloc, yloc + 1]
            print(current_pokemon.name, ' went right')
            visited[xloc][yloc + 1] =  1
            path.push(nxtloc)
                
        elif (xloc + 1) < len(maze) and maze[xloc+1][yloc] and visited[xloc+1][yloc] != 1:
            nxtloc = [xloc + 1, yloc]
            print(current_pokemon.name, ' went down')
            visited[xloc+1][yloc] = 1
            path.push(nxtloc)
        
        elif (yloc - 1) >= 0 and maze[xloc][yloc - 1] and visited[xloc][yloc - 1] != 1:
            nxtloc = [xloc, yloc - 1]
            print(current_pokemon.name, ' went left')
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
    global pokedex
    param = input("What type of pokemon are you looking for? ")
    param = param.title()
    print("")

    
    quick_sort(alist, 'type')
    found = binary_search(alist, param, 0, len(alist)-1)

    if found:
        results = [pokemon for pokemon in alist if pokemon.type == param]
        view_dex(results)
    else:
        print("\nSorry, we can't any pokemons of that type.")

bulbasaur = pokemon(bulbasaur_attr)
ivysaur = pokemon(ivysaur_attr)
venesaur = pokemon(venesaur_attr)

charizard = pokemon(charizard_attr)
charmeleon = pokemon(charmeleon_attr)
charizard = pokemon(charizard_attr)

squirtle = pokemon(squirtle_attr)
wartortle = pokemon(wartortle_attr)
blastoise = pokemon(blastoise_attr)

eevee = pokemon(eevee_attr)
ditto = pokemon(ditto_attr)
snorlax = pokemon(snorlax_attr)

pichu = pokemon(pichu_attr)
pikachu = pokemon(pikachu_attr)
raichu = pokemon(raichu_attr)

current_pokemon = raichu

maze_path(maze2)
