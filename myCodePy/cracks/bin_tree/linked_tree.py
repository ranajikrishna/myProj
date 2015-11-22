'''
Name: Linked List from a binary tree.

Author: Ranaji Krishna.

Notes:  Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D,you'll have D linked lists).
'''

from myLib import *

class node(object):
	def __init__(self, val, next_node = None):
		self.val = val
		self.next_node = next_node


def make_list(tree, queue = [None], root = None):
	if(root == None):
		queue.append(tree)
		del queue[0]
		queue.append (None)
	
	if (queue[0] == None):
		queue.append(None)
		del queue[0]
		root = 1

	if(queue[0]):
		if (queue[0].lnode):
			queue.append(queue[0].lnode)
		if (queue[0].rnode):
			queue.append(queue[0].rnode)
	
		new_list = node(queue[0].val, root)
		root = new_list
		del queue[0]
					
		list_lkd, tik  = make_list(queue[0], queue, root)
		if (tik == 1):
			list_lkd.append(new_list)
			tik = 0
			return(list_lkd, tik)
		else:
			if (new_list.next_node == 1):
				tik = 1
			return(list_lkd, tik)
	else:
		list_lkd = []
		tik = 1
		return(list_lkd, tik)			
			
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

	list_lkd,tmp = make_list(tree)

	return(0)


if __name__=='__main__':
	status = main()
	sys.exit(status)


