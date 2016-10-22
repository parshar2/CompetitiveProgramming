'''Search for an element k in a 2D array whose rows and columns are sorted in increasing sorted order'''
def findK(A, k):
	m = len(A)
	n = len(A[0])
	i, j = 0, n - 1
	while j >= 0 and i < m:
		if A[i][j] == k:
			print i, j
			return True
		elif k > A[i][j]:
			i += 1
		else:
			j -= 1
	return False

if __name__ == '__main__':
	A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [7, 8, 9, 10]]
	k = int(raw_input())
	print findK(A, k)

