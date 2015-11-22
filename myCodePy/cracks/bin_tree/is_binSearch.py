
'''
Name: Is the tree a binary search tree?

Author: Ranaji Krishna.

Notes: Imp/emen t a function to check if a binary tree is a binary search tree.'''

from myLib import *


def is_bin(sub, l, r):

	if (sub.lnode and sub.rnode):
		if(sub.lnode.val < sub.rnode.val):
			l = is_bin(sub.lnode, l, r)
			r = is_bin(sub.rnode, l, r)

		else:
			return(0)
	return(l*r)
	
def main(argv = None):

	tree = binTree_node.node(8)

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

	print(is_bin(tree, 1, 1))

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
