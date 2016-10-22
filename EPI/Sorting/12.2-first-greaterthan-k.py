'''Search sorted array for the first element greater than k'''
def findLargerElement(a, k):
	l, r = 0, len(a) - 1
	while l <= r:
		m = l + (r-l)/2
		if k > a[m]:
			l = m + 1
		elif k < a[m]:
			r = m - 1
		else:
			l = m + 1
			if m == r or a[m] != a[m+1]:
				break
	if l >= len(a):
		return -1
	else:
		return a[l]

def findLargerElement2(a, k):
	l, r = 0, len(a) - 1
	ind = -1
	while l <= r:
		m = l + (r-l)/2
		if a[m] > k:
			ind = m
			r = m - 1
		else:
			l = m + 1
	return a[ind]

if __name__ == '__main__':
	a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
	k = int(raw_input())
	print findLargerElement(a, k)


