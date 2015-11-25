
'''
Name: Path leading to a sum.

Author: Ranaji Krishna.

Notes: 
You are given a binary tree in which each node contains a value. Design an algorithm to print all paths which sum to a given value. The path does not need to start or end at the root or a leaf.

'''
from myLib import *

def find_sum(path, tgt_sum):
	i = len(path)-1
	cum_sum = 0
	while (i > -1):
		cum_sum  = path[i].val + cum_sum
		if(cum_sum == tgt_sum):
			j = i
			while (j < len(path)):
				print path[j].val,
				j = j + 1
			print ""
		i = i -1 
	return(0)

def pre_search(tree, tgt_sum, path):
	path_size = len(path)-1
	if (path[path_size].lnode):
		path.append(path[path_size].lnode)
		find_sum(path, tgt_sum)
		pre_search(path[path_size], tgt_sum, path)
	if (path[path_size].rnode):
		path.append(path[path_size].rnode)
		find_sum(path, tgt_sum)
		pre_search(path[path_size], tgt_sum, path)
		
	del path[len(path)-1]
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
	
	tgt_sum = 12 
	pre_search(tree, tgt_sum, path = [tree])
	
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
