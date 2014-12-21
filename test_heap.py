import pytest
import heap
import random

def test_print_tree(capsys):
	a = [1, 2, 3, 4, 5]
	heap.print_tree(a)

	out, err = capsys.readouterr()
	lines = out.strip().split('\n')
	print out

	assert(lines[0] == '[1]')
	assert(lines[1] == '[2, 3]')
	assert(lines[2] == '[4, 5]')

def test_add(capsys):
	a = [-float('inf')]
	heap.add(a, 1)
	heap.add(a, 2)
	heap.add(a, 4)
	heap.add(a, 3)
	heap.print_tree(a)
	out, err = capsys.readouterr()
	lines = out.strip().split('\n')

	assert(len(lines) == 3)
	assert(a == [-float('inf'), 1, 2, 4, 3])

def test_heap():
	a = [-float('inf'), 4]
        assert(heap.look(a) == 4)

def test_add2():
	a = [-float('inf')]
	heap.add(a, 1)
	heap.add(a, 3)
	heap.add(a, 2)
	assert(a == [1, 3, 2])

def test_add2():
	a = [-float('inf')]
	heap.add(a, 1)
	heap.add(a, 3)
	heap.add(a, 2)
	assert(a == [-float('inf'), 1, 3, 2])

def test_remove():
        a = [-float('inf')]
        with pytest.raises(heap.HeapError):
            heap.remove(a)

        a = [-float('inf'), 1, 2, 3, 4, 5]
        assert(heap.remove(a) == 1)
        assert(a == [-float('inf'), 2, 4, 3, 5])

def test_all():
    length = 5000
    unsorted_list = [int(random.random() * 10000) for x in xrange(length)]
    sorted_list = sorted(unsorted_list)
    heap_sorted = []

    my_heap = [-float('inf')]
    for i in xrange(length):
        heap.add(my_heap, unsorted_list[i])

    while len(my_heap) > 1:
        heap_sorted.append(heap.remove(my_heap))

    assert heap_sorted == sorted(unsorted_list)
