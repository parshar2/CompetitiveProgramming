import math
n = int(raw_input().strip())

def getReverse(n):
	reverse_n = 0
	while n!= 0:
		reverse_n = reverse_n*10 + n%10
		n = n/10
	return reverse_n

def checkPalindrome(n):
	num_digits = int(math.log10(n)) + 1
	left_divisor = 10**(num_digits-1)
	for i in range(0, num_digits/2):
		right_digit = n%10
		left_digit = n/left_divisor
		if right_digit != left_digit:
			return False
		n = n%left_divisor
		n = n/10
		left_divisor /= 100
	return True

print n - getReverse(n) == 0
print checkPalindrome(n)