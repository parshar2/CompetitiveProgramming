#Details about the problem can be found here: https://leetcode.com/problems/the-skyline-problem/
class Solution(object):
	def getSkyline(self, buildings):
		"""
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
        	return []
        elif len(buildings) == 1:
        	return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

