def isWinnable(a):
	'''Takes an array a and checks whether the end state is reachable'''
	curr_state, max_reached_state = 0, 0
	while curr_state <= max_reached_state:
		max_reached_state = max(max_reached_state, curr_state + a[curr_state])
		if max_reached_state >= len(a) - 1:
			return True
		curr_state += 1
	return False

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(','))
	print isWinnable(a)
