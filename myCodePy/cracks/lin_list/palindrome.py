
'''
Name: Check if a Linked List is a palindrome.

Author: Ranaji Krishna.

Notes:
Implement a function to check if a linked list is a palindrome,
'''


from myLib import *



def is_palindrome(chk_list, node_bck, k):

	if node_bck:
		k += 1
		node_for, m, chk = is_palindrome(chk_list, node_bck.get_next(), k)
		if chk == 0:
			node_for = node_for.get_next()
			return(node_for, floor(k/2), 0)
	else:
		node_for = chk_list.head()
		return(node_for, floor(k/2), 1)

	if (node_for.get_data() == node_bck.get_data()):
		node_for = node_for.get_next()
		return(node_for, m, 1)
	else:
		node_for = node_for.get_next()
		return(node_for, m, 0)

def main(argv = None):

	myList = lkdList_example.linkedList()
	myList.add(1)
	myList.add(2)
	myList.add(3)
	myList.add(1)
	myList.add(3)
	myList.add(2)
	myList.add(1)
		
	node, mid, is_pal= is_palindrome(myList, myList.head(), 0)
	if (is_pal == 0):
		print("False")
	else:
	 	print("True")

	return(0)



if __name__ == '__main__':
	status = main()
	sys.exit(status)
