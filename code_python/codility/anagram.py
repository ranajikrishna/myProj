
#
# Name: Anagram Code
# Author: Ranaji Krishna
#
# Notes: This code requests two strings and checks whether they are
#	 Anagrams.
#

import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.


def getString():

	strArray1 = raw_input("Enter first word: ");	# Word 1
	strArray2 = raw_input("Enter second word: ");	# Word 2

	return(strArray1.lower(), strArray2.lower());	# Return lower case.

def populate(tmpStr1, tmpStr2):
	
	dtry1 = {x:tmpStr1.count(x) for x in tmpStr1};	# Dictionary of first word  (key: letter, value: freq). 
	dtry2 = {x:tmpStr2.count(x) for x in tmpStr2};	# Dictionary of second word (key: letter, value: freq.)

	if (dtry1.keys() != dtry2.keys()):		# Check if the keys (letters) are the same.
		print ("Not an Anagram!");
	elif (dtry1.values() != dtry2.values()):	# Check if the values (freq) are the same.
		print ("Not an Anagram!");
	else:
		print ("Anagram!");
	
	return();

def main(argv=None):
		
	[str1, str2] = getString();
	strList1 = sorted(list(str1));			# Sort list in alphabetical order.
	strList2 = sorted(list(str2));
	
	populate(strList1, strList2);


if __name__ == '__main__':
	status = main();
	sys.exit(status);


