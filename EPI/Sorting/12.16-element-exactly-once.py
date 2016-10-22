'''In an array, all elements appear three times except one, find that element'''
def findLonelyElement(A):
	ones, twos = 0, 0
	for i in A:
		next_ones = ones & ~i | i & ~ones & ~twos
		next_twos = ones & i | twos & ~i
		ones, twos = next_ones, next_twos
	print ones

if __name__ == '__main__':
	A = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3]
	findLonelyElement(A)