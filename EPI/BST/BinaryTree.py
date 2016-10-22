class BinaryTree:
	'Defines a Binary Tree which has a left node and a right node'
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

def getBST():
	'''Returns a Binary Search Tree. Hard Coding a Binary Tree for now'''
	a5 = BinaryTree(5, BinaryTree(1), BinaryTree(7)) 
	a15 = BinaryTree(15, BinaryTree(12), BinaryTree(17))
	a10 = BinaryTree(10, a5, a15)
	a30 = BinaryTree(30, BinaryTree(25), BinaryTree(35))
	a20 = BinaryTree(20, a10, a30)
	root = a20
	return root

def getNonBST():
	'''Returns a Binary Search Tree. Hard Coding a Binary Tree for now'''
	a5 = BinaryTree(5, BinaryTree(1), BinaryTree(7)) 		#Left child of 10
	a15 = BinaryTree(15, BinaryTree(12), BinaryTree(17))	#Right child of 15
	a10 = BinaryTree(10, a5, a15)							#Left child of root
	a30 = BinaryTree(30, BinaryTree(25), BinaryTree(35))	#Right Child of root
	a20 = BinaryTree(40, a10, a30)							#Root
	root = a20
	return root

def preorderTraversal(root):
	'''Prints the pre-order traversal of the tree'''
	if root is None:
		return
	else:
		print root.data,
		preorderTraversal(root.left)
		preorderTraversal(root.right)

def preOrderIterative(root):
	if root is None:
		return
	stack = [root]
	while len(stack) != 0:
		node = stack.pop()
		print node.data,
		if node.right is not None:
			stack.append(node.right)
		if node.left is not None:
			stack.append(node.left)

def inOrderIterative(root):
	'''Perform inOrder traversal in an iterative manner'''
	stack = []
	currNode = root
	while (len(stack) != 0 or currNode != None):
		if currNode is not None:
			stack.append(currNode)
			currNode = currNode.left
		else:
			currNode = stack.pop()
			print currNode.data,
			currNode = currNode.right

def inOrderIterativeOnlyStack(root):
	'''Perform inOrder traversal in an iterative manner'''
	stack = [root]
	while (len(stack) != 0):
		currNode = stack.pop()
		if currNode is not None:
			next_elem = None if len(stack) == 0 else stack[len(stack) -1]
			if next_elem == currNode.left:
				if len(stack) != 0:
					stack.pop() 
				print currNode.data,
				stack.append(currNode.right)
			else:
				stack.append(currNode.left)
				stack.append(currNode)
				stack.append(currNode.left)



def postOrderTraversal(node):
	if node is None:
		return
	postOrderTraversal(node.left)
	postOrderTraversal(node.right)
	print node.data,

def postOrderTraversalIterative(root):
	stack = [] #used for visiting a node the second and third time
	p = root #used for visiting a node the first time
	while len(stack) != 0 or p != None: 
		if p is not None:
			stack.append(p) #First time node is visited
			p = p.left
		else :
			p = stack.pop() 
			next_elem = None if len(stack) == 0 else stack[len(stack)-1]
			if next_elem is not p.right:
				 #Second time node is visited
				 stack.append(p.right)
				 stack.append(p)
				 p = p.right
			else:
				#Third time node is visited
				stack.pop()
				print p.data,
				p = None


if __name__ == '__main__':
	a = getBST()
	print postOrderTraversal(a)
	print postOrderTraversalIterative(a)
	print inOrderIterative(a)
	print inOrderIterativeOnlyStack(a)
	
	