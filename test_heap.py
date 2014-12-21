import heap
def test_print_tree(capsys):
	a = [1, 2, 3, 4, 5]
	heap.print_tree(a)

	out, err = capsys.readouterr()
	lines = out.strip().split('\n')
	print out

	assert(lines[0] == '[1]')
	assert(lines[1] == '[2, 3]')
	assert(lines[2] == '[4, 5]')

def test_balance_up(capsys):
	a = []
	heap.add(a, 1)
	heap.add(a, 2)
	heap.add(a, 4)
	heap.add(a, 3)
	heap.print_tree(a)
	out, err = capsys.readouterr()
	lines = out.strip().split('\n')

	assert(len(lines) == 3)
	assert(a == [1, 2, 4, 3])
