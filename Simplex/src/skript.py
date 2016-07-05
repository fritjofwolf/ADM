import io
from numpy import *
import simplex

#fileinput = "/home/fritjof/git/ADM/Simplex/data/test.sif"
#io.parseSIFFile(fileinput)

#A = array([[3,-2,0,1,0,0],[2,0,1,0,1,0],[1,3,-2,0,0,1]])
#b = array([3,4,6])
#c = array([1,1,-1,0,0,0])
#B = [3,4,5]
#N = [0,1,2]


A = array([[1,0,1,0,0,0],[2,1,0,1,0,0],[-1,1,0,0,1,0],[0,3,0,0,0,1]])
b = array([4,10,5,20])
c = array([1,2,0,0,0,0])
B = [2,3,4,5]
N = [0,1]
simplex.computePhaseII(A,b,c,B,N)
