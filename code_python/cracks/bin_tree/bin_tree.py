
'''
Name: Binary Tree.

Author: Ranaji Krishna.

Notes:

'''


from myLib import *


class Node(object):

	def __init__(self, val):
		self.lnode = None
		self.rnode = None
		self.val = val

class Tree(object):

	def __init__(self):
		self.root = None

	def add(self, val):
		if (self.root == None):
			self.root = Node(val)
		else:
			self._add(self.root, val)

	def _add(self, node, val):
		if (self.root != None):
			if (node.val < val):
				if node.rnode != None:
					self._add(node.rnode, val)
				else:
					node.rnode = Node(val)
			else:
				if node.lnode != None:
					self._add(node.lnode, val)
				else:
					node.lnode = Node(val)
		else:
			self._add(self.root, val)



	def print_tree(self):
		if (self.root != None):
			self._print_tree(self.root)
	
	def _print_tree(self, node):
		if (node != None):
			self._print_tree(node.lnode) 
			print str(node.val) + ' '
			self._print_tree(node.rnode) 
		

def main (argv = None):
	
	tree = Tree()
	tree.add(3)
	tree.add(4)
	tree.add(0)
	tree.add(8)
	tree.add(2)
	tree.add(5)
	tree.add(6)
	tree.add(2)
	tree.add(9)
	tree.add(1)

	return(0) 


if __name__ == '__main__':
	status = main()
	sys.exit(status)

