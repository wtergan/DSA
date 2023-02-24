'''
    Implementation of the Bubble Sort algorithm:
        -Repeatedly swap the adjacent elements if they are in the 
         wrong order. 
        -Not suitable for large data sets.
        -TIME COMPLEXITY:
            BEST: O(n)
                --List is already sorted, no swaps needed. 
                --Still have to iterate through list once in order to check.
            AVERAGE: O(n^2)
                --Roughly (n^2)/4 comparisons and swaps.
            WORST: O(n^2)
                --List is in total reverse order, max swaps needed.
                --n(n-1)/2 total comparisons and swaps.
'''
import time

class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(arr)

    # Implementation of the Bubble Sort Algorithm in ascending order (least to greatest).
    def sort_ascend(self):
        start = time.time()
        # Traverse through all of the elements in the array at each iteration. This is N passes.
        for i in range(self.len_arr):
            # Last "i" elements already in place. Perform N-i-1 total comparisons at each iteration.
            for j in range(0, self.len_arr - i - 1):
                # If element at position "j" is greater than element at "j+1", swap.
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        end = time.time()
        return self.arr, end-start
    
    # Implementaion of the Bubble Sort Algorithm in descending order (greatest to least).
    def sort_descend(self):
        start = time.time()
        # Traverse trrough all of the elements in the array at each iteration. This is N passes.
        for i in range(self.len_arr):
            # Last "i" elements already in place. Perform N-i-1 total comparisions at each iteration.
            for j in range(0, self.len_arr-i-1):
                # If element at position "j" is less than element at "j+1", swap.
                if self.arr[j] < self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
        end = time.time()
        return self.arr, end-start


