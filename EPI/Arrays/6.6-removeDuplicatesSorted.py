def removeDuplicates(a):
	'''remove all duplicate elements from a sorted array a and return size of valid array'''
	i, j = 0, 1
	l = len(a)
	while j < l:
		if a[j] != a[i]:
			i += 1
			a[i] = a[j]
			j += 1
		else:
			j += 1
	return i + 1

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(','))
	size = removeDuplicates(a)
	print 'Valid size: ', size
	print 'Modified array: ', a