'''Find the duplicate and missing element in an array of size n where only one element is repeating'''
def findDupMiss(A):
	n = len(A) #All elements are between 0 and n-1
	xor = 0
	for num in A:
		xor ^= num
	for num in range(n):
		xor ^= num


	lsb = xor & ~(xor-1)
	d, m = 0, 0
	for num in A:
		if num & lsb:
			d ^= num
		else:
			m ^= num

	for num in range(n):
		if num & lsb:
			d ^= num
		else:
			m ^= num
	print d, m

if __name__ == '__main__':
	A = [0, 1, 2, 4, 2]
	findDupMiss(A)

