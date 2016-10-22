'''Find the minimum and maximum of an array using 3n/2 comparisons'''
def getMinMax(A):
	if len(A) == 1:
		print A[0], A[0]
	else:
		s = min(A[0], A[1])
		l = A[0] + A[1] - s
		i = 2
		while i < len(A):
			if i == len(A) - 1:
				s = min(s, A[i])
				l = max(l, A[i])
			else:
				m = min(A[i], A[i+1])
				n = A[i] +  A[i+1] - m
				s = min(s, m)
				l = max(l, n)
			i += 2
	print s, l

if __name__ == '__main__':
	A = [1, 3, 2, 5, 10, -1, 3, 9]
	getMinMax(A)

