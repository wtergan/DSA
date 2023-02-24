
import numpy as np
import time 

class Sort: 
    '''
    A class that contains implementation of common sorting algorithms.

    Attributes at initalization:
    ============================
    arr: array-like 
        -The array that needs to be sorted.
    len_arr: int
        -The length of the array.

    Methods:
    ========
    bubble_sort(order):
        -Implementation of the Bubble Sort algorithm.
    selection_sort(order):
        -Implementation of the Selection Sort algorithm.
    insertion_sort(order):
        -Implementation of the Insertion Sort algorithm.
    merge_sort(order):
        -Implementation of the Merge Sort algorithm.
    quick_sort(order):
        -Implementation of the Quick Sort algorithm.
    heap_sort(order):
        -Implementation of the Heap Sort algorithm.
    counting_sort(order):
        -Implementation of the Counting Sort algorithm.
    radix_sort(order):
        -Implementation of the Radix Sort algorithm.
    
    The methods will do the following tasks:
        -Sort the given array in ascending order.
        -Sort the given array in descending order.
        -Give the run-time of the algorithm(s)
        -Give the Time and Space Complexities for the algorithm(s).
    '''
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(self.arr)
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
    def bubble_sort(self, order):
        # Implementation of algorithm in ascending order:
        if order == 'ascend':
            # Traverse through all of the elements in the array.
            start = time.time()
            for i in range(self.len_arr):
            # Last i elements already in place, doing n-1 comparisons.
                for j in range(0, self.len_arr-i-1):
                    if self.arr[j] > self.arr[j+1]:
                        self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
            end = time.time()
            return self.arr, end-start

        # Implementation of algorithm in descending order:
        elif order == 'descend':
            # Traverse through all of the elements in the array.
            start = time.time()
            for i in range(self.len_arr):
                # Last i elements already in place, doing n-1 comparisons. Then swap adjacent
                # elements.
                for j in range(0, self.len_arr-i-1):
                    if self.arr[j] < self.arr[j+1]:
                        self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
            end = time.time()
            return self.arr, end-start

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
    def selection_sort(self, order):
        # Implementation of the algorithm in ascending order:
        if order == 'ascend':
            # Traverse through the array, finding the minimum element in the array.
            start = time.time()
            for i in range(self.len_arr):
                # Initializaion of min index, start at i.
                min_idx = i
                # Unsorted subarray. Traverse through it, changing min_idx to reflect least 
                # element. Then swap once you finish iterating that subarray.
                for j in range(i+1, self.len_arr):
                    if self.arr[j] < self.arr[min_idx]:
                        min_idx = j
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            end = time.time()
            return self.arr, end-start

        # Implementation of the algorithm in descending order:
        elif order == 'descend':
            # Traverse through the array, finding the min element in the array.
            # if min element is found, swap, then increment min index.
            start = time.time()
            for i in range(self.len_arr):
                # Initalization of min index, start at i.
                min_idx = i
                # Unsorted subarray. Traverse through it, changing min_idx to reflect greatest
                # element. then swap once you finish iterating that subarray.
                for  j in range(i+1, self.len_arr):
                    if self.arr[j] > self.arr[min_idx]:
                        min_idx = j
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
            end = time.time()
            return self.arr, end-start

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
    def insertion_sort(self, order):
        # Implementation of the algorithm in ascending order:
        if order == 'ascend':
            # Traverse through the array, starting from the second element.
            start = time.time()
            for i in range(1, self.len_arr):
                key = self.arr[i]
                j = i-1
                while j >= 0 and self.arr[j] > key:
                    self.arr[j+1] = self.arr[j]
                    j-=1
                self.arr[j+1] = key
            end = time.time()
            return self.arr, end-start

        elif order == 'descend':
            # Traverse through the array, starting from the second element.
            start = time.time()
            for i in range(1, self.len_arr):
                key = self.arr[i]
                j = i-1
                while j >=0 and self.arr[j] < key:
                    self.arr[j+1] = self.arr[j]
                    j-=1
                self.arr[j+1] = key
            end = time.time()
            return self.arr, end-start
    '''
    Comparison method.
        -This method compares the time between two different sorting algorithms.
    '''
    def compare_sort(self, sort_time_1, sort_time_2):
        # Find the difference in execution times between the two algorithms.
        print(f'This is the execution time of the first sort: {sort_time_1}')
        print(f'This is the execution time of the second sort: {sort_time_2}')
        print(f'Difference in execution time: {np.abs(sort_time_1 - sort_time_2)}')
        print(f'Percentage difference = {np.abs(sort_time_1 - sort_time_2) / ((sort_time_1 + sort_time_2)/2) * 100:.2f}%')

    
# Initialization of the array, and instance of the Sort class.
array = np.random.randint(0, 100, 10000)
sort = Sort(array)

# Bubble Sort.
bubble_sorted, bubble_sort_time = sort.bubble_sort('ascend')
#sort.bubble_sort('descend')

#Selection Sort.
select_sorted, select_sort_time = sort.selection_sort('ascend')
#sort.selection_sort('descend')

#Insertion Sort.
insert_sorted, insert_sort_time = sort.insertion_sort('ascend')

#Comparision routine:
sort.compare_sort(bubble_sort_time, insert_sort_time)
