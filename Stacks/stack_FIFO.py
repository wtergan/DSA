'''
STACKS FIFO

    this is the implementation of First In First Out stacking.

'''

import random

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == None

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        first = self.stack[0]
        self.stack = self.stack[1:]
        return self.stack

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)  

    def print_fn(self):
        print(self.stack, '\n')                     

def main():
    s = Stack()

    for x in range(10):
        s.push(random.randint(0, 10))

    s.print_fn()

    print(s.peek())

    s.pop()
    s.print_fn()

main()    