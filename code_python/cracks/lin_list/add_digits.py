
'''
Name: Addition using Linked List.

Author: Ranaji Krishna.

Notes:
You have two numbers represented by a linked list, where each node contains a single digit. Thedigits are stored in reverse order, such that the 1'sdigit isat the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
'''


from myLib import *


def add_dig(list1, list2):

	add_list = lkdList_example.linkedList()
	add_node = add_list.head()
	node1 = list1.head()
	node2 = list2.head()
		

	while (node1):

		tmp = node1.get_data() + node2.get_data()
		if (tmp >= 10 and node1.get_next()):
			add_list.add(tmp - 10)
			node1.get_next().set_data(1 + node1.get_next().get_data())
		else:
			if(tmp >= 10):
				add_list.add(tmp - 10)
				add_list.add(1)
			else:
				add_list.add(tmp)

		node1 = node1.get_next()
		node2 = node2.get_next()

			
	return(add_list)



def main(argv = None):

	list1 = lkdList_example.linkedList()
	list2 = lkdList_example.linkedList()

	# --- Form number 617 ---
	list1.add(6)
	list1.add(1)
	list1.add(7)

	# --- Form number 295 ---
	list2.add(2)
	list2.add(9)
	list2.add(5)


	add_list = add_dig(list1, list2)
	add_list.show()


	return(0)



if __name__ == '__main__':
	status = main()
	sys.exit(status)

