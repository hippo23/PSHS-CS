#CS5 2nd Quarter Project
#Rosete; Magleo
#Grade 11


import random
class Pokemon:

    def __init__(self, hindex, hpokemon, htype, hhp, hattack, hspattack, hdeff, hspdeff, hmove, hspmove, hspeed, hnmove, hnsmove):
        self.index = hindex
        self.name = hpokemon
        self.type = htype
        self.hp = hhp
        self.attack = hattack
        self.spattack = hspattack
        self.deff = hdeff
        self.spdeff = hspdeff
        self.move = hmove
        self.spmove = hspmove
        self.speed = hspeed
        self.nmove = hnmove
        self.nsmove = hnsmove
    def view(self):
        print(str(self.index).ljust(10), self.name.ljust(20), self.type.ljust(10), str(self.hp).ljust(5), str(self.attack).ljust(4), str(self.spattack).ljust(6), str(self.deff).ljust(6), str(self.spdeff).ljust(4))
    def __lt__(self,other):
            if param == 'index':
                return self.index < other.index
            if param == 'name':
                return self.name < other.name
            if param == 'HP':
                return self.hp < other.hp
            if param == 'ATK':
                return self.attack < other.attack
            if param == 'SP. ATK':
                return self.spattack < other.spattack
            if param == 'DEF':
                return self.deff < other.deff
            if param == 'SP. DEF':
                return self.spdeff < other.spdeff
            if param == 'type':
                return self.type < other.type
    def __eq__(self,other):
        return self.name == other.name
    def __gt__(self,other):
         return self.index > other.index
    def attack(self, other):
                a = random.randint(1,3)
                global damage
                global z
                if a == 1:
                    damage = 0*(0.3*(self.attack/other.deff)*self.move)
                    damage = round(damage)
                    asd = other.hp - damage
                    if asd<0:
                        asd = asd - asd
                    print('\n', self.name, 'attack missed!\n')
                    print(self.name, ':', self.hp, '/', mbb)
                    print(other.name, ':', asd, '/', bmm)
                elif a == 2:
                    damage = 0.3*(self.attack/other.deff)*self.move
                    damage = round(damage)
                    asd = other.hp - damage
                    if asd<0:
                        asd = asd - asd
                    print('\n', other.name, 'received', damage, 'damage\n')
                    print(self.name, ':', self.hp, '/', mbb)
                    print(other.name, ':', asd, '/', bmm)
                elif a == 3:
                    damage = 2*(0.3*(self.attack/other.deff)*self.move)
                    damage = round(damage)
                    asd = other.hp - damage
                    if asd<0:
                        asd = asd - asd
                    print('\nCritical Hit!')
                    print(other.name, 'received', damage, 'damage\n')
                    print(self.name, ':', self.hp, '/', mbb)
                    print(other.name, ':', asd, '/', bmm)
                other.hp = other.hp - damage
                if other.hp <= 0:
                    if namee == other.name:
                        print(other.name, 'fainted')
                        print(self.name, 'won the battle!', 'You lose!\n')
                        other.hp = other.hp + bmm
                        main()
                    else:
                        print(other.name, 'fainted')
                        print(self.name, 'won the battle!', other.name, 'went off to rest\n')
                        z = 1
                    
                return other.hp
    def spattack(self, other):
        global damage
        global z 
        a = 0
        if self.type == 'Grass':
            if other.type == 'Water':
                a = 2
            elif other.type == 'Fire' or other.type == 'Grass':
                a = 0.5
            else:
                a = 1
        elif self.type == 'Water':
            if other.type == 'Fire':
                a = 2
            elif other.type == 'Water' or other.type == 'Grass':
                a = 0.5
            else:
                a = 1
        elif self.type == 'Fire':
            if other.type == 'Grass':
                a = 2
            elif other.type == 'Fire' or other.type == 'Water':
                a = 0.5
            else:
                a = 1
        elif self.type == 'Electric':
            if other.type == 'Water':
                a = 2
            elif other.type == 'Electric' or other.type == 'Grass':
                a = 0.5
            else:
                a = 1
        elif self.type == 'Normal':
            a = 1

        aa = random.randint(1,3)
        if aa == 1:
            damage = a*(0*(0.3*(self.attack/other.deff)*self.spmove))
            damage = round(damage)
            asd = other.hp - damage
            if asd<0:
                asd = asd - asd
            print('\n', self.name, 'attack missed!\n')
            print(self.name, ':', self.hp, '/', mbb)
            print(other.name, ':', asd, '/', bmm)
        elif aa == 2:
            damage = a*(0.3*(self.attack/other.deff)*self.spmove)
            damage = round(damage)
            asd = other.hp - damage
            if asd<0:
                asd = asd - asd
            print('\n', other.name, 'received', damage, 'damage\n')
            print(self.name, ':', self.hp, '/', mbb)
            print(other.name, ':', asd, '/', bmm)
            
        elif aa == 3:
            damage = a*(2*(0.3*(self.attack/other.deff)*self.spmove))
            damage = round(damage)
            asd = other.hp - damage
            if asd<0:
                asd = asd - asd
            print('\nCritical Hit!')
            print(other.name, 'received', damage, 'damage\n')
            print(self.name, ':', self.hp, '/', mbb)
            print(other.name, ':', asd, '/', bmm)
        other.hp = other.hp - damage

        if other.hp <= 0:
            if namee == other.name:
                print(other.name, 'fainted')
                print(self.name, 'won the battle!', 'You lose!\n')
                main()
            else:
                print(other.name, 'fainted')
                print(self.name, 'won the battle!', other.name, 'went off to rest\n')
                z = 1
        return other.hp
        
    def choosee(a, self):
            if a == self.index:
                print('You chose:', self.name)
                return self.name
            else:
                return 10
    def eqq(a, self):
            return a == self.name
    def namegetter(self):
        return self.name
    def speedgetter(self, other):
        return self.speed > other.speed
    def hpgetter(self):
        return self.hp
    def nmove(self):
        return self.nmove
    def nmovee(self):
        return self.nsmove
    def heal(self):
        self.hp = self.hp + mb
        print(self.name, 'healed to', mb)
    def healll(self):
        helt = bmmm - self.hp
        self.hp = helt + self.hp
        print(self.name, 'healed to', self.hp)
        choosed(asss, aaa)
    def heall(self):
        a = (0.2)*(self.hp)
        a = round(a)
        self.hp = self.hp + a
        print('\n', self.name, 'took a nap!')
        if self.hp > bm:
            a = self.hp - bm
            self.hp = self.hp - a
        print(self.name, 'health was restored to', self.hp)
    def mazee(self, maze):
        maze_path(self.name, maze)

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
        
