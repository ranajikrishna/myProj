
'''
Name: Remove duplicates from list withput a buffer.

Author: Ranaji Krishna.

Notes:
Implement an algo. to find the kth last elmt. in a linked list.

'''

from myLib import *

def find_kth(chk_node, k):

	if (chk_node.get_next() == None):		
		return(0)
	
 	i = find_kth(chk_node.get_next(), k) + 1

	if (i == k):
		print(chk_node.get_data())
		
	return(i)

def main (argv = None):
		
	myList = lkdList_example.linkedList()
		
	myList.add(5)
	myList.add(8)
	myList.add(12)
	myList.add(14)
	myList.add(8)
	myList.add(3)
	myList.add(8)
	myList.add(12)

	find_kth(myList.head(), 0)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)

