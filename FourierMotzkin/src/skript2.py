import io
import fourierMotzkinElimination as fme
import numpy as np
import time

# For timing purposes

fileName = '/home/fritjof/git/ADM/FourierMotzkin/data/mo9.txt'
(data, variables) = io.readData(fileName)
#print(data)

start = time.time()
for j in variables:
	#print(j)
	data = fme.rescaleData(data,j-1)
	data = fme.computeFMElimination(data, j-1) 
	#print(data)
print("Required time was: " , time.time() - start) 
