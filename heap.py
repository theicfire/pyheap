import pytest

class HeapError(Exception):
    pass

def print_tree(l):
    level = 0
    while True:
            amount = 2 ** level
            start = sum([2**x for x in range(level)])
            print l[start:start + amount]
            level += 1
            if start + amount >= len(l):
                    break

def new():
    return ['heap']

def parent_index(i):
    return i / 2

def look(heap):
    return heap[1]

def add(obj, value):
    obj.append(value)
    balance_up(obj, len(obj) - 1)

def balance_up(obj, icur):
    if icur <= 1:
        return

    iparent = parent_index(icur)
    if obj[icur] < obj[iparent]:
        (obj[icur], obj[iparent]) = (obj[iparent], obj[icur])
        balance_up(obj, iparent)

def remove(heap):
    if len(heap) <= 1:
        raise HeapError("Can't remove from empty heap")
    ret = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    balance_down(heap, 1)
    return ret

def min_child(heap, icur):
    ileft = icur * 2
    iright = icur * 2 + 1
    if ileft >= len(heap):
        return icur
    imin_child = ileft
    if iright < len(heap):
        imin_child = ileft if heap[ileft] <= heap[iright] else iright
    if heap[icur] <= heap[imin_child]:
        return icur
    return imin_child

def balance_down(heap, icur):
    assert(icur >= 1)
    if icur * 2 >= len(heap):
        return

    ibetter = min_child(heap, icur)
    if ibetter == icur:
        return
    (heap[icur], heap[ibetter]) = (heap[ibetter], heap[icur])
    balance_down(heap, ibetter)

if __name__ == '__main__':
    pytest.main()
