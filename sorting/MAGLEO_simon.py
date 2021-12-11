# MAGLEO, Simon Benedict A. 
# 11 - A
# LG 4.2 - LG 4.6 Sorting Algorithms

# Exercise Section 1 - Bubble Sort
def bubble_sort(args):
    swap_count = -1
    
    while(swap_count != 0):
        swap_count = 0

        for i in range (len(args)-1):
            try:
                if args[i] > args[i+1]:
                    swap_count+=1;
                    temp = args[i]
                    args[i] = args[i+1]
                    args[i+1] = temp
            except TypeError:
                if isinstance(args[i], int) == False:
                    swap_count+=1;
                    temp = args[i]
                    args[i] = args[i+1]
                    args[i+1] = temp
        print(args)

# Exercise Section 2 - Quick Sort
def quick_sort(args):
    splitpoint_type = partition_type(args, 0, len(args)-1)
    left_arr = args[0:splitpoint_type+1]
    right_arr = args[splitpoint_type+2:len(args)]

    quicksort_helper(left_arr, 0, len(left_arr)-1)
    quicksort_helper(right_arr, 0, len(right_arr)-1)
    args = left_arr + right_arr

    return args

def quicksort_helper(args, start, end):
    if start < end:
        splitpoint = partition(args, start, end)
        quicksort_helper(args, start, splitpoint-1)
        quicksort_helper(args, splitpoint+1, end)

def partition(args,first,last):
   pivotvalue = args[first] #select pivot value
   leftmark = first+1 #assign left position marker
   rightmark = last #assign right position marker

   done = False
   while not done: #while split point is not foun 
       while rightmark >= 0 and args[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
       while leftmark <= len(args)-1 and args[leftmark] >= pivotvalue and leftmark <= rightmark:
            leftmark = leftmark + 1
       if rightmark < leftmark:
            done = True
       else:
            temp = args[rightmark]
            args[rightmark] = args[leftmark]
            args[leftmark] = temp

   temp = args[first]
   args[first] = args[rightmark]
   args[rightmark] = temp
   print(args[first:last+1])

   return rightmark


def partition_type(args,first,last):
   leftmark = first+1 #assign left position marker
   rightmark = last #assign right position marker
   swaps = 0

   done = False
   while not done: #while split point is not foun 
       while rightmark >= 0 and isinstance(args[rightmark], int) == False and rightmark >= leftmark:
            rightmark = rightmark - 1
       while leftmark <= len(args)-1 and isinstance(args[leftmark], int) == True and leftmark <= rightmark:
            leftmark = leftmark + 1
       if rightmark < leftmark:
            done = True
       elif rightmark >= 0 and leftmark <= len(args)-1:
            temp = args[rightmark]
            args[rightmark] = args[leftmark]
            args[leftmark] = temp
            swaps+=1

   if swaps > 0:
       temp = args[first]
       args[first] = args[rightmark]
       args[rightmark] = temp

   if isinstance(args[rightmark], int) == True:
       return rightmark
   else:
       return rightmark - 1


list1 = [19, 5, 'cat', 'rabbit', 2, 32, 'mice', 'dog', 7]
list2 = ['traveler', 'paimon', 12, 36, 10, 'venti', 'jean', 29, 34, 75, 'aloy']
list3 = [27, 'harry', 'ron', 17, 'hermione', 78, 93, 'dobby', 132, 'dumbledore']

# Bubble Sort Demonstration
print("Bubble Sorting:")
bubble_sort(list1)
print("Sorting the first list: {}".format(list1))

# Quick Sort Demonstration
list2 = ['traveler', 'paimon', 12, 36, 10, 'venti', 'jean', 29, 34, 75, 'aloy']
print("Quick Sorting:")
list2 = quick_sort(list2)
print("Sorting the first list: {}".format(list2))
