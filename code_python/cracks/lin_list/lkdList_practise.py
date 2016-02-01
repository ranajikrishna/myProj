
'''
Name: Example of a linked list.

Author: Ranaji Krishna.

Notes:
This is a different implementation of a linked list compared to
lkdList_example.py
'''

from myLib import *

class node(object):

	data = None
	next_node = None

class linkedList(object):

	root = None

	def add(self,d):
		new_node = node()
		new_node.data = d
		new_node.next_node = self.root
		self.root = new_node

    	def find (self, d):
        	this_node = self.root
        	while this_node:
            		if this_node.data == d:
                		return d
            		else:
                		this_node = this_node.next_node
		
	 	return None

	def show(self):			# My code.
		this_node = self.root

		while this_node:
			print(this_node.data)
			this_node = this_node.next_node

	def remove (self, d):
		this_node = self.root
	        prev_node = None

        	while this_node:
	            if this_node.data == d:
        	        if prev_node:
                	    prev_node.next_node = this_node.next_node
	                else:
			    self.root = this_node.next_node
	                return True		# data removed
        	    else:
                	prev_node = this_node
	                this_node = this_node.next_node
        	return False  # data not found

'''
def main(argv = None):

	myList = linkedList()
	myList.add(5)
	myList.add(8)
	myList.add(12)
	myList.add(14)
	myList.add(8)
	myList.add(3)
	myList.add(8)
	myList.add(12)

#	myList.show()

	myList.remove(12)
	myList.show()

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
'''
