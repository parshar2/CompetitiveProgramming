'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''

class Solution(object):
	def convert(self, s, numRows):
		conv_string = [[] for _ in range(numRows)]
		curr_row = 0 #row data needs to be added to
		charIndex = 0
		while charIndex < len(s):
			for i in range(0, numRows):
				if charIndex >= len(s):
					break
				conv_string[i].append(s[charIndex])
				charIndex += 1
			for i in range (numRows - 2, 0, -1):
				if charIndex >= len(s):
					break
				conv_string[i].append(s[charIndex])
				charIndex += 1
		retString = ''
		for string in conv_string:
			retString += ''.join(string)
		return retString

