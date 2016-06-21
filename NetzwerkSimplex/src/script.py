import io
import netzwerkSimplex as ns
import numpy as np

# Read in data
fileName = '/home/fritjof/git/ADM/NetzwerkSimplex/data/testExample1.txt'
(arcs, bedarfe) = io.parseInput(fileName))
print("Reading Input completed.")

# Network Simplex algorithm
createFirstInstance(arcs, bedarfe)
while True:
	computeNodeCosts()
	a = checkOptimality()
	if a == -1:
		break
	#Augmenting()
	updateTreeSolution()
print("Network simplex algorithm completed")

# Check if solution is feasible for old instance
if sum(arcs[-len(bedarfe)+1:,5]): # assuming that bedarfe contains n+1 nodes
	print("The minimum costs are:", np.inner(np.transpose(arcs[:,4]),np.transpose(arcs[:,5])))
	print("The flow optimal flow is:", arcs[:,[0,1,5]])
else:
	print("There is no solution.")
