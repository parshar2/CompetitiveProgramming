''' Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} #mapping from value to index in array
        for index, num in enumerate(nums):
        	if target - num in hashmap:
        		return [hashmap.index(target - num), index]
        	else:
        		hashmap[num] = index
        return [] 


'''
The above solution is a hashmap based solution that runs in O(n) time but also requires O(n) additional space.
'''