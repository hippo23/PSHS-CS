# CS5 2nd Quarter Long Exam 1
# Magleo, Simon
# 11 - A

#Part1 : Classes and Objects: Create the class 'Product'. 

class Product():
    # defining class attributes
    def __init__(self, name, type, price):
        self.name = name 
        self.type = type
        self.price = price
        self.qty = 10

    def view(self):
        # if the quantity is greater than zero, there is stock
        if self.qty > 0:
            print(self.name.ljust(35), self.type.ljust(28), str(self.price).ljust(8), "In Stock")  
        # if not, then display that there is no stock
        else:
            print(self.name.ljust(35), self.type.ljust(28), str(self.price).ljust(8), "Not In Stock")  

    def buy(self, requested):
        if (requested > self.qty):
            requested = self.qty
        print("Qty. purchased: {}".format(requested))
        print("Price: {}".format(requested * self.price))
    def restock(self, amount):
        self.qty = amount;

#Instances of your Class: 
item_001 = Product('Tyma TD-10E Dreadnought', 'Acoustic Guitar', 23450)
item_002 = Product('Baton Rouge AR21C/ME Traveler', 'Acoustic Guitar', 14900)
item_003 = Product('Phoebus Baby 30 GS Mini', 'Acoustic Guitar', 6900)
item_004 = Product('Maestro Project X X1-V1 OM', 'Acoustic Guitar', 32500)
item_005 = Product('Sire A4 Grand Auditorium', 'Acoustic Guitar', 27490)

item_006 = Product('Tagima TW55', 'Electric Guitar', 9500)
item_007 = Product('Epiphone G400 ', 'Electric Guitar', 19500)
item_008 = Product('D’Angelico Premiere DC', 'Electric Guitar', 49000)
item_009 = Product('PRS Silver Sky', 'Electric Guitar', 138950)
item_010 = Product('Vintage V100 Reissued', 'Electric Guitar', 27950)

item_011 = Product('Phoebus Buddie 30 GS-E', 'Bass Guitar', 8720)
item_012 = Product('Sire U5', 'Bass Guitar', 27490)
item_013 = Product('Lakland Skyline Vintage J', 'Bass Guitar', 82950)
item_014 = Product('Schecter Model T Session 5', 'Bass Guitar', 45900)
item_015 = Product('Tagima Millenium Coda 4', 'Bass Guitar', 14900)

item_016 = Product('Boss Katana 50 Mk II ', 'Accessory', 15950)
item_017 = Product('TC Electronic BH250 Micro Bass', 'Accessory', 18990)
item_018 = Product('Kemper Profiler Powerhead', 'Accessory', 130000)
item_019 = Product('Headrush Pedal Board', 'Accessory', 27490)
item_020 = Product('NUX MG30', 'Accessory', 12900)

inventory = [item_001, item_002, item_003, item_004, item_005, item_006, item_007, item_008, item_009, item_010, item_011, item_012, item_013, item_014, item_015, item_016, item_017, item_018, item_019, item_020]             

#Overall View Function
def view_inv(alist):

    hproduct = "Item Name"
    htype = "Type"
    hprice = "Price"
    havail = "Availability"

    print("\n", hproduct.ljust(35), htype.ljust(28), hprice.ljust(8), havail, "\n")
    for i in range(len(alist)):
        alist[i].view()
        if i%5 == 4:
            print("")
            
#Main function
import sys
def main():
    print("Welcome to the offline guitar store!")
    print("What would you like to do?")
    print("1: View all items")
    print("2: Sort items")
    print("3: Search items")
    print("4: Exit Program")
    
    choice = input("Your Choice: ")              
        
    if choice == '1':
        view_inv(inventory)
    elif choice =='2':
        sorting(inventory)
    elif choice =='3':
        searching(inventory)
    elif choice == '4':
        print("Thank you for using the program!")
        sys.exit()
    else:
        print("Invalid input. Try Again\n")

    main()

#Part 2: Sort Algorithm: Choose between Merge Sort & Quick Sort.
def sorting(alist):
    print("\nPlease choose sorting criteria")
    print("1: Sort by Name")
    print("2: Sort by Price")
    print("3: Reset Sort")
    choice = input("Your Choice: ")
    param = ''
    if choice == '1':
        param = 'name'
        view_inv(alist)
        quick_sort(alist, param)
        view_inv(alist)
    elif choice =='2':
        param = 'price'
        quick_sort(alist, param)
        view_inv(alist)
    elif choice =='3':
        alist[:] = [item_001, item_002, item_003, item_004, item_005, item_006, item_007, item_008, item_009, item_010, item_011, item_012, item_013, item_014, item_015, item_016, item_017, item_018, item_019, item_020]
        view_inv(alist)
    else:
        print("Invalid input. Try Again")
        sorting(alist)

#Insert your code here
# Additional quick sort function to make calling the function easier
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

#Part 3: Search Algorithm: Use binary search and secondary sort algorithm
def searching(alist):
    param = input("\nWhat are you looking for? ")
    param = param.title()
    
    quick_sort(alist, 'type')
    find = binary_search(alist, param, 0, len(alist)-1)
    view_inv(alist)
    if find:
        start = find
        end = find

        # use for loops to find the start and end of all instances of type given by the reference index
        for i in range(len(alist)-1):
            # start from the reference index and decrement. If element is no longer of the same type as reference
            # or index is out of range, end the loop
            if find-i >= 0:
                if getattr(alist[find-i], 'type') != getattr(alist[find], 'type'):
                    start = find-i+1
                    break
            else:
                start = find-i+1
                break
        for i in range(len(alist)-1):
            # start from the reference index and increment. If element is no longer of the same type as reference
            # or index is out of range, end the loop
            if find+i <= len(alist)-1:
                if getattr(alist[find+i], 'type') != getattr(alist[find], 'type'):
                    end = find+i-1
                    break
            else:
                end = find+i-1
                break

        print("\nHere are the results of your search")
        if param == 'Electric Guitar':
            results = alist[start:end+1] #Modify this such that the covered indexes will be of the same type
        else:
            results = alist[start:end+1] #Modify this such that the covered indexes will be of the same type
            
        bubble_sort(results)
        view_inv(results)
    else:
        print("\nSorry, we don't have the item that you are looking for.")
        main()

#Part 3a: Binary Search.
#Return either an index to serve as the reference point for the search results or a boolean value if it does not exist.
#Insert your code here
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
            return middle
    # base case
    else:
        # base definition
        return False

#Part 3b: Secondary Sort Algorithm: Choose between bubble, selection, and insertion sort
#Sort your search results either by price or by name
#Insert your code here
def bubble_sort(args):
    # counter for number of swaps
    swap_count = -1
    
    # if there was a in the previous iteration (or it is the first iteration), keep going
    while(swap_count != 0):
        swap_count = 0

        for i in range (len(args)-1):
            # if the first elements price is greater than the second elements price, swap
            if getattr(args[i], 'price') > getattr(args[i+1], 'price'):
                swap_count+=1;
                temp = args[i]
                args[i] = args[i+1]
                args[i+1] = temp

main()
