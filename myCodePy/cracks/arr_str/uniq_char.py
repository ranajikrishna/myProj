
'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure
'''

from myLib import *

def uniq_char(test_str):
	
	if len(test_str) > 25: return(False)
	bool_arr=[ ]
	for i in test_str:
		if i in bool_arr: 
			return(False)
		else: 
			bool_arr.append(i)
	return(True)

def isUniqueChars(string):
 	checker = 0
  	for c in string:
    		val = ord(c) - ord('a')
		if (checker & (1 << val) > 0):
	      		return (False)
    		else:
		      checker |= (1 << val)
	return (True)

def main(argv = None):

	test = 'tpeople'
#res = uniq_char(list(test))
	res = isUniqueChars(test)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
