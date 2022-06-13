'''
FIND MIDDLE OF LINKED LIST

    write a function that finds the middle of the list

    EXAMPLE:
        input: 1->2->3->4->5
        output: 3

        input: 1->2->3->4->5->6 
        output: 4 (second middle)   
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

    '''
    middle_0():
        traverse through the list, and count number of nodes.
        traverse through the list again, until count/2 node is reached.
    '''
    def middle_0(self):
        traverse_0 = self.head
        traverse_1 = self.head
        count_0 = 0
        count_1 = 0
        reached = False
        while traverse_0 != None:
            count_0 += 1
            traverse_0 = traverse_0.next

        if count_0/2 % 2 != 0:
            count_0 += 1    

        while reached == False:
            count_1 += 1
            if count_1 == count_0/2:
                reached = True
            else:
                traverse_1 = traverse_1.next
        return traverse_1.data            

    def middle_1(self):
        slow = self.head
        fast = self.head
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def print_fn(self):
        current = self.head
        while current != None:
            print(current.data, end=' ')
            current = current.next
        print('\n')

def main():
    find_middle = LinkedList()

    for x in range(5):
        find_middle.add(random.randint(0, 10))

    find_middle.print_fn()

    print(find_middle.middle_0())

main()