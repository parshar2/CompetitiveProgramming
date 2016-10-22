def computeLenenshteinDistance(a, b):
	'''Computes the number of edits it takes to transform a into b via insertions, 
	deletions and substitutions'''
	len_a = len(a)
	len_b = len(b)
	distances = range(len_b+1)
	print distances
	for i in range(len_a-1, -1, -1):
		prev_i_1_j_1 = distances[len_b]
		distances[len_b] = len_a - i
		for j in range(len_b-1, -1, -1):
			prev_i_j = distances[j]
			if a[i] == b[j]:
				distances[j] = prev_i_1_j_1
			else:
				distances[j] = 1 + min(prev_i_1_j_1, distances[j+1], distances[j])
			prev_i_1_j_1 = prev_i_j
	print distances
	return distances[0]

if __name__ == '__main__':
	a = raw_input().strip()
	b = raw_input().strip()
	print computeLenenshteinDistance(a, b)
