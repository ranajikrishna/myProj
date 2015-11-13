
'''
Name: Look for the unique character.

Author: Ranaji Krishna.

Notes:
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string.
'''

from myLib import *

def rev_char(arr_str):

	str_arr = [ ]
	str_cpr = [ ]
	for i in arr_str: str_arr.append(i)

	last = str_arr[0]
	count = 1
	for i in range(1, len(str_arr)):
		if (str_arr[i] == last):
			count += 1
		else:
		 	str_cpr.append(str_arr[i-1])
		 	str_cpr.append(count)
		 	count = 1
		 	last = str_arr[i]

	str_cpr.append(str_arr[i])
	str_cpr.append(count)

	return(str_cpr)	


def main(argv = None):

	wrd = 'aabcccccaaa'
	res = rev_char(wrd)
	print(res)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)