Bulbasaur = Pokemon('001', 'Bulbasaur', 'Grass', 45, 49, 65, 49, 65, 40, 45, 45, 'Tackle', 'Vine Whip')
Ivysaur = Pokemon('002', 'Ivysaur', 'Grass', 60, 62, 80, 63, 80, 40, 55, 60, 'Tackle', 'Razor Leaf')
Venusaur = Pokemon('003', 'Venusaur', 'Grass', 80, 82, 100, 83, 100, 40, 90, 80, 'Tackle', 'Petal Blizzard')

Squirtle = Pokemon('007', 'Squirtle', 'Water', 44, 48, 50, 65, 64, 40, 40, 43, 'Tackle', 'Water Gun')
Wartoise = Pokemon('008', 'Wartoise', 'Water', 59, 63, 65, 80, 80, 40, 90, 58, 'Tackle', 'Aqua Tail')
Blastoise = Pokemon('009', 'Blastoise', 'Water', 79, 83, 85, 100, 105, 40, 100, 78, 'Tackle', 'Hydro Pump')

Charmander = Pokemon('004', 'Charmander', 'Fire', 39, 52, 60, 43, 50, 40, 40, 65, 'Scratch', 'Ember')
Charmeleon = Pokemon('005', 'Charmeleon', 'Fire', 58, 64, 80, 58, 65, 40, 65, 80, 'Scratch', 'Fire Fang')
Charizard = Pokemon('006', 'Charizard', 'Fire', 78, 84, 109, 78, 85, 40, 95, 100, 'Scratch', 'Heat Wave')

Pikachu = Pokemon('025', 'Pikachu', 'Electric', 35, 55, 50, 40, 50, 40, 90, 90, 'Quick Attack', 'Thunderbolt')
Magnemite = Pokemon('081', 'Magnemite', 'Electric', 25, 35, 95, 70, 55, 40, 65, 45, 'Tackle', 'Spark')
Ampharos = Pokemon('181', 'Ampharos', 'Electric', 90, 75, 115, 85, 90, 40, 120, 55, 'Tackle', 'Zap Cannon')

