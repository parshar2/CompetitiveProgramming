import BinaryTree
class Solution(object):
	def kthSmallest(self, root, k):
		'''Get the kth smallest element from a given BST. Assume 1 <= k <= BST's total element'''
		dict = {}
		self.inOrderTraversal(root, 0, k, dict)
		return dict[k]

	def inOrderTraversal(self, node, numPreviousElements, k, dict):
		if node is None:
			return 0
		numElementsToLeft = self.inOrderTraversal(node.left, numPreviousElements, k, dict)
		totElements = numPreviousElements + numElementsToLeft + 1 
		if totElements == k:
			dict[k] = node.data
			return k
		elif totElements > k:
			return k
		else :
			numElementsToRight = self.inOrderTraversal(node.right, totElements, k, dict)
			return numElementsToRight + numElementsToRight + 1

if __name__ == '__main__':
	root = BinaryTree.getBST()
	print Solution().kthSmallest(root, 11)
