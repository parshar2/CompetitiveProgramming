'''Find for the kth element in two sorted arrays'''
import math
def getKthElement(A, B, k):
	if len(A) == 0:
		return B[k-1]
	if len(B) == 0:
		return A[k-1]
	if k == 1:
		return min(A[0], B[0])
	x = min(len(A), k/2 + k%2)
	y = k - x
	if A[x-1] < B[y-1]:
		return getKthElement(A[x:], B, k - x)
	elif A[x -1] > B[y-1]:
		return getKthElement(A, B[y:], k - y)
	else:
		return A[x-1]


if __name__ == '__main__':
	A = [1, 3, 5, 7, 9, 11]
	B = [4]
	k = int(raw_input())
	print getKthElement(A, B, k)