Snorlax = Pokemon('143', 'Snorlax', 'Normal', 160, 110, 65, 65, 110, 40, 80, 30, 'Tackle', 'Crunch')
Lickylicky = Pokemon('463', 'Lickylicky', 'Normal', 110, 85, 80, 95, 95, 65, 30, 50, 'Stomp', 'Lick')
Jigglypuff = Pokemon('039', 'Jigglypuff', 'Normal', 115, 45, 45, 20, 25, 40, 90, 20, 'Pound', 'Play Rough')

pokemon = [Bulbasaur, Ivysaur, Venusaur, Squirtle, Wartoise, Blastoise, Charmander, Charmeleon, Charizard, Pikachu, Magnemite, Ampharos, Snorlax, Lickylicky, Jigglypuff]

maze = [[ 1, 0, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1 ],
        [ 0, 1, 0, 1, 1 ],
        [ 1, 1, 0, 1, 9 ]]

maze2 = [[ 1, 0, 1, 1, 0 ],
         [ 1, 1, 1, 0, 9 ],
         [ 0, 1, 0, 1, 1 ],
         [ 1, 1, 1, 1, 1 ]]

maze3 = [[ 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 9, 0, 0, 1 ],
        [ 0, 1, 0, 1, 1, 0, 1 ],
        [ 0, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 0, 0, 0, 0, 1 ],
        [ 0, 1, 1, 1, 1, 1, 1 ],]

def view_inv(alist):

    hindex = "Index"
    hpokemon = "Pokemon"
    htype = "Type"
    hhp = "HP"
    hattack = "ATK"
    hspattack = "SP. ATK"
    hdeff = "DEF"
    hspdeff = "SP. DEF"

    print("\n", hindex.ljust(10), hpokemon.ljust(20), htype.ljust(10), hhp.ljust(4), hattack.ljust(2), hspattack.ljust(8), hdeff.ljust(4), hspdeff.ljust(4), "\n")
    for i in range(len(alist)):
        alist[i].view()
        if i%3 == 2:
            print("")
            
import sys
def main():
    print("Welcome to Pseudo-mon!")
    print("What would you like to do?")
    print("1: Open Pokedex")
    print("2: Pick Pokemon")
    print("3: Exit Program")
    
    choice = input("Your Choice: ")
    print('')
        
    if choice == '1':
        ichoice()
    elif choice =='2':
        iichoice(pokemon)
    elif choice == '3':
        print("Thank you for using the program!")
        sys.exit()
    else:
        print("Invalid input. Try Again\n")

def ichoice():
    print("Pseudo-dex Opened.")
    print("What would you like to do?")
    print("1: View All Pokemon")
    print("2: Sort Pokemon")
    print("3: Search")
    print("4: Go Back to Main")

    choice = input("Your Choice: ")
    print("")
        
    if choice == '1':
        view_inv(pokemon)
    elif choice =='2':
        sorting(pokemon)
    elif choice =='3':
        searching(pokemon)
    elif choice =='4':
        main()
    ichoice()

def iichoice(pokemon):
    global aaa
    global asss
    aaa = 0
    print("\nHere's a list of all the pokemon:")
    view_inv(pokemon)
    choice = input("\nPlease input the index of your pokemon choice: ")
    for i in range(len(pokemon)):
        aa = pokemon[i]
        asss = Pokemon.choosee(choice, aa)
        if Pokemon.eqq(asss,aa):
            break
        aaa = aaa + 1
    if asss == 10:
        print("\nThere's no pokemon available with that index, please try again.")
        iichoice(pokemon)
    else:
        global bmmm
        bmmm = Pokemon.hpgetter(pokemon[aaa])
        choosed(asss,aaa)
          
def choosed(a,aaa):
    global bm
    bm = Pokemon.hpgetter(pokemon[aaa])
    print('\nWhat would you like', a, 'do?')
    print('1: Battle Pokemon')
    print('2: Find Treasure in a Maze')
    print('3: Sleep')
    print('4: Go Back to Main')
    choice = input("\nYour Choice:")
        
    if choice == '1':
        numbers = list(range(0,14))
        numbers.remove(aaa)
        aaaaa = random.choice(numbers)
        aaaa = Pokemon.namegetter(pokemon[aaaaa])
        print(a,"'s opponent is ", aaaa, '!')
        fightt(pokemon[aaa], pokemon[aaaaa])
    elif choice =='2':
        d = random.randint(1,3)
        if d == 1:
            mazed = maze
        elif d == 2:
            mazed = maze2
        elif d == 3:
            mazed = maze3
        Pokemon.mazee(pokemon[aaa], mazed)
    elif choice =='3':
        Pokemon.healll(pokemon[aaa])
    elif choice =='4':
        main()
        
