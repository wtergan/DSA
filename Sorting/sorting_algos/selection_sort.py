'''
    Implementation of the Selection Sort Algorithm.
        -Repeatedly find the minumum element from the unsorted part of the array,
         put that min element in its correct place (beginning or end depending on order
         choice).
        -Maintains two sub arrays in the given array:
            Sorted subarray, which starts with the first element and grows from left to right.
            Unsorted subarray, which consists of the remaining elements that is needed to be 
                sorted.
        -TIME CONPLEXITY:
            BEST: 
            AVERAGE:
            WORST:
'''
import numpy as np
import time

class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(arr)

    # Implementation of the Selection Sort Algorithm in ascending order (least to greatest).
    def sort_ascend(self):
        # Find the minimum element in the array at each "ith" iteration. N total passes.
        start = time.time()
        for i in range(self.len_arr):
            # Initialization of minimum index, starts at "i".
            min_idx = i
            # Traverse through this unsorted subarray, changing min_idx to relect the 
            # "jth" position of the minimum element.
            for j in range(i+1, self.len_arr):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            # Once that traversal in complete, swap element at position "i" with element at 
            # position "j". Now minimum element is in correct posiiton.
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
        end = time.time()
        return self.arr, end-start

    # Implementation of the Selection Sort Algorithm in descending order (greatest to least).
    def sort_descend(self):
        # Find the maximum element in the array at each "ith" iteration. N total passes.
        start = time.time()
        for i in range(self.len_arr):
            # Initialization of maximum index, starts at "i".
            max_idx = i
            # Traverse through this unsorted subarray, changing max_idx to reflect the 
            # "jth" position of the maximum element.
            for j in range(i+1, self.len_arr):
                if self.arr[j] > self.arr[max_idx]:
                    max_idx = j
            # Once that traversal is complete, swap element at position "i" with element at 
            # position "j". Now maximum element is in correct position.
            self.arr[i], self.arr[max_idx] = self.arr[max_idx], self.arr[i]
        end = time.time()
        return self.arr, end-start


