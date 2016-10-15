def computeBinomial(n, k):
	'''Compute n choose k without overflow'''
	binomial = [0]*(k+1)
	binomial[0] = 1
	for i in range(1, n+1):
		prev = binomial[0]
		binomial[0] = 1
		for j in range(1, min(i,k)+1):
			curr = binomial[j]
			binomial[j] = curr + prev
			prev = curr
	return binomial[k]

if __name__ == '__main__':
	n = int(raw_input())
	k = int(raw_input())
	print computeBinomial(n, k)


