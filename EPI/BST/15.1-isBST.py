import BinaryTree as BT
#Data is given to be between 0 and 10*1000
def check_binary_search_tree_(root):
	'''Checks whether the given tree is binary search tree or not and returns True or False'''
	return root is None or (check_binary_subtree(root.left, 0, root.value-1) and check_binary_subtree(root.right,
		root.value + 1, 10*1000))


def check_binary_subtree(root, minValue, maxValue):
	if root is None:
		return True
	if root.value < minValue or root.value > maxValue:
		return False
	return check_binary_subtree(root.left, minValue, root.value-1) and check_binary_subtree(root.right, root.value+1, maxValue)


if __name__ == '__main__':
	BST = BT.getBST()
	print check_binary_search_tree_(BST)