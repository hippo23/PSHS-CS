# MAGLEO, Simon Benedict A.
# 11 - A
# LG 5.1 - 5.3 Analysis of ALgorithms

import time
import random

# Exercise Section 1 - Analysis of Algorithms

# roll a regular (6 sided) die
# Running time complexity - O(1)
def roll_dice():
    # we only execute the function once, with the operation taking constant time.
    # thus, the time complexity of the function overall will also be constant time.
    return random.randint(1,6)

# binary search
# Running time complexity - O(log(n))
def binary_search(find, collection):
    first = 0
    last = len(collection) - 1
    found = False
    while first<=last and not found:
        mid = (first + last)//2
        # find the middle of the list
        print(collection[mid])
        # assuming this is the worst-case scenario, we won't find the element we already
        # searching for until the very end of the algorithm
        if collection[mid] == find:
            found = True
        else:
            # continue to split the list in half if we don't find the element we are searching for
            if find < collection[mid]:
                last = mid - 1
            else:
                first = mid + 1

    # The number of times we can split a list into halves is equal to log2(n). 
    # Since each iteration of the loop takes constant time, the time complexity
    # of the algorithm overall will be log2(n), or log(n) in short.
    return found

# quick sort
# Running time comeplexity - O(n^2)
def quick_sort(alist,first,last):
    
    if first < last: 
       splitpoint = partition(alist,first,last) 
       quick_sort(alist,first,splitpoint-1) 
       quick_sort(alist,splitpoint+1,last) 
       # the worst case for this algorithm is when the pivot value chosen by the parition function
       # is either always the greatest or always the smallest value. Thus, the first time we partition the array,
       # we will end up with a parition that is size 1, and a parition that is size n-1. The time taken to
       # do this will also be n-1. We then continue to call the parition function recursively until both paritions
       # it produces are of size 1.

       # overall, the time it will take to partition and sort the entire array will be equal to
       # n + n-1 + n-2 + ... 3 + 2. This leaves us with a worst case time complexity of n^2.

def partition(alist,first,last):
   pivotvalue = alist[first]
   print(alist[first:last+1]) 
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] >= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] <= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark] #swap values
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print(alist[first:last+1])

   return rightmark

# insertion sort
# Running time complexity - O(n^2)
def insertion(alist):
   for index in range(1,len(alist)): 
     # iterate throughout the list
     print(alist)
     currentvalue = alist[index]
     position = index
     
     # for each iterations of the list, we will have to go through 1 + 2 + 3... + (n-2) + (n-1)
     # comparisons and swaps. This is only true in the worst-case scenario wherein the list is sorted
     # in reverse
     while position>0 and alist[position-1]<currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

# brute-force attack to break alpha-numeric passwords
# Running time comeplexity - O(2^n)

# the number of possible combinations that an alphanumeric password 
# of length n can have is equal to 62^n, where 62 is the amount of
# unique alphanumeric characters. 
# In the worst case, we will only find the right password at the 
# very end. Thus, we need to generate 62^n passwords, with the generation
# of each password taking constant time.

# Exercise Section 2 - Dynamic Programming

# declare memo dictionary to store results of all subproblem
memo = {}
time_taken = 0.0
def hanoi(x):
    global time_taken

    time_before = time.process_time()
    # if the subproblem of the algoritm has already been memoized, get result from memo
    if x in memo.keys():
        return memo[x]
    # if not and x == 1, execute base case
    if x == 1:
        return 1

    # else, recursively call hanoi(x-1) twice 
    steps = hanoi(x-1) + hanoi(x-1)
    # memoize number of steps for current subpoblem
    memo[x] = steps
    time_after = time.process_time()
    time_taken = time_after - time_before
    # return the number of steps
    return steps
    # In this algorithm, hanoi(x) (where x is some number) recurses only the first time its called. Thus, the number of subproblems
    # we actually need to solve is n, with each subproblem taking constant time.
    # This shows that the time complexity of the algorithm is linear.

def hanoi_nonmemo(x):
    global time_taken

    time_before = time.process_time()

    if x == 1:
        return 1
    steps = hanoi_nonmemo(x-1) + 1 + hanoi_nonmemo(x-1)
    time_after = time.process_time()
    time_taken = time_after - time_before
    return steps

def main():
    global time_taken

    discs = int(input("How many discs do you want to have?: "))

    steps = hanoi_nonmemo(discs)
    print("\nNon-memoized:")
    print("-> STEPS TAKEN: {}".format(steps))
    print("-> TIME TAKEN:  {}".format(round(time_taken, 10)))

    time_taken = 0.0

    steps = hanoi(discs)
    print("\nMemoized:")
    print("-> STEPS TAKEN: {}".format(steps))
    print("-> TIME TAKEN:  {}".format(round(time_taken, 10)))

main()
