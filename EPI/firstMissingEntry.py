def swap(a, i, j):
	'''swap elements at position i and j'''
	a[i] = a[i]^a[j]
	a[j] = a[i]^a[j]
	a[i] = a[i]^a[j]

def findSmallestMissingEntry(a):
	'''Find smallest missing positive entry from a'''
	i = 0
	while i < len(a):
		if a[i] == (i + 1) or a[i] <= 0 or a[i] > len(a):
			i += 1
		else:
			if a[a[i] - 1] != a[i] :
				swap(a, i, a[i]-1)
			else:
				i += 1
	for i, num in enumerate(a):
		if num != (i+1):
			return i + 1
	return len(a) + 1

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(','))
	print 'Smallest missing entry: ', findSmallestMissingEntry(a)


 

