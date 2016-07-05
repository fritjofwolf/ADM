from numpy import *
from numpy.linalg import *
import time

def computePhaseII(A, b, c, B, N):
	"""
	Computes the optimal solution of the linear program
	max c^T*x, Ax = b, x >= 0
	using the revised Simplex algorithm
	"""
	basis = A[:,B]
	inverse = inv(basis)
	b_bar = dot(inverse, b)
	while True:
		# BTRAN
		shadowPrice = dot(c[B].T,inverse)
		
		# PRICE
		reduced = c[N].T - dot(shadowPrice, A[:,N])
		if all(reduced <= 0):
			x = zeros(c.shape[0])
			x[B] = dot(inverse, b)
			print("Eine optimale Basisloesung ist",x)
			print("Optimal value is",dot(x.T,c))
			return x
		else: # steepest edge pivoting rule
			s = argmax(reduced)
			
		# FTRAN
		d = dot(inverse,A[:,N[s]])
		
		# CHUZR
		if all(d <= 0):
			return -1
		else:
			l0 = min([b_bar[i] / float(d[i]) for i in range(b.shape[0]) if d[i] > 0])
			for i in range(b.shape[0]): # todo: avoid cycling by using lexographic rule
				if d[i] != 0 and b_bar[i] /float(d[i]) == l0:
					r = i
					break
		# WRETA
		N[s],B[r] = B[r], N[s]
		basis = A[:,B]
		inverse = inv(basis) # todo: use eta vectors
		b_bar = dot(inverse, b)


def computePhaseI(A, b, c):
	"""
	Computes a valid basis that can be used in phase II or decides that
	the polyeder has no solution or is unbounded
	"""
	pass
