
'''
Name: Remove duplicates from list.

Author: Ranaji Krishna.

Notes:
 Write code to partition a linked list around a value x, such that all nodes less than x come before alt nodes greater than or equal to x?

'''

from myLib import *

def partition(chk_list, x):

	chk_node = chk_list.head()
	before = lkdList_example.linkedList()
	after = lkdList_example.linkedList()

	while chk_node:
		if(chk_node.get_data() < x):
			before.add(chk_node.get_data())
		else:
			after.add(chk_node.get_data())

		chk_node = chk_node.get_next()

	node_bf = before.head()
	while (node_bf):
		 if (node_bf.get_next() == None):
			 node_bf.set_next(after.head())
			 return(before)
		 
		 node_bf = node_bf.get_next()




def main(argv = None):

	myList = lkdList_example.linkedList()

	myList.add(5)
	myList.add(8)
	myList.add(12)
	myList.add(14)
	myList.add(8)
	myList.add(3)
	myList.add(8)
	myList.add(12)

	newList = partition(myList, 7)
	newList.show()

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)

