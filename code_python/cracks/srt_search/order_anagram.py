
'''
Name: Arrange anagram.

Author: Ranaji Krishna.

Notes:
Write a method to sort an array of strings so that all the anagrams are next to each
other.

'''
from myLib import *

def grp_ana(tmp_arr):
	dict_grp = {}
	
	for i in xrange(0,len(tmp_arr)):
		dict_grp.setdefault(''.join(sorted(map(lambda c:c, tmp_arr[i]))), []).append(tmp_arr[i])

	return(dict_grp.values())
	
def main(argv = None):

	str_arr = ['vini','lila','ranaji','ilal','invi','duncan','candun',\
		   'lali','jirana','llia','dncuan']

	print(grp_ana(str_arr))
	return(0)


if __name__ =='__main__':
	status = main()
	sys.exit(status)

