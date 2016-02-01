
'''
Name: Remove duplicates from list.

Author: Ranaji Krishna.

Notes:
Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

'''

from myLib import *

class node(object):

	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def set_data(self,data):
		self.data = data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next


class linkedList(object):


	def __init__(self, r = None):
		self.root = r
		self.size = 0
	
	def get_size(self):
		return self.size

	def add(self,d):
		new_node = node(d,self.root)
		self.root = new_node
		self.size += 1

	def head(self):			# My code.
		return(self.root)

	def show(self):			# My code.
		this_node = self.root

		while this_node:
			print(this_node.get_data())
			this_node = this_node.get_next()
	
	def remove (self, d):
		this_node = self.root
	        prev_node = None

        	while this_node:
	            if this_node.get_data() == d:
        	        if prev_node:
                	    prev_node.set_next(this_node.get_next())
	                else:
        	            self.root = this_node.get_next()
                	self.size -= 1
	                return True		# data removed
        	    else:
                	prev_node = this_node
	                this_node = this_node.get_next()
        	return False  # data not found

    	def find (self, d):
        	this_node = self.root
        	while this_node:
            		if this_node.get_data() == d:
                		return d
            		else:
                		this_node = this_node.get_next()
		
	 	return None

'''
def main(argv = None):

	myList = linkedList()
	myList.add(5)
	myList.add(8)
	myList.add(12)
	myList.remove(8)
	print(myList.remove(12))
	print(myList.find(5))

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)

'''
