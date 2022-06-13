'''
DELETE DUPLICATES

    write a function that takes a list sorted in assorted order and deletes
    any duplicate nodes from the list. The list should only be traversed once.

    EXAMPLE
        LL before removal: 11->11->11->21->43->43->60
        LL after removal: 11->21->43->60

    COMPLEXITY:
        -time: O(n), where n is the number of nodes in the list
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
        adds node in the list in ascending order.
        if the data in the current node is greater than the data in new node,
        this means that we can place the new node in this position.

        -create current, set as head
        -create previous, set as None
        -create new node
        -create stop, set as False
        -while current is not None and stop is still False:
            if current.data is greater than the item in new node:
                stop = True
            else:
                we keep traversing through the list
        -if previous is None (which means current is the head):
            point the new node to the head
            set the head as the new node
        -else:
            point the new node to the current node
            point previous node to the new node    
    '''

    def add(self, item):
        new_node = Node(item)
        current = self.head
        previous = None
        stop = False
        while current != None and stop == False:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
        if previous == None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            previous.next = new_node

    '''
    remove(item):
        deletes a node that contains the item specified.

        -create current, set as head
        -create previous, set as None
        -create found, set as False
        -while found is still False:
            if current.data is same as item:
                found = True
            else:
                set previous to current
                set current as current.next
    '''

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while found == False:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    '''
    delete_duplicate():
        removes any duplicate items in the list.

        -create current, set as head
        -while current.next is not None:
            if current.data is same as current.next:
                point current.next to current.next.next
            else:
                set current as current.next

    '''
    def delete_duplicates(self):
        current = self.head
        while current.next != None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    '''
    print_fn():
        output the linked list.

        -create current, set as head
        -while current is not None:
            print the data in current
    '''
    
    def print_fn(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next


def main():
    duplicate = LinkedList()

    for x in range(10):
        duplicate.add(random.randint(0, 10))

    duplicate.print_fn() 
    print('\n')

    duplicate.delete_duplicates()
    duplicate.print_fn()

main()