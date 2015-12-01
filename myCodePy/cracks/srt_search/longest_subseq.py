
'''
Name: Longest subsequence.

Author: Ranaji Krishna.

Notes:
A circus is designing a tower routine consisting of people standing atop one anoth- er's shoulders. 
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below 
him or her. Given the heights and weights of each person in the circus, write a method to compute the 
largest possible number of people in such a tower.
'''


from myLib import *


class person (object):
	def __init__(self, hgt, wgt):
		self.hgt = hgt
		self.wgt = wgt

def subSeq(tmpList, newList, upto, cur):
	if (cur < 0):
		return(newList, len(newList))
	if(tmpList[upto].wgt < tmpList[cur].wgt):
		newList.append(tmpList[cur])
		upto = cur
		cur = cur - 1
		return	subSeq(tmpList, newList, upto, cur)
	else:
		cur = cur - 1
		return subSeq(tmpList, newList, upto, cur)

def main(argv = None):
	
	#np.random.seed(seed=1)
	num = 50
	myList = [person(np.random.randint(1,100,1), np.random.randint(10,100,1)) \
	          for count in xrange (num)]
	
	myList = sorted(myList, key = lambda x:x.hgt, reverse=True)

	myDict = {}
	for i in range(num):
		tmpList, size = subSeq(myList, [myList[i]], i, i-1)
		myDict.setdefault(size,[]).append(tmpList) 	

	for i in range(max(myDict, key=myDict.get)):
		print(myDict[max(myDict, key=myDict.get)][0][i].hgt, myDict[max(myDict, key=myDict.get)][0][i].wgt)	

	#print(myDict)
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
