'''
Implmentation of the Insertion Sorting Algorithm.
    -Comparing each element in an array with the elemments that comes before it,
        swapping them if they are in the wrong order.
    -Start from the second element in the array, compare the current element with the
        one before it.
    -If the current element is smaller than the one before it, swap the two elements.
    -Repeat step 2 until the current element is in the correct position relative to
        the ones before it.
    -Repeat 1-3 for each element in the whole array.
'''
import time

class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(arr)

    # Implmentation of the Insertion Sort algorithm in ascending order (least to greatest).
    def sort_ascend(self):
        start = time.time()
        # Traverse through all of the elements in the array at each iteration. 
        # Start from the second element in the array.
        for i in range(1, self.len_arr):
            # Initialize "key" as the "ith" element in the array.
            # Initalize "j" as the index/position to the immediate left of the "ith" index.
            key = self.arr[i]
            j = i-1
            # As long as index "j" >= 0 and element at "jth" index is greater than "ith" element (key),
            # swap "j+1th" element and "jth" element.
            while j >= 0 and self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
                j-=1
            # Place key at after the element just smaller than it.
            self.arr[j+1] = key
        end = time.time()
        return self.arr, end-start

    # Implementation of the Insertion Sort Algorithm in descending order (greatest to least).
    def sort_descend(self):
        start = time.time()
        # Traverse through all of the elements in the array at each iteration.
        # Start from the second element in the array.
        for i in range(1, self.len_arr):
            # Initialize "key" as the "ith" element in the array.
            # Initialize "j" as the index/postion to the immediate of left of the "ith" index.
            key = self.arr[i]
            j = i-1
            # As long as index "j" >= 0 and the element at "jth" index is less than "ith", 
            # swap "j+ith" element and "jth" element.
            while j>=0 and self.arr[j] < key:
                self.arr[j+1] = self.arr[j]
                j-=1
            # Place key at after the element just smaller than it.
            self.arr[j+1] = key
        end = time.time()
        return self.arr, end-start

    

    
