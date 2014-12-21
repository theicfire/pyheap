import pytest

def print_tree(l):
    level = 0
    while True:
            amount = 2 ** level
            start = sum([2**x for x in range(level)])
            print l[start:start + amount]
            level += 1
            if start + amount >= len(l):
                    break

def parent_index(i):
    return i / 2

def look(heap):
    return heap[0]

def add(obj, value):
    obj.append(value)
    balance_up(obj, len(obj) - 1)

def balance_up(obj, icur):
    if icur <= 0:
            return

    iparent = parent_index(icur)
    if obj[icur] < obj[iparent]:
            # swap
            tmp = obj[icur]
            obj[icur] = obj[iparent]
            obj[iparent] = tmp

            balance_up(obj, iparent)

		
	
if __name__ == '__main__':
    pytest.main([__file__])
