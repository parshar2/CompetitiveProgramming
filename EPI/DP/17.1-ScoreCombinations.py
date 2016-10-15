def getNumCombinations(goal, coins):
	'''Returns number of ways of achieving goal using the given denominations in coins'''
	num_ways = [0]*(goal + 1)
	num_ways[0] = 1	#Zero can be achieved in one way by not picking any coins
	for coin in coins:
		for i in range(coin, goal+1):
			num_ways[i] += num_ways[i-coin]
	print num_ways
	return num_ways[goal]


if __name__ == '__main__':
	goal = int(raw_input().strip())
	coins = map(int, raw_input().strip().split(','))
	print getNumCombinations(goal, coins)
