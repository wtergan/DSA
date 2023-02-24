import numpy as np
from sorting_algos import bubble_sort, selection_sort, insertion_sort

array = np.random.randint(0, 100, 1000)

def Bubble(array, order):
    bubble = bubble_sort.BubbleSort(array)
    if order == 'ascend':
        sort, time = bubble.sort_ascend()
        print(f'Sorted array:\n{sort}\nExecution time: {time} seconds.')

    elif order == 'descend':
        sort, time = bubble.sort_descend()
        print(f'Sorted array:\n{sort}\nExecution time: {time} seconds.')

def Select(array, order):
    select = selection_sort.SelectionSort(array)
    if order == 'ascend':
        sort, time = select.sort_ascend()
        print(f'Sorted array:\n{sort}\nExecution time: {time} seconds.')

    elif order == 'descend':
        sort, time = select.sort_descend()
        print(f'Sorted array:\n{sort}\nExecution time: {time} seconds.')


def Insert(array, order):
    insert = insertion_sort.InsertionSort(array)
    if order == 'ascend':
        sort, time = insert.sort_ascend()
        print(f'Sorted array:\n{sort}\nExecution time: {time} seconds.')

    elif order == 'descend':
        sort, time = insert.sort_descend()
        print(f'Sorted array:\n{sort}\nExecxution time: {time} seconds.')

Insert(array, 'ascend')
