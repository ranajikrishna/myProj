'''
Name: Remove duplicates from list.

Author: Ranaji Krishna.

Notes:
Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

'''

from myLib import *


def remove_dup(chk_list):   # using myList = lkdlist_practise.linkedList()

	h_table = {'None':None}
	this_node = chk_list.root
	while this_node: 
		if (this_node.data in h_table):
			chk_list.remove(this_node.data)
			this_node = this_node.next_node
			
		else:
			h_table[this_node.data] = True
			this_node = this_node.next_node

	return(0)
'''
def remove(chk_list):      # using myList = lkdList_example.linkedList()

	h_table = {'None':None}
	this_node = chk_list.head()
	while this_node: 
		if (this_node.get_data() in h_table):
			chk_list.remove(this_node.get_data())
			this_node = this_node.get_next()
			
		else:
			h_table[this_node.get_data()] = True
			this_node = this_node.get_next()

	return(0)
'''



def main(argv = None):

#myList = lkdList_example.linkedList()
	myList = lkdList_practise.linkedList()

	myList.add(5)
	myList.add(8)
	myList.add(12)
	myList.add(14)
	myList.add(8)
	myList.add(3)
	myList.add(8)
	myList.add(12)
	remove_dup(myList)

	myList.show()

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
