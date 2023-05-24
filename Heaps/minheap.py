"""
    Implementation of Min Heap Data Structure.
        -A specialized tree-based data structure in which the tree is a complete binary
         tree.
        -Min Heap: in which, for any given root node, the value of the root node 
         must be least among all of its child nodes, and the same rule must apply 
         for its left and right sub-tree as well.
        -The process to rearrange the elements to maintain the property of heap data is 
         called "heapify". Its done when a certain node creates an imbalance in the heap
         due to some of the operations on that node. 
        -Extra memory overhead to maintain the heap structure.
        -Slower than other data structures like arrays and linked lists for non-priority queue ops.
        -TIME COMPLEXITY:
            BEST: O(1)
                --Occurs when the heap is already in sorted order (like finding min, max element).
            AVERAGE: O(logN)
                --When the heap is randomly ordered.
                --The total number of comparisons required in the max heap is based on that 
                  tree's height. Height of a complete binary tree is always logN.
            WORST: O(logN)
                --When the heap is in reverse sorted order.
                --Same as for the average case. Based on the height of the tree.
        -SPACE COMPLEXITY:
            BEST: O(1)
                --This can be achieved only if the heap is implemented via Linked List.
            AVERAGE: O(N)
                --Where N is the number of elements in the heap.
            WORST: O(N)
                --Where N is the number of elements in the heap.
"""

class MinHeap:
    """Simple Min Heap class.
       The value present at the root node must be least among all of the values present
       for all of that root's children.
    """
    def __init__(self):
        # Initialization of the minheap array for usage.
        self.minheap = []

    def __repr__(self):
        # Returns the min heap array.
        return str(self.minheap)
    
    def __len__(self):
        # Returns the length of the min heap.
        return len(self.minheap)
    
    def parent(self, idx):
        # Returns the index of the parent node of the node with the index 'idx'.
        return (idx - 1) // 2
    
    def left_child(self, idx):
        # Returns the index of the left child node, given the index 'idx'.
        return 2 * idx + 1

    def right_child(self, idx):
        # Returns the index of the right child node, given the index 'idx'.
        return 2 * idx + 2
          
    def min_heapify(self, idx):
        """Method responsible for restoring the property of the Min Heap.

           -Ensures that the heap property is maintained for the given node. It starts by getting the index of the 
            left and right children node of the parent node at index 'idx'.
           -It then checks whether the current node is less than the left child's value.
           -It then checks whether the current node is less than the right child's value.
           -If the smallest value is not at the current node ('idx'), it means that one of the children has that 
            smallest value. Thus, we swap the current node with the smaller child.
           -After swapping, we call the method recursively on the subtree where the smaller child existed.
           -(Moving current nodes down the heap thats larger than its child nodes.) 
        """
        left = self.left_child(idx)
        right = self.right_child(idx)
        # Assumes that the node at index 'idx' is the smallest.
        smallest = idx
        if left < len(self.minheap) and self.minheap[idx] < self.minheap[left]: smallest = left
        if right < len(self.minheap) and self.minheap[idx] < self.minheap[right]: smallest = right
        if smallest != idx:
            self.minheap[idx], self.minheap[smallest] = self.minheap[smallest], self.minheap[idx]
            self.min_heapify(smallest)

    def down_heapify(self, idx):
        """Method responsible for restoring the property of the Min Heap.
        
           -The check involves seeing if the value of the index's parent node is greater than the value at the 
            current node.
           -If it is, it swaps the position of both, and then sets the index as the child index, which will now correspond
            to the value we originally inserted. the index will keep traversing downwards.
        """
        while idx != 0 and self.minheap[self.parent(idx)] > self.minheap[idx]:
            self.minheap[self.parent(idx)], self.minheap[idx] = self.minheap[idx], self.minheap[self.parent(idx)]
            idx = self.parent(idx)
    
    def insertion(self, value):
        """Insertion of a new value into the Min Heap. O(logN) time complexity for all cases.
        
           -It appends the value into the minheap array, followed by getting the index of that newly inserted value.
           -Then it calls the down_heapify function to satisfy the min heap property.
        """
        self.minheap.append(value)
        idx = len(self.minheap) - 1
        self.down_heapify(idx)

    def deletion(self, value):
        """Deletion of the given value in the Min Heap. O(logN) time complexity for all cases.
        
           -Get the index of the value given, setting that as the last element in the heap, then popping it.
           -We must then min heapify the value at the given index.
        """