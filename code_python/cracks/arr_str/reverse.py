
'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Implement a function void reversefchar* str) in Cor C++ which reverses a null-termi- nated string.
'''

from myLib import *

def rev_char(arr_str):
	sta = 0
	test_str = [ ]
	for i in arr_str: 
		test_str.append(i)	
	
	end = len(test_str)-1
	while (sta != end):
		tmp = test_str[end]
		test_str[end] = test_str[sta]
		end-=1
		test_str[sta] = tmp
		sta+=1
	return(test_str)

def main(argv = None):

	test = 'tpeople'
	res = rev_char(test)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