def fightt(a, b):
    global namee
    global nameee
    global bmm
    global mbb
    global bm
    global mb
    namee = Pokemon.namegetter(a)
    nameee = Pokemon.namegetter(a)
    bm = Pokemon.hpgetter(a)
    mb = Pokemon.hpgetter(b)
    turns = 1
    if Pokemon.speedgetter(a,b):
        bmm = mb
        mbb = bmmm
        print(Pokemon.namegetter(a), 'gets to move first\n')
        print('Moves:')
        print('1:', Pokemon.nmove(a))
        print('2:', Pokemon.nmovee(a))
        print('3: Nap (Restores 20% hp)')
        choice = input('Choice: ')
        if choice == '1':
            print(Pokemon.namegetter(a), 'used', Pokemon.nmove(a))
            q = Pokemon.attack(a,b)
        elif choice == '2':
            print(Pokemon.namegetter(a), 'used', Pokemon.nmovee(a))
            q = Pokemon.spattack(a,b)
        elif choice == '3':
                Pokemon.heall(a)
        turns = 1
    else:
        bmm = bmmm
        mbb = mb
        print(Pokemon.namegetter(b), 'gets to move first')
        ab = random.randint(1,2)
        if ab == 1:
            print('Enemy ', Pokemon.namegetter(b), 'used', Pokemon.nmove(b))
            q = Pokemon.attack(b,a)
        elif ab == 2:
            print('Enemy ', Pokemon.namegetter(b), 'used', Pokemon.nmovee(b))
            q = Pokemon.spattack(b,a)
        turns = 2
    while q > 0:
        turnss = turns%2
        if turnss == 0:
            bmm = mb
            mbb = bmmm
            print('\nMoves:')
            print('1:', Pokemon.nmove(a))
            print('2:', Pokemon.nmovee(a))
            print('3: Nap (Restores 20% hp)')
            choice = input('Choice: ')
            if choice == '1':
                print(Pokemon.namegetter(a), 'used', Pokemon.nmove(a))
                q = Pokemon.attack(a,b)
                turns = turns + 1
            elif choice == '2':
                print(Pokemon.namegetter(a), 'used', Pokemon.nmovee(a))
                q = Pokemon.spattack(a,b)
                turns = turns + 1
            elif choice == '3':
                Pokemon.heall(a)
                turns = turns + 1
        else:
            bmm = bmmm
            mbb = mb
            ab = random.randint(1,3)
            if ab == 1:
                print('Enemy ', Pokemon.namegetter(b), 'used', Pokemon.nmove(b))
                q = Pokemon.attack(b,a)
                turns = turns + 1
            elif ab == 2:
                print('Enemy ', Pokemon.namegetter(b), 'used', Pokemon.nmovee(b))
                q = Pokemon.spattack(b,a)
                turns = turns + 1
            elif ab == '3':
                Pokemon.heall(b)
                turns = turns + 1
    if z == 1:
        Pokemon.heal(b)
        print('')
        choosed(asss, aaa)

#Part 2: bubble sort(n^2), selection sort(n^2), insertion sort(n^2), fastest: merge sort(n*log(n)), quick sort(n^2)
def sorting(alist):
    print("\nPlease choose sorting criteria")
    print("1: Pokemon Index")
    print("2: Pokemon Name")
    print("3: HP")
    print("4: ATK")
    print("5: SP. ATK")
    print("6: DEF")
    print("7: SP. DEF")
    choice = input("Your Choice: ")
    global param
    param = ''

    if choice == '1':
        param = 'index'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='2':
        param = 'name'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='3':
        param = 'HP'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='4':
        param = 'ATK'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='5':
        param = 'SP. ATK'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='6':
        param = 'DEF'
        sorrtt(alist)
        view_inv(alist)
    elif choice =='7':
        param = 'SP. DEF'
        sorrtt(alist)
        view_inv(alist)
    else:
        print("Invalid input. Try Again")
        sorting(alist)

