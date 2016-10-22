'''Search a sorted array containing distinct elements for A[i] = i'''
def searchArray(a):
	l, r = 0, len(a) - 1
	while l <= r:
		m = l + (r - l)/2
		if A[m] == m:
			return m
		elif A[m] > m:
			r = m - 1
		else:
			l = m + 1
	return -1

if __name__ == '__main__':
	A = [-2, 0, 3, 4, 6, 7, 9]
	print searchArray(A)
