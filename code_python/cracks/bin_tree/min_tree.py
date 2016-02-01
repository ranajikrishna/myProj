'''
Name: Minimum height tree.

Author: Ranaji Krishna.

Notes: Given a sorted (increasing order) array with unique integer elements, write an algo- rithm to create a binary search tree with minimal height.
'''

from myLib import *


class node(object):
	def __init__(self,val):
		self.val = val
		self.lnode = None
		self.rnode = None

def min_tree(arr, st, ed):
	
	if (st > ed):
		return(None)
	
	mid = (st + ed)/2
	sub = node(arr[mid])
	print(sub.val)
	sub.lnode = min_tree(arr, st, mid-1)
	sub.rnode = min_tree(arr, mid+1, ed)
	return sub



def main(argv = None):

	arr = range(1,12)
	tree = binTree_node.node(arr[len(arr)/2])
	
	min_tree(arr, 0, len(arr)-1)
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
