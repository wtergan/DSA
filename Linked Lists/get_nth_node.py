'''
GET NTH NODE IN LINKED LIST

    write a function that takes a linked list and an integer index and 
    returns the data value stored in the node at that index position.

    EXAMPLE:
        input: 1->10->30->14, index = 2
        output: 30

    COMPLEXITY:    
        -time: O(n), have to traverse through the linked list, O(1) if first node
        -space: O(1), no extra space is needed 
'''

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    '''
    add(item):
        adds node in the list.
        since order in this case do not matter, we can simply prepend.

        -create new node
        -point the new node to the head
        -set new node as the head
    '''

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node    

    '''
    get_nth(index):
        returns the data thats stored in the node at index position.

        -create count, set to -1
        -create reached, set to False
        -create current, set as head
        -while reached is still False:
            increment count
            if count the same as index:
                set reached to True
            else:
                set current to current.next
        return current.data            

    '''
    def get_nth(self, index):
        current = self.head
        count = -1
        reached = False
        while reached == False:
            count +=1
            if count == index:
                reached = True
            else:
                current = current.next
        return current.data

    def print_fn(self):
        current = self.head
        while current != None:
            print(current.data, end=' ')
            current = current.next
        print('\n')    

def main():
    nth = LinkedList()

    for x in range(10):
        nth.add(random.randint(0,100))

    nth.print_fn()
    print(nth.get_nth(0))   

main()    