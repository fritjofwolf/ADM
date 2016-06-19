import io
import fourierMotzkinElimination as fme
import numpy as np

fileName = '/home/fritjof/git/ADM/FourierMotzkin/data/mo9.txt'
(data, variables) = io.readData(fileName)
print(data.shape[0])

for j in variables:
	#print(j)
	data = fme.computeFMElimination(data, j-1) 
	print(data.shape[0])
