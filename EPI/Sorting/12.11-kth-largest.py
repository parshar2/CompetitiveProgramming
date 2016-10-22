'''Find the kth largest element in an unsorted array with O(n) expected time'''
from random import randint

def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def sortAboutPivot(A, pivot):
	swap(A, 0, pivot)
	i = 0
	for j in range(1, len(A)):
		if A[j] <= A[0]:
			i += 1
			swap(A, i, j)
	swap(A, 0, i)
	return i + 1




def getKthLargest(A, k):
	pivot = randint(0, len(A) - 1)
	n = sortAboutPivot(A, pivot)
	if n == k:
		return A[n - 1]
	elif k < n:
		return getKthLargest(A[:n-1], k)
	else:
		return getKthLargest(A[n:], k - n)



if __name__ == '__main__':
	A = [1, 10, 9, 4, 8, 6, 2, 0, 10, -10, 30, 20, 30, 100]
	print sorted(A)
	k = int(raw_input())
	print getKthLargest(A, k)

