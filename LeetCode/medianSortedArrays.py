'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print nums1
        print nums2
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 and l2 == 1:
        	return nums2[0]
        elif l1 == 1 and l2 == 0:
        	return nums1[0]
        elif l1 == 1 and l2 == 1:
        	return (nums2[0] + nums1[0])/2.0
        else:
        	m1 = (nums1[l1/2] + nums1[(l1-1)/2])/2.0
        	m2 = (nums2[l2/2] + nums2[(l2-1)/2])/2.0
        	if m1 == m2:
        		return m1
        	elif m1 >= m2:
        		return findMedianSortedArrays(nums1[:(l1 + 1)/2], nums2[l2/2:])
        	else:
        		return findMedianSortedArrays(nums1[l1/2:], nums2[:(l2 +1)/2])

