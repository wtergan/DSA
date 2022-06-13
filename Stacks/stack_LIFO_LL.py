
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.head == None else False

    '''
    we can simply prepend the linked list, so that last one to add is in 
    front of the list.
    '''
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        current = self.head
        if self.is_empty() == False:
            self.head = current.next

    def peek(self):
        if self.is_empty() == False:
            return self.head.data

    def print_fn(self):
        current = self.head
        while current != None:
            print(current.data, end=' ')
            current = current.next
        print('\n')    

def main():
    s = Stack()

    for x in range(10):
        s.push(random.randint(0, 10))

    s.print_fn()

    print(s.peek())

    s.pop()
    s.print_fn()

main()        
