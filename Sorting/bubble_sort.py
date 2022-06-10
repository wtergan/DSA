'''Repeatedly swapping the adjacent elements if they are in the wrong order'''
def bubbleSort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def forBubble(arr):
    for i in range(len(arr)):
        for x in range(len(arr)-1)
print(bubbleSort([5,4,7,3,1]))
print(bubbleSort([3,0,4,34,-8]))
print(bubbleSort([64,34,25,12,22,11,90]))
