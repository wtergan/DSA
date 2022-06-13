'''
DELETE N NODES AFTER M NODES OF A LINKED LIST

    Given a linked list and two integers M, and N, traverse the linked list
    such that you retain M nodes then delete next N nodes, continue
    the same until the end of the list.

    EXAMPLE:
        input: M = 2, N = 2
        linked list: 1->2->3->4->5->6->7->8
        output: 1->2->5->6

        input: M = 3, N = 2
        linked list: 1->2->3->4->5->6->7->8->9->10
        output: 1->2->3->6->7->8
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def skip_M_delete_N(self, m, n):
        pass
