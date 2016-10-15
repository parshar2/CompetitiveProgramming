def findMaxProfit(a):
	'''Find maximum profit that can be made by buying and selling any number of times
	over a given time period a'''
	l = len(a)
	max_profit = [0]*(l+1) # stores max profit that can be made over subarrays
	for i in range(l-1, -1, -1):
		share_min_value = a[i]
		for j in range(i+1, l):
			if a[j] > share_min_value:
				profit = a[j] - share_min_value + max_profit[j+1]
				if profit > max_profit[i]:
					max_profit[i] = profit
			else:
				share_min_value = a[j]
	return max_profit[0]

if __name__ == '__main__':
	a = map(int, raw_input().strip().split(','))
	print 'Max profit: ', findMaxProfit(a)

