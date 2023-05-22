'''
    Implementation of the Qucik Sort Algorithm.
        -A Divide and Conquer Algorithm.
        -Involves picking a pivot, sort everything to the left and right of this
         pivot (partitioning).
        -Many different options in picking this pivot: 
            -- Can be picked at random, first or last element, or median of the array.
        -Partitioning:
            --Given an array and an element 'x' of an array as the pivot, put 'x' in its 
              correct position in a sorted array, and put all smaller elements 
              (smaller than x) before x, all greater elements after. Reversed if in 
              descending order.
        -Recursively do the same for the left subarray and right subarray.
        -TIME COMPLEXITY:
            BEST: 
            AVERAGE:
            WORST:
'''
import numpy as np
import time

'''class QuickSort:
    def __init__(self, arr, start, end):
        self.arr = arr
        self.start = start
        self.end = end
        self.len_arr = len(arr)

    # Implementation of the quicksort part of the algorithm. Called recursively.
    def sort_ascend(self):
        # Only sort if the part that's being sorted is more than one element.
        if self.start < self.end:
            # Find pivot element such that element smaller than the pivot are on the left
            # element greater than the pivot are on the right.
            pivot = self.partition(self.arr, self.start, self.end)

            # Recursively call on the left of the pivot.
            self.sort_ascend(self.arr, self.start, pivot-1)

            # Recursively call on the right of the pivot.
            self.sort_ascend(self.arr, pivot+1, self.end)
        return self.arr

    # Implementation of the partition part of the algorithm.
    def partition(self, arr, start, end):
        # For this implementation, we will select the pivot as the rightmost element.
        pivot_element = self.arr[self.end]
        # This "i" will be pointer for the greater element.
        i = 0
        # Traverse through all of the elements. Compare each element with the pivot.
        for j in range(start, end):
            if arr[j] <= pivot_element:
                # If element smaller than the pivot is found, then we swap it with the 
                # greater element pointed by "i".
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # Swap the pivot element with every greater element specified by "i"
        arr[i+1], arr[self.end] = arr[self.end], arr[i+1]
        # Return the position from where the partition is done.
        return i + 1
    

array = [10,7,8,9,1,5]
sort = QuickSort(array, 0, len(array)-1)
sort.sort_ascend()
print(sort)'''

# Function that perform the partition for the quicksort.
def partition(array, start, end):
    # Choose the rightmost element as the pivot.
    pivot = array[end]
    # Pointer for the greater element.
    i = start - 1
    # Traverse through all of the elements in the array, compare each element with the pivot.
    for j in range(start, end):
        if array[j] <= pivot:
            # If the element is smaller than the pivot, swap it with the greater element pointed by i.
            i += 1
            array[i], array[j] = array[j], array[i]
        # Swap the pivot element with every element specified by i.
        array[i+1], array[end] = array[end], array[i+1]
        # Return the position from where the partition is done.
        return i + 1

# Function that performs the quicksort. Called recursively on both sides of the pivot.
def quicksort(array, start, end):
    if start < end:
        # Find pivot element such that element smaller is to the left, element larger is to
        # the right.
        piv = partition(array, start, end)
        # Recursively call on the left of the pivot.
        quicksort(array, start, piv-1)
        # Recursively call on the right of the pivot.
        quicksort(array, piv+1, end)

array = [10,7,8,9,1,5]
quicksort(array, 0, len(array)-1)

print(f'The sorted array is : {array}')




