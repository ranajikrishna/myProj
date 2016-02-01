
'''
Name: Route.

Author: Ranaji Krishna.

Notes: Is there a route between two given nodes.
'''

from myLib import *


def bfs_search(queue, val2):
	if (queue == None):
		return(False)	
	if (queue[0]):
		if (queue[0].val == val2):
			return(True)
		else:
			if (queue[0].lnode):
				queue.append(queue[0].lnode)
			if(queue[0].rnode):
				queue.append(queue[0].rnode)
			del queue[0]
			if (len(queue) != 0):
				return(bfs_search(queue, val2))
			else:
				return(False)

def is_route(val1, val2, tree):

	node1, parent1 = tree.lookup(val1)
	queue = [node1]	
	
	print(bfs_search(queue, val2))

	return(0)

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

	num1 = 6; num2 = 3
	is_route(num1, num2, tree)

	return(0)



if __name__ == '__main__':
	status = main()
	sys.exit(status)
