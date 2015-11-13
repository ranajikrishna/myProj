
'''
Name: Remove duplicates from list withput a buffer.

Author: Ranaji Krishna.

Notes:
How would you solve this problem if a temporary buffer is not allowed?

'''

from myLib import *

def remove_dup_nobuf(chk_list):

	current_node = chk_list.head()
	
	while current_node:
		runner_node = current_node
		while runner_node.get_next():
			if(current_node.get_data() == runner_node.get_next().get_data()):
				runner_node.set_next(runner_node.get_next().get_next())
			else:
				runner_node = runner_node.get_next()

		current_node = current_node.get_next()


		
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
	remove_dup_nobuf(myList)

	myList.show()

	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)