def sorrtt(listt):
        if len(listt)>1: 
            mid = len(listt)//2
            #split: log2(n)
            lefthalf = listt[:mid]
            righthalf = listt[mid:] 
            sorrtt(lefthalf) 
            sorrtt(righthalf) 

            i=0 
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf): #n steps 
                    if lefthalf[i].__lt__(righthalf[j]) or lefthalf[i].__eq__(righthalf[j]): 
                        listt[k] = lefthalf[i]
                        i=i+1
                    else:
                        listt[k] = righthalf[j]
                        j=j+1
                    k=k+1
            while i < len(lefthalf):
                listt[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                listt[k]=righthalf[j]
                j=j+1
                k=k+1
                
def searching(alist):
    global param
    paramm = input("\nWhat type of pokemon are you looking for? ")
    paramm = paramm.title()
    param = 'type'
    sorrtt(alist)
    if binary(paramm, alist):
        print("\nHere are the results of your search")
        if paramm in {"Grass", "Fire", 'Water', 'Electric', 'Normal'}:
            results = [obj for obj in alist if obj.type == paramm]
            results = bubble(results)
        view_inv(results)
    else:
        print("\nSorry, we don't have the type of pokemon that you are looking for.")
        main()

def binary(word, sett):
    first = 0
    last = len(sett) - 1
    asd = False
    global paramm
    while first<=last and not asd: 
        mid = (first + last)//2
        if sett[mid].type == word:
            return True
            asd = True
        else:
            if sett[mid].type > word:
                last = mid - 1
            else:
                first = mid + 1

def bubble(collection):
    my_list = list(collection)
    for endnum in range(len(my_list)-1, 0, -1):
        for i in range(endnum):
            if my_list[i].__gt__(my_list[i+1]):
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return my_list


visited = [[ 1, 0, 0, 0, 0 ],
           [ 0, 0, 0, 0, 0 ],
           [ 0, 0, 0, 0, 0 ],
           [ 0, 0, 0, 0, 0 ]]

def reset():
    visited[:] = [[ 1, 0, 0, 0, 0 ],
                 [ 0, 0, 0, 0, 0 ],
                 [ 0, 0, 0, 0, 0 ],
                 [ 0, 0, 0, 0, 0 ]]

def maze_path(name, maze):
    print('\nYou found a map of a maze. The maze looks like this:\n')
    for i in range(len(maze)):
            print(maze[i])
            i += 1     
    a = i - 4
    while a != 0:
        visited.append([ 0, 0, 0, 0, 0 ])
        a = a - 1
    for i in range(len(maze[1])):
        i += 1
    aa = i - 5
    while aa != 0:
        for i in range(len(visited)):
            visited[i].append(0)
            i += 1
        aa = aa - 1

    print('\n', name, 'entered the maze!\n')
        
    x = 0
    y = 0

    path = Stack()

    start = [x, y]
    path.push(start)

    while path:
        
        loc = path.pop()
        
        xloc = loc[0]
        yloc = loc[1]

        if maze[xloc][yloc] == 9:
                print('\nCurrent Location:', loc)
                print (name, 'found the item at the end of the maze!')
                reset()
                choosed(asss, aaa)
                break
        
        path.push(loc)
    
        if (xloc - 1) >= 0 and maze[xloc-1][yloc] and visited[xloc-1][yloc] != 1:
            nxtloc = [xloc - 1, yloc] #Move up
            print('\nCurrent Location:', loc)
            print(name, 'went up')
            visited[xloc-1][yloc] = 1 #Mark tile as visited
            path.push(nxtloc) #Add coordinates to path stack

        elif (yloc + 1) < len(maze[0]) and maze[xloc][yloc + 1] and visited[xloc][yloc + 1] != 1:
            nxtloc = [xloc, yloc + 1]
            print('\nCurrent Location:', loc)
            print(name, 'went right')
            visited[xloc][yloc + 1] =  1
            path.push(nxtloc)
                
        elif (xloc + 1) < len(maze) and maze[xloc+1][yloc] and visited[xloc+1][yloc] != 1:
            nxtloc = [xloc + 1, yloc]
            print('\nCurrent Location:', loc)
            print(name, 'went down')
            visited[xloc+1][yloc] = 1
            path.push(nxtloc)
        
        elif (yloc - 1) >= 0 and maze[xloc][yloc - 1] and visited[xloc][yloc - 1] != 1:
            nxtloc = [xloc, yloc - 1]
            print('\nCurrent Location:', loc)
            print(name, 'went left')
            visited[xloc][yloc - 1] =  1
            path.push(nxtloc)    

        else:
            visited[xloc][yloc] = 1
            s = path.pop() #pop last location to backtrack
            print('\nCurrent Location:', s)
            print(name, 'went back to his previous position')
            if path.size() == 0:
                break

    print(name, 'Failed to find the treasure')
    reset()   

main()
