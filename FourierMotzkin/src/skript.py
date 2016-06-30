import io
import fourierMotzkinElimination as fme
import numpy as np

# for printing purposes

fileName = '/home/fritjof/git/ADM/FourierMotzkin/data/moOpt.txt'
(data, variables) = io.readData(fileName)

data = fme.rescaleData(data,variables[0])
data = fme.deleteRedundantRows(data)

for i in range(len(variables)):
	# Update indices
	for j in range(i+1,len(variables)):
		if variables[j] > variables[i]:
			variables[j] -= 1
	data = fme.rescaleData(data,variables[i]-1)
	data = fme.computeFMElimination(data, variables[i]-1) 

	data = fme.rescaleData(data,variables[i]-1)
	data = fme.deleteRedundantRows(data)

print(fme.rescaleData(data,0))
