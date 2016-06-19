import io
import fourierMotzkinElimination as fme
import numpy as np

# for printing purposes

fileName = '/home/fritjof/git/ADM/FourierMotzkin/data/mo3.txt'
(data, variables) = io.readData(fileName)
print(data)

for j in variables:
	#print(j)
	data = fme.computeFMElimination(data, j-1) 
	print(data)
