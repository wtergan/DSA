'''
STACKS LIFO

    linear data structure that follows a particular order in which the operations
    are followed.
        -LIFO (Last In First Out)
        -FIFO (First In First Out)

    main operations includes: push(), pop(), size(), peek(), etc.

    two main ways of implementing a stack:
        -using arrays
        -using linked lists 
'''

import random

class Stack:
    def __init__(self):
        self.stack = []

    '''
    is_empty():
        determine if the stack is empty or not.
    '''
    def is_empty(self):
        return self.stack == None

    '''
    push():
        adds item in the top of the stack. (appends).
    '''
    def push(self, item):
        self.stack.append(item)

    '''
    pop():
        removes the top item in the stack (LIFO), returns item.
        we could have easily used the official pop method for this.
    '''
    def pop(self):
        top = self.stack[-1]
        self.stack = self.stack[:-1]
        return top
    '''
    peek():
        returns the top item from the stack but does not remove it.
    '''
    def peek(self):
        return self.stack[-1]

    '''
    size(): 
        returns the size of the stack.
    '''    
    def size(self):
        return len(self.stack)    

    '''
    print_stack():
        prints the stack.
    '''     
    def print_stack(self):
        print((self.stack), '\n')   


def main():
    s = Stack()

    for x in range(10):
        s.push(random.randint(0,10))

    s.print_stack()

    print(s.peek(), '\n')

    s.pop()
    s.print_stack()
main()        