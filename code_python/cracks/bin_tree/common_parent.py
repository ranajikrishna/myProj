
'''
Name: First common node.

Author: Ranaji Krishna.

Notes: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''

from myLib import *

def bfs_search(node, p, q, chk, queue):
	if (queue[0].val == p or queue[0].val == q):
		chk = chk + 1
		if(chk == 2):
			return(chk)

	if (queue[0].lnode):
		queue.append(queue[0].lnode)
	if (queue[0].rnode):
		queue.append(queue[0].rnode)
	del queue[0]

	if (len(queue) != 0):
		return(bfs_search(queue[0], p, q, chk, queue))	
	
	return(chk)

def common_node(tree, p, q):
	chk_l = bfs_search(tree.lnode, p, q, 0, queue=[tree.lnode])
	chk_r = bfs_search(tree.rnode, p, q, 0, queue=[tree.rnode])

	if (chk_l == 2):
		return(common_node(tree.lnode, p, q))

	elif (chk_r == 2):
		return(common_node(tree.rnode, p, q))
		
	elif (chk_l == 0 and chk_r == 0):
		return (None)

	elif((chk_l == 1 or chk_r == 1) and (tree.val == p or tree.val == q)):
		return (tree)

	elif (chk_l == 1 and chk_r == 1):
		return(tree)

	else:
		return(None)


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

	com_node = common_node(tree,7,2)
	print(com_node)
	if(com_node):
		print(com_node.val)

	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
