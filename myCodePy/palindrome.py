
#
# Name: Palindrome code.
# Author: Ranaji Krishna.
#
# Notes: The code requests a string and evaluates whether it is a 
#	 Palindrome.
#


import sys;
import numpy;
from random import*
import itertools;
from math import*
from decimal import*

def main(argv = None):
	strArray1 = raw_input("Enter Word:");		# Request word. 
	strArray2 = strArray1.replace(" ","").replace(",","").replace("!","").replace(":","").replace(".","").replace("-","");		# Remove characters , ! : . - from the string.
	strArray = list(strArray2.lower());
	i = 0;
	j = 0;
	while(i <= int(0.5*(len(strArray) - 1))):	# Check if the letters progressing from the start and end are the same.
		if(strArray[i] != strArray[int(len(strArray)) - i - 1]):	# If letters are not the same. 
			j = 1;
			print("Not a Palindrome");	
			break;
		else:
			i += 1;
	
	if(j != 1):	
		print("Is a Palindrome");


if __name__ == '__main__':
	status = main();
	sys.exit(status);

