
'''
Name: Binary Tree.

Author: Ranaji Krishna.

Notes: Single class implementation of binary tree. 

'''

from myLib import *


class node(object):

	def __init__(self,val):
		self.lnode = None
		self.rnode = None
		self.val = val


	def add(self, val):
			if (self.val < val):
				if(self.rnode):
					self.rnode.add(val)
				else:
					self.rnode = node(val)
			else:
				if(self.lnode):
					self.lnode.add(val)
				else:
					self.lnode = node(val)
	
	def lookup(self, val, parent =None):
        	if val < self.val:
	            if (self.lnode):
	            	return self.lnode.lookup(val, self)
		    return None, None
        	elif val > self.val:
	            if (self.rnode):
	            	return self.rnode.lookup(val, self)
		    return None, None
        	else:
	            return self, parent


	# --- Depth first search ---
	def pre_prnt(self):				# Pre-order
		if (self):
			print(self.val)
			if (self.lnode):
				self.lnode.pre_prnt()
			if (self.rnode):
				self.rnode.pre_prnt()
			return(None)


	def in_prnt(self):				# In-order
		if (self.lnode):
			self.lnode.in_prnt()
		if(self):
			print(self.val)
		if (self.rnode): 
			self.rnode.in_prnt()


	def post_prnt(self):				# Post-order
		if (self.lnode): 
			self.lnode.post_prnt()
		if (self.rnode): 
			self.rnode.post_prnt()
		if(self):
			print(self.val)


	# --- Breath first search ---
	def bfs_prnt(self, queue = [None]):
		if (queue[0] == None):
			queue[0] = self
		if (queue[0]):
			print (queue[0].val)
			del queue[0]
			if (self.lnode):
				queue.append(self.lnode)
			if (self.rnode):
				queue.append(self.rnode)
			if (len(queue) != 0):
				queue[0].bfs_prnt(queue)


def main(argv = None):

	tree = node(6)

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

#	tree.post_prnt()
#	tree.bfs_prnt()
#	node1, parent = tree.lookup(3)
#	print(node1)
#	print(parent)

	tree.pre_prnt()

	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)

