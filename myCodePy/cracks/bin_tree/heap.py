
'''
Name: Binary Tree.

Author: Ranaji Krishna.

Notes: Single class implementation of binary tree.
website: http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

'''

from myLib import *

class binHeap(object):
	def __init__(self):
		self.heapList = [0]
		self.curSize = 0

	def percUp(self, i):
		while (i // 2 > 0):
			if (self.heapList[i//2] > self.heapList[i]):
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i]  = tmp
				i = i//2	
	
	def insert(self, k):
		self.heapList.append(k)
		self.curSize = self.curSize + 1
	 	self.percUp(self.curSize)
		
	def percDwn(self, k):
		while (2 * k <= self.curSize):
			mc = self.minChild(k)
			if self.heapList[k] > self.heapList[mc]:
				tmp = self.heapList[mc]
				self.heapList[mc] = self.heapList[k]
				self.heapList[k] = tmp
			k = mc

	def minChild(self, k):
		if 2 * k + 1 > self.curSize:
			return 2 * k
		else:
			if self.heapList[2 * k + 1] > self.heapList[2 * k]:
				return 2 * k
			else:
				return 2 * k + 1

	def delMin(self):
		retVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.curSize]
		self.heapList.pop()
		self.curSize = self.curSize - 1
		self.percDwn(1)
		return retVal

	def buildHeap(self, myList):
		i = len(myList)//2
		self.curSize = len(myList)
		self.heapList = [0] + myList[:]
		while(i > 0):
			self.percDwn(i)
			i = i - 1

	def getHeap(self):
		return self.heapList
		



def main(argv = None):


	myList = [9,8,4,3,5,2,6,7,2]
		
	myHeap = binHeap()
	myHeap.buildHeap(myList)

	print(myHeap.delMin())
	print(myHeap.getHeap())


	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
