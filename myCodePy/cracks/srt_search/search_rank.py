
'''
Name: Search and rank.

Author: Ranaji Krishna.

Notes:
Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number 
x (the number of values less than or equal to x). Imple- ment the data structures and algorithms to support these
operations. That is,imple- mentthemethodtrack(int x), which is called when each number is generated, and the method 
get Rank Of'Number (int x), which returns thenumberof values less than or equal to x (not including x itself).
'''


from myLib import *


class node(object):
	def __init__(self, val, rank = None):
		self.val = val
		self.rank = rank
		self.lnode = None
		self.rnode = None
		
	def add(self, val):
		if (self.val < val):
			if(self.rnode):
				return self.rnode.add(val)
			else:
				self.rnode = node(val, 0)
				return None
		else:
			self.rank = self.rank + 1
			if(self.lnode):
				return self.lnode.add(val)
			else:
				self.lnode = node(val, 0)
				return None


	def in_find(self, val, subRank = None):
		
		if (self.lnode):
			subRank_l = self.lnode.in_find(val, subRank)
			if (subRank_l != subRank):
				return subRank_l
		if (self.val == val):
			return (self.rank + 1)
		if (self.rnode):
			subRank_r = self.rnode.in_find(val, subRank)
			if (subRank_r != subRank):
				return subRank_r + self.rank + 1
		return None

	


def main(argv = None):


	tree = node(8,0)

	tree.add(4)
	tree.add(12)

	tree.add(2)
	tree.add(6)
	tree.add(10)
	tree.add(14)

	tree.add(1)
	tree.add(3)
	tree.add(5)
	tree.add(7)
	tree.add(9)
	tree.add(11)
	tree.add(13)
	tree.add(15)


	print(tree.in_find())


	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)


