import io
import fourierMotzkinElimination as fme
import numpy as np
import time

# For timing purposes

fileName = '/home/fritjof/git/ADM/FourierMotzkin/data/mo8.txt'
(data, variables) = io.readData(fileName)

start = time.time()
data = fme.rescaleData(data, variables[0])
data = fme.deleteRedundantRows(data)

for i in range(len(variables)):
	for j in range(i+1,len(variables)):
		if variables[j] > variables[i]:
			variables[j] -= 1
	print(data.shape)
	data = fme.rescaleData(data,j-1)
	data = fme.computeFMElimination(data, variables[i]-1) 
	data = fme.rescaleData(data, variables[0])
	data = fme.deleteRedundantRows(data)

print(data.shape)
print("Required time was: " , time.time() - start) 
