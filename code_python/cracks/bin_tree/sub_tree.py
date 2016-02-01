
'''
Name: Is it a sub-tree.

Author: Ranaji Krishna.

Notes: You have two very large binary trees: Tl, with millions of nodes, and T2, with
hundreds of nodes.Create an algorithm to decide if T2 is a sub tree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree ofn is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical. 
'''

from myLib import *

def pre_search(node_T1, T2):
	
	if (node_T1.val == T2.val):
		if ((bool(node_T1.lnode) ^ bool(T2.lnode)) and \
	            (bool(node_T1.rnode) ^ bool(T2.rnode))):
			if (node_T1.lnode and T2.lnode):
				return(pre_search(node_T1.lnode, T2.lnode))
			if (node_T1.rnode and T2.rnode):
				return(pre_search(node_T1.rnode, T2.rnode))
			return True
		else:
			return False
	else:
		return False
		  
def is_sub(T1, T2, queue = None):		# Apply bfs to look for root of T2.
	
	if (queue[0].val != T2.val):
		if (queue[0].lnode):
			queue.append(queue[0].lnode)
		if (queue[0].rnode):
			queue.append(queue[0].rnode)
		del queue[0]
		if(len(queue)!=0):
			return (is_sub(queue[0], T2, queue))
		else:
			return(False)
	else:
		return (pre_search(queue[0], T2))

def main(argv = None):

	T1 = binTree_node.node(8)

	T1.add(4)
	T1.add(12)
	
	T1.add(2)
	T1.add(6)
	T1.add(10)
	T1.add(14)	

	T1.add(1)
	T1.add(3)
	T1.add(5)
	T1.add(7)
	T1.add(9)
	T1.add(11)
	T1.add(13)
	T1.add(15)

	T2 = binTree_node.node(25)
	T2.add(11)
	T2.add(15)

	print(is_sub(T1,T2, queue=[T1]))

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)


