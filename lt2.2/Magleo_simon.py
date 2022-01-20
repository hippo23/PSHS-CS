#CS5 2nd Quarter Long Exam 2
#Last Name, First Name
#Grade Level

#Part1 : Arrange the following algorithms in increasing time complexity.  
steps = 0

#Recursive Factorial
#Best Case: Ω(n)
#Worst Case: O(n)
def fact(x): 
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 0:
        return 1
    else:
        return (x * fact(x-1))

#Merge Sort
#Best Case: Ω(nlogn)
#Worst Case: O(nlogn)
def merge(alist):
    '''This is the merge sort algorithm'''
    print("Splitting ",alist)
    if len(alist)>1: 
        mid = len(alist)//2
        lefthalf = alist[:mid] 
        righthalf = alist[mid:] 

        merge(lefthalf) 
        merge(righthalf) 

        i=0 
        j=0
        k=0

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
#Best Case: Ω(n^2)
#Worst Case: O(n^2)
def pascal(n):
    global steps
    iterations = 0
    '''This is a recursive function that gets
       the nth row of the pascal's triangle'''
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        print("-------")
        print(previous_line)
        for i in range(len(previous_line)-1):
            print(i)
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        print(line)
    return line



#Selection Sort
#Best Case: Ω(n^2)
#Worst Case: O(n^2)
def selection(collection):
    '''This is the modified version of selection sort that I discussed in class'''
    for endnum in range(len(collection)-1, 0, -1):
        print(collection)
        max_idx = endnum
        if max(collection[0:endnum]) > collection[endnum]:
            max_idx = collection.index(max(collection[0:endnum]))
        collection[endnum], collection[max_idx] = collection[max_idx], collection[endnum]


#Part 2: Create a palindrome checker using Stacks.


#Put your Stack Class below.
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

#Put your code below.
#palindrome checker
def balanced_par(palin_string):
    left_half = Stack()
    palindrome = True
    middle = (len(palin_string)-1)//2
    new_string = palin_string
    if len(palin_string)%2 != 0:
        new_string = palin_string[:middle] + palin_string[middle+1:]
        middle = (len(new_string)-1)//2

    for i in range(len(new_string)):
        if i <= middle:
            left_half.push(new_string[i].lower())
        else:
            if new_string[i].lower() != left_half.pop():
                palindrome = False

    return palindrome

pascal(10)
print(steps)
