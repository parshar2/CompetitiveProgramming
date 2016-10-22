'''Find the position of the smallest element in a descending array that is cyclically sorted'''
def findMin(a):
	l, r = 0, len(a) - 1
	while l < r:
		m = l + (r - l)/2
		if a[m] > a[r]:
			l = m + 1
		else:
			r = m
	return a[l]

'''Search for an element k in a cyclically sorted array'''
def searchElem(a, k):
	l, r = 0, len(a) - 1
	while l <= r:
		m = l + (r - l)/2
		if a[m] == k:
			return m
		if a[m] <= a[r]:
			if k > a[m] and k <= a[r]:
				l = m + 1
			else:
				r = m - 1
		else:
			if k < a[m] and k >= a[l]:
				r = m - 1
			else:
				l = m + 1
	return -1


if __name__ == '__main__':
	A = [378, 478, 550, 631, 5, 10, 20, 50 ,100, 103, 203, 220, 234, 279, 368]
	print searchElem(A, 220)