'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Write a method to replace all spaces in a string with '%20'. Youmay assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string.
'''

from myLib import *

def rev_char(arr_str):


	----- INCOMPLETE -----
	test_str = [ ]
	for i in arr_str: test_str.append(i)
	
	for i in xrange(len(test_str)-1, 0, -1):
		if (test_str[i] == ' '):
			test_str[i] = "0"
			test_str[i-1] = "2"
			test_str[i-2] = "%"
	
	return(test_str)


def main(argv = None):

	wrd = 'kori shna'
	res = rev_char(wrd)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
