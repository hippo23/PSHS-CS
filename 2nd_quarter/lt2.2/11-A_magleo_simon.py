#CS5 2nd Quarter Long Exam 2
#Last Name, First Name
#Grade Level

#Part1 : Arrange the following algorithms in increasing time complexity.  

#Recursive Factorial
#Best Case: Ω(n) : linear
#Worst Case: O(n) : linear
def fact(x): 
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 0:
        return 1
    else:
        # each time we call the fact function recursively, it will take us constant time. The number of times 
        # the function recurses is equal to x, where x is the number that was entered.
        # Thus, the number of steps that is required by the algorithm is n, giving us linear time complexity
        # worst and best case will take the same time
        return (x * fact(x-1))

#Merge Sort
#Best Case: Ω(nlogn) : loglinear
#Worst Case: O(nlogn) : loglinear
def merge(alist):
    '''This is the merge sort algorithm'''
    print("Splitting ",alist)
    if len(alist)>1: 
        mid = len(alist)//2
        lefthalf = alist[:mid] 
        righthalf = alist[mid:] 

        # we recursively call merge on the array, eventually splitting the array logn times
        merge(lefthalf) 
        merge(righthalf) 

        i=0 
        j=0
        k=0

        # when merging the array back together, we do n things. Thus, we do n things, logn times, giving us a time complexity of loglinear
        # we will also not know if a list is sorted until the very end, meaning that the best and worst case of the algorithm is the same
        while i < len(lefthalf) and j < len(righthalf):
            
            if lefthalf[i] <= righthalf[j]: 
                alist[k]=lefthalf[i] 
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

#Pascal's Triangle
#Best Case: Ω(n^2) : quadratic
#Worst Case: O(n^2) : quadratic
def pascal(n):
    '''This is a recursive function that gets
       the nth row of the pascal's triangle'''
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        # iterate throughout the length of the previous line - 1. In total, the amount of times we iterate is equal to 1 + 2... + (n-3) + (n-2)
        # this gives us quadratic time
        # this is the same for both best case and worst case.
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line



#Selection Sort
#Best Case: Ω(n^2) : quadratic
#Worst Case: O(n^2) : quadratic
def selection(collection):
    '''This is the modified version of selection sort that I discussed in class'''
    # iterate througout the length of the array, starting from the end
    for endnum in range(len(collection)-1, 0, -1):
        print(collection)
        max_idx = endnum
        # if any number is greater than the current element at endnum, swap those numbers
        # in total, we will have to iterate n times, doing roughly n-1 comparisons each time.
        # this gives us a time complexity of n^2 for both worst case and best case
        # as the algorithm will not know that the list is already sorted until the very end
        if max(collection[0:endnum]) > collection[endnum]:
            max_idx = collection.index(max(collection[0:endnum]))
        collection[endnum], collection[max_idx] = collection[max_idx], collection[endnum]


#Part 2: Create a palindrome checker using Stacks.

#Put your Stack Class below.
class Stack:
    # store all values in stack in items attribute
    def __init__(self):
        self.items = []
    # use push to appen any elemnts to the items attribute
    def push(self, item):
        self.items.append(item)
    # use pop to delete and return the last elemement in the items attribute
    def pop(self):
        return self.items.pop()

#Put your code below.
#palindrome checker
def balanced_par(palin_string):
    # the left half of the string will be stored in a Stack
    left_half = Stack()
    # declare boolean to show whether or not the string is a palindrome
    palindrome = True
    # get the middle of the string
    middle = (len(palin_string)-1)//2
    # in the event of an odd-numbered string, use a separate variable to ignore the middle character without changing the original string
    new_string = palin_string
    if len(palin_string)%2 != 0:
        # ignore middle character if string is odd-numbered
        new_string = palin_string[:middle] + palin_string[middle+1:]
        # find middle of new string
        middle = (len(new_string)-1)//2
    
    # iteratate throughout the entire length of the new string
    for i in range(len(new_string)):
        # if we are still before or at the middle of the string, continue to add current elemement to stack
        if i <= middle:
            left_half.push(new_string[i].lower())
        else:
            # if we are no longer at the middle, remove the last item from the stack and compare it to the current elemement in the new string
            if new_string[i].lower() != left_half.pop():
                # in the case that they are different, the string is no longer a palindrome
                palindrome = False
                break

    # if no character in the right half was different from the left half, then the string is a palindrome
    return palindrome

