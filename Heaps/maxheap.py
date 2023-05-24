"""
    Implementation of Max Heap Data Structure.
        -A specialized tree-based data structure in which the tree is a complete binary
         tree.
        -Max Heap: in which, for any given root node, the value of root node must 
          be greatest among all of its child nodes, and the same rule must apply
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

class MaxHeap:
    """Simple Max Heap class.
       The value present at the root node must be greatest among all of the values present
       for all of that root's children.
    """
    def __init__(self):
        # Initialization of the maxheap array for usage.
        self.maxheap = []

    def __repr__(self):
        # Returns the max heap array.
        return str(self.maxheap)
    
    def __len__(self):
        # Returns the length of the max heap.
        return len(self.maxheap)
    
    def parent(self, idx):
        # Returns the index of the parent node of the node with the index 'idx'.
        return (idx - 1) // 2
    
    def left_child(self, idx):
        # Returns the index of the left child node, given the index 'idx'.
        return 2 * idx + 1

    def right_child(self, idx):
        # Returns the index of the right child node, given the index 'idx'.
        return 2 * idx + 2
    
    def max_heapify(self, idx):
        """Method responsibe for restoring the property of the Max Heap.

          -Ensures that the heap property is maintained for the given node. It starts by getting the index of the 
           left and right children node of the parent node at index 'idx'. 
          -It then checks whether the left child's value is greater than the current node's value. 
          -It then checks whether the right child's value is greater than the largest known node's value.
          -If the largest value if not at the current node('idx') it means that one of the children has that
           largest value. Thus, we swap the current node with the larger child.
          -After swapping, we call the methiod recursively on the subtree where the larger child existed.
          -(Moving current nodes down the heap thats smaller than its child nodes.)
        """
        left = self.left_child(idx)
        right = self.right_child(idx)
        # Assumes that the node of at index 'idx' is the largest.
        largest = idx
        if left < len(self.maxheap) and self.maxheap[left] > self.maxheap[idx]: largest = left
        if right < len(self.maxheap) and self.maxheap[right] > self.maxheap[largest]: largest = right
        if largest != idx:
            self.maxheap[idx], self.maxheap[largest] = self.maxheap[largest], self.maxheap[idx]
            self.max_heapify(largest)
    
    def up_heapify(self, idx):
        """Method responsible for restoring the property of the Max Heap.
        
          -The check involves seeing if the value of the index's parent node is less than the value at the current node.
          -If it is, it swaps the position of both, and then sets the index as the parent index, which will 
           now correspond to the value we originally inserted. 
          -The process continues until the index is 0 (meaning its at the tree's root) and the value of the parent node 
           is NOT less than the value of the current node.
          -(Moving elements up the heap thats larger than the child nodes.)
        """
        while idx != 0 and self.maxheap[self.parent(idx)] < self.maxheap[idx]: 
            self.maxheap[idx], self.maxheap[self.parent(idx)] = self.maxheap[self.parent(idx)], self.maxheap[idx]
            idx = self.parent(idx)

    def insertion(self, value):
        """Insertion of a new value into the Max Heap. O(logN) time complexity for all cases.

           -It appends the value into the maxheap array, followed by getting the index of that newly inserted value.
           -Then it calls the up_heapify function to satisfy the max heap property.
        """
        self.maxheap.append(value)
        idx = len(self.maxheap) - 1
        # Call the up_heapify method to restore the max heap propety.
        self.up_heapify(idx)
    
    def deletion(self, value):
        """Deletion of the given value in the Max Heap. O(logN) time complexity for all cases.
        
          -Get the index of the value given, setting that as the last element in the heap, then popping it.
          -We must then max heapify the value at given index.
        """
        # Finding the element to be deleted and then swapping it with the last element in the heap. Then last element
        # can then be removed from the heap and the tree can be heapified.
        idx = self.maxheap.index(value)
        self.maxheap[idx] = self.maxheap[-1]
        self.maxheap.pop()
        self.max_heapify(idx)

    def remove_max(self):
        """Removal of the max value in the Max Heap. O(logN) time complexity for most cases, O(1) if only one element in heap.

           -If the Max Heap's length is greater than 1, we set the root value as the last value of the array,
            then we remove the last element from the heap array, since thats now the max value.
           -We finally heapify to resstore the max heap property, since the root is now the last value of the array.  
        """
        if len(self.maxheap) == 0: return "Empty max heap."
        max = self.maxheap[0]
        if len(self.maxheap) > 1:
            self.maxheap[0] = self.maxheap[-1]
            self.maxheap.pop()
            self.max_heapify(0)
        else: # If there is only one element in the max heap.
            self.maxheap.pop()
        return max
        
    def remove_min(self):
        """Removal of the min value in the Max Heap. O(N) time compelxity for all cases, O(1) if only one element in heap.

          -The method looks for the minimum value in the Max Heap, which can be anywhere in the heap.
          -After finding the min value, it is swapped with the last element, then popped from the list.
          -This is followed by heapifying at the index where we put the last element.
        """
        if len(self.maxheap) == 0: return "Empty max heap."
        # Get the index of the min element, which can be anywhere in the array. Then swap with the last element. Then pop.
        min_idx = self.maxheap.index(min(self.maxheap))
        self.maxheap[min_idx], self.maxheap[-1] = self.maxheap[-1], self.maxheap[min_idx]
        min_value = self.maxheap.pop()
        
        # Heapify at the index where we put the last element.
        if min_idx < len(self.maxheap):
            self.max_heapify(min_idx)
            self.up_heapify(min_idx)
        return min_value

    def get_max(self):
        """Gets the maximum element for the Max Heap. O(1) time complexity for all cases."""
        return self.maxheap[0] if len(self.maxheap) !=0 else "Empty max heap."
    
    def get_min(self):
        """Gets the minimum element for the Max Heap. O(N) time complexity for all cases."""
        return min(self.maxheap) if len(self.maxheap) !=0 else "Empty max heap."
    