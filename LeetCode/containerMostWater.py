'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
class Solution(object):
	def maxArea(self, height):
		"""
        :type height: List[int]
        :rtype: int
        """
        low, high = 0, len(height)
        maxArea = 0
        while low < high:
        	maxArea = max(maxArea, min(height[low], height[high])*(high-low))
        	if height[low] < height[high]:
        		low += 1
        	else:
        		high -= 1
        return maxArea