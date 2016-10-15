def removeElement(a, k):
	'''Removes all occurences of k from array a and returns the valid size of a'''
	i, j = 0, 0
	l = len(a)
	num_k = 0
	while j < l:
		if a[j] != k:
			a[i] = a[j]
			i += 1
			j += 1
		else:
			num_k += 1
			j += 1
	return l - num_k

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(',')) #Assuming that input is separated by ,
	k = int(raw_input().strip())
	print "Valid array size: ", removeElement(a, k)
	print 'Modified array:' , a