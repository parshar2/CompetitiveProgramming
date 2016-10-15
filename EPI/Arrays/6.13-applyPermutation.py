def applyPermutation(a, p):
	'''Apply permutation p to array a'''
	i = 0
	l = len(a)
	while i < l:
		temp = a[i]
		j = i
		while p[j] != i:
			a[j] = a[p[j]]
			old_j = j
			j = p[j]
			p[old_j] = old_j
		a[j] = temp
		p[j] = j
		i += 1


if __name__ == "__main__":
	a = map(int, raw_input().strip().split(','))
	p = map(int, raw_input().strip().split(','))
	applyPermutation(a, p)
	print a


