# MAGLEO, Simon Benedict A.
# 11 - A
# LG 6.1 - 6.3 : Stacks

# Exercise Section 1 : Stack Class

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

# Exercise Section 2 : Check for Balanced Parentheses

def balanced_par(parenth_string):
    open_par = Stack()
    balanced = True
    idx = 0

    prenth_string = extract_paren(parenth_string)

    if len(prenth_string) == 0:
        print("No parentheses to Extract")
        return

    while idx < len(prenth_string) and balanced: 
        sym = prenth_string[idx]

        if sym == '(':
            open_par.push(sym)
        else:
            if open_par.isEmpty():
                balanced = False
            else:
                open_par.pop()

        idx += 1

    if balanced and open_par.isEmpty():
        return True
    else:
        return False

# Exercise Section 3 : Function to extract parentheses

def extract_paren(parenth_string):
    new_string = ""

    for i in range(len(parenth_string)):
        if parenth_string[i] == ')' or parenth_string[i] == '(':
            new_string += parenth_string[i]

    return new_string
