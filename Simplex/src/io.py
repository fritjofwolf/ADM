import numpy as np

def parseSIFFile(fileinput):
	"""
	Reads in a linear program instance in mps format
	"""
	(m,n) = extractDimensions(fileinput)
	data = open(fileinput, 'r')
	
	# Skipping comments
	for line in data:
		if line.split()[0] == "ROWS":
			break
	
	# Defining Rows
	rows = {}		
	cnt = 0
	for line in data:
		words = line.split()
		if words[0] == "COLUMNS":
			break
		if words[1] != "COST":
			rows[words[1]] = (words[0],cnt)
			cnt += 1
		else:
			rows[words[1]] = (words[0],-1)
	
	# Defining variables
	variables = {}
	cntVars = 0
	c = np.zeros(n)
	A = np.zeros((m,n))
	for line in data:
		words = line.split()
		if words[0] == "RHS":
			break
		if words[0] not in variables:
			variables[words[0]] = cntVars
			cntVars += 1
		if len(words) > 3:
			if words[1] == "COST":
				c[variables[words[0]]] = int(words[2])
			else:
				A[rows[words[1]][1],variables[words[0]]] = int(words[2])
			if words[3] == "COST":
				c[variables[words[0]]] = int(words[4])
			else:
				A[rows[words[3]][1],variables[words[0]]] = int(words[4])
		else:
			if words[1] == "COST":
				c[variables[words[0]]] = int(words[2])
			else:
				A[rows[words[1]][1],variables[words[0]]] = int(words[2])
				
	# Defining RHS	
	b = np.zeros((m,1))
	for line in data:
		words = line.split()
		if words[0] == "BOUNDS":
			break
		if len(words) > 3:
			b[rows[words[1]][1]] = int(words[2])
			b[rows[words[3]][1]] = int(words[4])
		else:
			b[rows[words[1]][1]] = int(words[2])
			
	print(c)
	print(b)
	print(A)
	return (A,b,c)
	
def extractDimensions(fileinput):
	"""
	Goes through a .sif file and computes the number of equalities and
	variables
	"""
	data = open(fileinput,'r')
	
	return (3,3)
	
def normalizeLP():
	"""
	Convert a given LP to the normalized form which
	is expected by the Simplex algorithm
	"""
	pass
