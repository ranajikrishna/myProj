
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
		node_for, m = is_palindrome(chk_list, node_bck.get_next(), k)
	else:
		node_for = chk_list.head()
		return(node_for, floor(k/2))

	if (node_for.get_data() == node_bck.get_data()):
		node_for = node_for.get_next()
		if (k==1):
			return(True)
		else:
			return(node_for, m)
	else:
		if (k==1):
			return(False)
		else:
			return(node_for, m)

def main(argv = None):

	myList = lkdList_example.linkedList()
	myList.add(1)
	myList.add(2)
	myList.add(3)
	myList.add(2)
	myList.add(1)
		
	print(is_palindrome(myList, myList.head(), 0))

	return(0)



if __name__ == '__main__':
	status = main()
	sys.exit(status)
