'''
DELETE EVERY K-TH NODE OF THE LINKED LIST

    remove every k-th node of the linked list. 
    assume that k is always less than equal to length of list.

    EXAMPLE:
    input: 1->2->3->4->5->6->7->8, k = 3
    output: 1->2->4->5->7->8

    input 1->2->4->5->7->8, k = 1
    output: all node deleted

    ALGORITHM:
        -traverse through the linked list, with a counter
        -increment counter after visiting each node
        -if counter == k, delete that node at k, reset counter.
'''

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def delete_k_node(self, k):
        current = self.head
        previous = None
        count = 0
        reached = False
        while current != None:
            count += 1
            if count == k:
                if k == 1:
                    self.head = None
                else:
                    count = 0
                    previous.next = current.next        
            else:
                previous = current
                current = current.next        


    def print_fn(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next

def main():
    delete_k = LinkedList()

    for x in range(10):
        delete_k.add(random.randint(0, 10))

    delete_k.print_fn() 
    print('\n')

    delete_k.delete_k_node(3)

    delete_k.print_fn()

main()            
