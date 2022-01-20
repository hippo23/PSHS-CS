import time
import random

# roll a regular (6 sided) die
# O(1) - constant time
def roll_dice():
    # as can be seen, the function only executes one command to generate a number from 1 to 6
    # with the command itself only taking constant time, thus, the time complexity of the function
    # is constant time or O(1) as well.
    return random.randint(1,6)

# binary search
# O(log(n)) - logarithmic time complexity
def binary_search(find, collection):
    first = 0
    last = len(collection) - 1
    found = False
    while first<=last and not found:
        mid = (first + last)//2
        print(collection[mid])
        if collection[mid] == find:
            found = True
        else:
            if find < collection[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

# quick sort
# O(nlogn) - loglinear time complexity
def quick_sort(alist,first,last):
    
    if first < last: 
       splitpoint = partition(alist,first,last) 
       quick_sort(alist,first,splitpoint-1) 
       quick_sort(alist,splitpoint+1,last) 

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
# O(n^2) - Quadratic Time Complexity
def insertion(alist):
   for index in range(1,len(alist)): 
     print(alist)
     currentvalue = alist[index]
     position = index
     
     while position>0 and alist[position-1]<currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

# brute-force attack to break alpha-numeric passwords
# O(64^n) - exponential time complexity

memo = {}
time_taken = 0.0
def hanoi(x):
    global time_taken

    time_before = time.process_time()
    if x in memo.keys():
        return memo[x]
    if x == 1:
        return 1

    steps = hanoi(x-1) + hanoi(x-1)
    memo[x] = steps
    time_after = time.process_time()
    time_taken = time_after - time_before
    return steps

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
