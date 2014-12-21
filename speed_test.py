import heap
def speed_test():
    a = []
    times = 10000
    for i in xrange(times):
            heap.add(a, i)

    for i in xrange(times):
            heap.look(a)

if __name__ == '__main__':
    speed_test()
