def findLongestIncreasingSubsequence(a):
	'''returns a tuple (x,y) containing the indexes of the longest increasing subsequence'''
	i, j, max_i, max_j = 0, 1, 0, 0
	l = len(a)
	while j < l:
		if a[j] < a[j-1]:
			i = j
		j += 1
		if j - i > max_j - max_i + 1:
			max_i, max_j = i, j - 1
	return (max_i, max_j)

if __name__ == "__main__":
	a = map(int, raw_input().strip().split(','))
	print findLongestIncreasingSubsequence(a)
