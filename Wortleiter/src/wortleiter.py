# -*- encoding: iso-8859-15 -*-

def compareWords(x, y):
	"""
	Compares two words and returns the number of non-identical characters
	"""
	cnt = 0
	if len(x) != len(y):
		print("ERROR")
		print(x,y)
	for i in range(len(x)):
		if x[i] != y[i]:
			cnt = cnt + 1
	return cnt
	
def dfs():
	"""
	Depth-First Search
	"""
	pass



# read in word list and store a hashtable for the vertices
hashes = []
fobj = open("./resource/words.txt")
for line in fobj:
    hashes.append(line.split()[0])
fobj.close()

# Compute adjacency list for every vertex
adjazenz = [[] for i in range(len(hashes))]
for i in range(len(hashes)):
	for j in range(i, len(hashes)):
		if compareWords(hashes[i],hashes[j]) == 1:
			adjazenz[i].append(j)
			adjazenz[j].append(i)
			
# Print information about connections in the graph

print("The following nodes are isolated:")
for i in range(len(hashes)):
	if len(adjazenz[i]) == 0:
		print(hashes[i])

print("The word with most neighbors is:")
index = 0
maxLength = len(adjazenz[0])
for i in range(len(hashes)):
	if len(adjazenz[i]) > maxLength:
		maxLength = len(adjazenz[i])
		index = i
print(hashes[index],maxLength)
for j in adjazenz[index]:
	print(hashes[j])

