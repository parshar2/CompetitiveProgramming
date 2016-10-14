'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
'''
class Solution(object):
	def threeSum(self, nums):
		valid_indexes =  []
		length = len(nums)
		nums.sort()
		for i in xrange(length):
			c = -1*nums[i]
			low, high = i + 1, length -1
			while low < high:
				if low == i:
					low += 1
				elif high == i:
					high -= 1
				elif (nums[low] + nums[high]) < c:
					low += 1
				elif (nums[low] + nums[high]) > c:
					high -= 1
				else:
					found_tuple =  [nums[i], nums[low], nums[high]]
					found_tuple.sort()
					if found_tuple not in valid_indexes:
						valid_indexes.append(found_tuple)
					low += 1
					high -= 1
		return valid_indexes
