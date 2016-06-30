import numpy as np

def computeFMElimination(data, var):
	"""
	Computes the Fourier-Motzkin elimination
	Input:
	data - matrix A and vector b (last entry of each line)
	var - variable that shall be eliminated
	Output:
	matrix - new matrix D and vector d
	"""
	# Partionate index set
	Z,P,N = [],[],[]
	for i in range(data.shape[0]):
		if data[i,var] == 0:
			Z.append(i)
		elif data[i,var] > 0:
			P.append(i)
		else:
			N.append(i)
			
	# Create new matrix
	r = len(Z) + len(P)*len(N)
	D = np.zeros((r,data.shape[1]))
	cnt = 0
	
	# Computing new matrix entries
	for i in Z:
		D[cnt,:] = data[i,:]
		cnt += 1
		
	for i in N:
		for j in P:
			 D[cnt,:] = data[i,:] + data[j,:]
			 cnt += 1
	sindizes = range(data.shape[1])
	sindizes.remove(var)
	return D[:,sindizes]
	#return D
	
def rescaleData(data, var):
	"""
	Rescaling every line of the matrix A and vector b with 1 / abs(a.var)
	to make the computation of the Fourier-Motzkin elimination more
	efficient
	Input:
	data - matrix A and vector b (last entry of each line)
	var - variable that shall be eliminated
	Output:
	matrix - new matrix D and vector d
	"""
	for i in range(data.shape[0]):
		if data[i,var]:
			data[i,:] = data[i,:] / np.abs(data[i,var])
	return data
	
	
def deleteRedundantRows(data):
	# Delete zero rows
	indexList = []
	for i in range(data.shape[0]):
		for j in range(data.shape[1]-1):
			if data[i,j] != 0:
				indexList.append(i)
				break
		else:
			if data[i,-1] < 0:
				indexList.append(i)
	data = data[indexList,:]
	
	# Delete rows that appear more than one time
	indexList = [0]
	data = data[data[:,-1].argsort(),:]
	for i in range(1,data.shape[0]):
		for j in range(data.shape[1]):
			if data[i,j] != data[i-1,j]:
				indexList.append(i)
				break
	return data[indexList,:]

