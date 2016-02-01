

'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Implement a function void reversefchar* str) in Cor C++ which reverses a null-termi- nated string.
'''

from myLib import *

def rev_char(arr_str1, arr_str2):
	test_str1 = [ ]
	test_str2 = [ ]
	if (len(arr_str1) != len(arr_str2)):
		return(False)

	for i in xrange(0,len(arr_str1)): 
		test_str1.append(arr_str1[i])	
		test_str2.append(arr_str2[i])

	if(test_str1.sort() == test_str2.sort()):
 		return(True)
	else:
		return(False)
	
def main(argv = None):

	wrd1 = 'korishna'
	wrd2 = 'rikshaon'
	res = rev_char(wrd1,wrd2)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
