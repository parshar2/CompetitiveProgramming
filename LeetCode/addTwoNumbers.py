'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       	 start, end = None, None
        carryover = 0
        while l1 != None or l2 != None:
        	a1, a2 = 0, 0
        	if l1 != None:
        		a1 = l1.val
        		l1 = l1.next
        	if l2 != None:
        		a2 = l2.val
        		l2 = l2.next
        	s = (a1 + a2 + carryover)%10
        	carryover = (a1 + a2 + carryover)/10
        	node = ListNode(s)
        	if end == None:
        		start, end = node, node
        	else:
        		end.next = node
        		end = node
        if carryover != 0:
        	end.next = ListNode(carryover)
        return start
