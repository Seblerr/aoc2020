input = open('input').readlines()

def treeCounter(right, down):
	index = 0
	treeCount = 0

	for line in input[::down]:
		maxIndex = line.index('\n')
		if line[index % maxIndex] == '#':
			treeCount += 1
		index += right

	return treeCount

trees1 = treeCounter(1,1)
trees2 = treeCounter(3,1)
trees3 = treeCounter(5,1)
trees4 = treeCounter(7,1)
trees5 = treeCounter(1,2)

print(trees1 * trees2 * trees3 * trees4 * trees5)
