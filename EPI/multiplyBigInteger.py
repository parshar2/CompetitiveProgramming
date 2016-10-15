def addNumbers(s1, s2):
	'''Add two large numbers s1 and s2 which are represented as strings'''
	s = ''
	i, j = len(s1) -1, len(s2) - 1
	carry = 0
	while i >=0 or j >= 0:
		a1, a2 = 0, 0
		if i >= 0:
			a1 = int(s1[i])
		if j >= 0:
			a2 = int(s2[j])
		s = str((a1+a2+carry)%10) + s
		carry = (a1 + a2 + carry)/10
		i -= 1;
		j -= 1
	if carry != 0:
		s = str(carry) + s
	return s

def multiplyByDigit(s, d):
	'''Multiply number s by digit d'''
	i = len(s) - 1
	result = ''
	carry = 0
	while i >= 0:
		result = str((d*int(s[i]) + carry)%10) + result
		carry = (d*int(s[i]) + carry)/10
		i -= 1
	if carry != 0:
		result = str(carry) + result
	return result

def multiplyNumbers(s1, s2):
	i = len(s2) -1
	result = ''
	while i>= 0:
		curr_mult = multiplyByDigit(s1, int(s2[i])) + '0'*(len(s2) - 1 - i) 
		result = addNumbers(result, curr_mult)
		i -= 1
	return result


if __name__ == '__main__':
	a1 = raw_input().strip()
	a2 = raw_input().strip()
	print "Sum is :", addNumbers(a1, a2)
	print "Multiplication is : " , multiplyNumbers(a1, a2)
