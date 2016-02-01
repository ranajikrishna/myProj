
'''
Name: Is balanced tree.

Author: Ranaji Krishna.

Notes: Is the binary tree balanced?
'''

from myLib import *


def depth(self):

	if (self):
		return max(depth(self.lnode), depth(self.rnode)) + 1
	else:
		return (-1)	

def is_balanced(node):

	if (node):
		height_lnode = depth(node.lnode)
		height_rnode = depth(node.rnode)
		if (abs(height_lnode - height_rnode) <= 1):
			l = is_balanced(node.lnode)
			r = is_balanced(node.rnode)
			if (l==1 and r ==1):
				return(1)
			else: 
				return(-1)
		else:		
	 		return(-1)	 
	else:
		return(1)

def main(argv = None):

	tree = binTree_node.node(6)

	tree.add(10)
	tree.add(4)
	tree.add(9)
	tree.add(8)
	tree.add(7)
	tree.add(11)
	tree.add(2)
	tree.add(5)
	tree.add(1)
	tree.add(3)

	print(is_balanced(tree))	

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
