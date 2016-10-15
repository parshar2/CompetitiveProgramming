def getNextLargestPermutation(a):
	'''Get the next largest permutation after a'''
	i = len(a) - 1
	l = len(a)
	while i > 0 :
		if a[i-1] < a[i]:
			break
		i = i -1
	if i == 0:
		return
	else :
		next_largest_index = i
		for j in range(i+1, len(a)):
			if a[j] > a[i] and a[j] < a[next_largest_index]:
				next_largest_index = j
		#swap i and next_largest_index and sort (i+1:l)
		temp = a[i-1]
		a[i-1] = a[next_largest_index]
		a[next_largest_index] = temp
		a[i:] = sorted(a[i:])

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(','))
	getNextLargestPermutation(a)
	print a
