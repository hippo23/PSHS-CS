# MAGLEO, Simon Benedict A.
# 11 - A
# LG 3.1 - 4.1 Recursion

# Exercise 1 - Recursion
def collatz_conjecture(x, steps=0): # base case
    if x == 1:
        # base definition
        return steps
    # recursive case
    elif x%2 == 0:
        # recursive definition 
        steps+=1
        return collatz_conjecture(x/2, steps)
    # recursive case
    else:
        # recursive defintion
        steps+=1
        return collatz_conjecture(3*x + 1, steps)

def gcf(num1, num2):
    dividend = max(num1, num2)
    divisor = min(num1, num2)

    next_dividend = (dividend//divisor) * divisor
    next_divisor = dividend - next_dividend

    # base case
    if next_divisor == 0:
        # base definition
        return divisor
    # base case
    elif next_divisor == 1:
        # base definition
        return 1
    # recursive case
    else:
        # recursive definition
        return gcf(next_divisor, next_dividend)

# Exercise 2 - Search Algorithms 
def binary_search(list, x, bottom_limit, top_limit):

    # check if the base case is true
    if top_limit>=bottom_limit:
        middle_point = (top_limit + bottom_limit)//2
        # recursive case 1 and 2
        if list[middle_point]<x:
            return binary_search(list, x, middle_point+1, top_limit)
        elif list[middle_point]>x:
            return binary_search(list, x, bottom_limit, middle_point-1)
        # base case & definition
        else:
            return middle_point
    else:
        # base case definition
        return -1

def sequential_search(list, x, size):
    # check for the base case
    if size >= 0:
        # base case 2
        if list[size] == x:
            # base definition 2
            return size
        # recursive case 1
        else:
            # recursive definition 1
            return sequential_search(list, x, size-1)
    else:
        # base case definition
        return -1

# Collatz Conjecture test
print("The number of steps taken to transform 140 to 1 is: {}\n".format(collatz_conjecture(140)))

# Greatest Common Factor test
print("The greatest common factor of 198 and 360 is: {}\n".format(gcf(198, 360)))

# list 1
number_list = [2, 4, 6, 10, 12 ,14 ,20, 22, 24, 28, 30, 32]
## sequential search
print(sequential_search(number_list, 22, len(number_list)-1))
print(sequential_search(number_list, 27, len(number_list)-1))
print()
## binary search
print(binary_search(number_list, 22, 0, len(number_list)-1))
print(binary_search(number_list, 27, 0, len(number_list)-1))
print()

## COMMENTS: More efficient algorithm: Binary search. Steps taken by binary search is 3. Steps take by sequential search are 8 and n (size of list) steps.

# list 2
animal_list = ['cat', 'dog', 'lizard', 'mice', 'rabbit', 'snake']
## sequential search
print(sequential_search(animal_list, 'lizard', len(animal_list)-1))
print(sequential_search(animal_list, 'spider', len(animal_list)-1))
print()
## binary search
print(binary_search(animal_list, 'lizard', 0, len(animal_list)-1))
print(binary_search(animal_list, 'spider', 0, len(animal_list)-1))
print()

## COMMENTS: More efficient algorithm: Binary Search. Steps taken by Binary search is 1 and 2. Steps taken by sequential search is 3 steps and n (size of list) steps.

# list 3
mixed_list = [2, 5, 7, 19, 32, 'cat', 'dog', 'mice', 'rabbit']
## sequential search
print(sequential_search(mixed_list, 'mice', len(mixed_list)-1))
print(sequential_search(mixed_list, 28, len(mixed_list)-1))
print()
## binary search
print(binary_search(mixed_list, 28, 0, len(mixed_list)-1))
### returns an error: print(binary_search(mixed_list, 'mice', 0, len(mixed_list)-1))

## COMMENTS: Sequential search is the better of the two algorithms to use in this situation, as the list has multiple data types. 
## Using a '<' or '>' operator to compare a string and an integer will return an error, thus making binary search an invalid option.
