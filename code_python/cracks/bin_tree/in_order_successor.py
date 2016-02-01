
'''
Name: In-order successor.

Author: Ranaji Krishna.

Notes: An algorithm to find the 'next'node (i.e., in-order successor) of a given node in
a binary search tree. Youmay assume that each nodehas a link to its parent.'''

from myLib import *

class node (object):

	def __init__(self, val, parent = None):
		self.val = val
		self.lnode = None
		self.rnode = None
		self.parent = parent

	def add(self, val):
		if (self.val < val):
			if(self.rnode):
				self.rnode.add(val)
			else:
				self.rnode = node(val, self)
		else:
			if(self.lnode):
				self.lnode.add(val)
			else:
				self.lnode = node(val, self)

def get_lnode(sub):
	if(sub.parent.rnode == sub):
		return(get_lnode(sub.parent))
	else:
		return(sub.parent)

def in_order(sub):
	if (sub.lnode):
		return(in_order(sub.lnode))
	else:
		return(sub)

def successor(sub):

	if (sub.rnode):
		return(in_order(sub.rnode))		
		
	elif (sub.parent.lnode == sub):
		return(sub.parent)
			
	else:
		return(get_lnode(sub.parent))

def find_node(tree, val, sub = None):

	if (tree):
		sub = find_node(tree.lnode, val, sub)
		if (tree.val != val): 
			sub = find_node(tree.rnode, val, sub)
		else:
			return tree
		return sub

	return sub	

def main(argv = None):

	tree = node(8)

	tree.add(4)
	tree.add(12)

	tree.add(2)
	tree.add(6)
	tree.add(10)
	tree.add(14)

	tree.add(1)
	tree.add(3)
	tree.add(5)
	tree.add(7)
	tree.add(9)
	tree.add(11)
	tree.add(13)
	tree.add(15)

	tmp_node = find_node(tree, 7)
	suc = successor(tmp_node)

	print(suc.val)


	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
