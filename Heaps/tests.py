"""Series of simple tests used to check the correctness of various heap implementations."""

import argparse
from maxheap import MaxHeap
from minheap import MinHeap

def test_heap(heap_class):
    def test1():
        """Tests when the heap is empty."""
        heap = heap_class()
        assert heap.get_max() == "Empty max heap."
        assert heap.get_min() == "Empty max heap."
        assert heap.remove_min() == "Empty max heap."
        assert heap.remove_max() == "Empty max heap."
        assert len(heap) == 0
        print("passed!")

    def test2():
        """Tests when the max heap contains only one element."""
        heap = heap_class()
        heap.insertion(10)
        assert heap.get_max() == 10
        assert heap.get_min() == 10
        assert heap.remove_min() == 10
        assert heap.remove_max() == "Empty max heap."
        assert len(heap) == 0
        print("passed!")

    def test3():
        """Tests when the max heap contains multiple elements, but inserted into the heap in ascending order."""
        heap = heap_class()
        heap.insertion(50)
        heap.insertion(40)
        heap.insertion(30)
        heap.insertion(20)
        heap.insertion(10)
        assert len(heap) == 5
        assert heap.get_max() == 50
        assert heap.get_min() == 10
        assert heap.remove_min() == 10
        heap.insertion(10) # Lets put 10 back into the heap.
        assert heap.remove_max() == 50
        print("passed!")

    def test4():
        """Tests when the max heap contains multiple elements, but inserted into the heap in descending order."""
        heap = heap_class()
        heap.insertion(10)
        heap.insertion(20)
        heap.insertion(30)
        heap.insertion(40)
        heap.insertion(50)
        assert len(heap) == 5
        assert heap.get_max() == 50
        assert heap.get_min() == 10
        assert heap.remove_min() == 10
        heap.insertion(10) # Lets put 10 back into the heap.
        assert heap.remove_max() == 50
        print("passed!")

    def test5():
        """Tests when the max heap contain multiple elements, and some elements are duplicated."""
        heap = heap_class()
        heap.insertion(30)
        heap.insertion(30)
        heap.insertion(40)
        heap.insertion(60)
        heap.insertion(10)
        assert len(heap) == 5
        assert heap.get_max() == 60
        assert heap.get_min() == 10
        assert heap.remove_min() == 10
        heap.insertion(10) # Lets put 10 back into the heap.
        assert heap.remove_max() == 60
        print("passed!")

    print(f"Test 1: When {heap_class.__name__} is empty.")
    test1()
    print(f"Test 2: When {heap_class.__name__} only contains one element.")
    test2()
    print(f"Test 3: When {heap_class.__name__} contains multiple elements, ascending order.")
    test3()
    print(f"Test 4: When {heap_class.__name__} contains multiple elements, descending order.")
    test4()
    print(f"Test 5: When {heap_class.__name__} contains multiple elements, some elements are duplicated.")
    test5()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("heap_type", help="The type of heap to test. Choices are 'min' or 'max'.")
    args = parser.parse_args()

    if args.heap_type == "MinHeap":
        test_heap(MinHeap)
    elif args.heap_type == "MaxHeap":
        test_heap(MaxHeap)
    else:
        print(f"No heap class named {args.heap_type}")


