import ordered_list, unordered_list
import random

def main(obj_1, obj_2):
    for x in range(5):
        r1 = random.randint(0,20)
        obj_1.ordered_add(r1)
        obj_2.append(r1)
    print(obj_1.print_fn())
    print(obj_2.print_fn())
obj_1 =  ordered_list.LinkedList()
obj_2 = unordered_list.LinkedList()

main(obj_1, obj_2)

