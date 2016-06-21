import numpy as np

def parseInput(inputFile):
	"""
	Simple parser to read in the given instance of the min cost flow
	problem.
	
	Output:
	b - Bedarfe der Knoten
	A - arcs of the graph, each line corresponds to an arc, the entrys
	are: startNode, endNode, lowerBound, upperBound, cost, flow value,
	flag for L,T,U (-1,0,1)
	"""
	inputLines = open(inputFile, 'r')
	
	for i in inputLines:
		words = i.split()
		if words[0] == 'c':
			continue
		elif words[0] == 'p':
			if words[1] != "min":
				print('ERROR NOT A MINIMIZATION PROBLEM!')
			b = np.zeros((int(words[2]),1))
			A = np.zeros((int(words[3]),7))
			cnt = 0
		elif words[0] == 'n':
			b[int(words[1])-1] = int(words[2])
		elif words[0] == 'a':
			A[cnt,:5] = map(int, words[1:])
			cnt += 1
	return (b,A)
