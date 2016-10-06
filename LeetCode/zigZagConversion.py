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
		goingDown = True
		for c in s:
			conv_string[curr_row].append(c)
			if goingDown and curr_row == (numRows - 1):
				curr_row = curr_row - 1
				goingDown = False
			elif goingDown == False and curr_row == 1:
				curr_row = 0
				goingDown = True
			elif goingDown == False and curr_row == 0:
				curr_row = max(curr_row+1, numRows-1)
				goingDown = True
			else :
				curr_row = curr_row + 1 if goingDown else curr_row + 1
		for index in range(numRows):
			print ''.join(conv_string),
