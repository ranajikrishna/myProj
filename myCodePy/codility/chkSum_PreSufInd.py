#
# Name:   Index where sum of Prefix equals sum of Suffix .
#
# Author: Ranaji Krishna.
#
# *** Notes ***:

from myLib import *


def checkSum(tmpArray):

	sumArray = sum(tmpArray)
	prev, curr = 0, tmpArray[0]

	for index in range(1, len(tmpArray)):
		prev += tmpArray[index - 1]
		curr += tmpArray[index]

		if prev + curr == sumArray:
			return index

	return -1


def main (argv = None):

#myArray = [1,2,3,4,2,-1,6,5]
	myArray = [1,0,1,0,1,0,1,0]
	index = checkSum(myArray)		
	print(index)

	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
