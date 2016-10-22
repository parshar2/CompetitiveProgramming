'''Given an array with ascending followed by descending sequence, 
find the maximum element in A. Note ascending is different 
from strictly ascending'''



'''Given an array with strictly ascending followed by strictly descending sequence, 
find the maximum element in A.'''
def findMaxSASD(a): #1st attempt: works better if you cannot assume that sequence is well behaved
	l, r = 0, len(a) - 1
	max_elem = -1
	while l <= r:
		m = l + (r-l)/2
		if l == r:
			max_elem = a[l]
			break
		elif r - l == 1:
			max_elem = max(a[l], a[r])
			break
		else:
			if a[m] > a [m-1] and a[m] > a[m+1]:
				max_elem = a[m]
				break
			elif a[m] > a[m-1]:
				l = m + 1
			else:
				r = m - 1
	return max_elem

def findMaxSASD1(a): #After reading from CLRS
	l, r = 0, len(a) - 1
	while l < r:
		m = l + (r-l)/2
		if a[m] > a[m+1]:
			r = m
		else:
			l = m + 1
	return a[l]


'''Given an array with strictly ascending followed by descending sequence, 
find the maximum element in A.'''
def findMaxSAD(a):
	l, r = 0, len(a) - 1
	while l < r:
		m = l + (r-l)/2
		if a[m] >= a[m+1]:
			r = m
		else:
			l = m + 1
	return a[l]


if __name__ == '__main__':
	SASD = [-5, -3, -2, 0, 5, -1, -5, -9, -10]
	#SAD = [-5, -3, -2, 0, 0, 0, 0, -1, -5, -5, -9, -10, -10]

	print findMaxSASD1(SASD)



