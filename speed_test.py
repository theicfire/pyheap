import heap
import random

def speed_test():
    length = 90000
    unsorted_list = [int(random.random() * 10000) for x in xrange(length)]
    sorted_list = sorted(unsorted_list)
    heap_sorted = []

    my_heap = [-float('inf')]
    for i in xrange(length):
        heap.add(my_heap, unsorted_list[i])

    while len(my_heap) > 1:
        heap_sorted.append(heap.remove(my_heap))

    assert heap_sorted == sorted(unsorted_list)

if __name__ == '__main__':
    speed_test()
