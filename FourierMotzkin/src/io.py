import numpy as np

def readData(file):
	"""
	Read in data for Fourier-Motzkin elimination
	Output:
	data - Matrix A and vector b defining polyeder
	variables - list of variables that shall be eliminated 
	"""
	data = np.loadtxt(file,skiprows = 1)
	fileObject = open(file)
	for line in fileObject:
		variables = np.array(map(int,line.split()))
		break
	return (data, variables)
		
