'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Loop will check for longest palindromic substring centered at i
        longest = 0
        longest_seq = ''
        for index, c in enumerate(s):
    		len_pal = 1
    		lindex, rindex = index - 1, index + 1
    		while lindex >= 0 and rindex < len(s) and s[lindex] == s[rindex]:
    			len_pal += 2
    			lindex -= 1
    			rindex += 1
    		if len_pal > longest:
    			longest = len_pal
    			longest_seq = s[lindex+1:rindex]
    		len_pal = 0
    		lindex, rindex = index - 1, index
    		while lindex >= 0 and rindex < len(s) and s[lindex] == s[rindex]:
    			len_pal += 2
    			lindex -= 1
    			rindex += 1
    		if len_pal > longest:
    			longest = len_pal
    			longest_seq = s[lindex+1:rindex]
        return longest_seq