'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordmap = {}
        lindex, maxlen, currlen = 0, 0, 0
        for index, c in enumerate(s):
        	if c in wordmap:
        		indexc = wordmap.get(c)
        		while lindex <= indexc :
        			wordmap.pop(s[lindex], None)
        			lindex += 1
        		currlen = index - indexc
        	else:
        		currlen += 1
        	wordmap[c] = index
        	if currlen > maxlen:
        		maxlen = currlen
        return maxlen

