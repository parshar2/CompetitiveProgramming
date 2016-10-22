'''Search a sorted array for the first occurence of k'''
def searchArray(a, k):
	l, r = 0, len(a) - 1
	while l<= r:
		m = l + (r-l)/2
		if k < a[m]:
			r = m - 1
		elif k > a[m]:
			l = m + 1
		else:
			if m == l or a[m] != a[m-1]:
				return m
			else:
				r = m - 1
	return -1

def searchArray2(a, k):
	l, r = 0, len(a) - 1
	ind = -1
	while l<= r:
		m = l + (r-l)/2
		if k < a[m]:
			r = m - 1
		elif k > a[m]:
			l = m + 1
		else:
			ind = m
			r = m - 1
	return ind

if __name__ == '__main__':
	a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
	k = 285
	print searchArray2(a, k)