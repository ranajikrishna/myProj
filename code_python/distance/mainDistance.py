
# -------------------------------
#
# Name: Distance computing code.
# Author: Ranaji Krishna.
#
# Notes: 
#
# The edit distance is defined by the series of operations that  transforms the second string into the first one.  The allowed operations are: 
# -	Insertion of a character
# -	Deletion of a character
# -	Substitution of a character for another
# For example, the string “kitten” can be transformed into “splitting” as follows: substitute “k” with “s”, insert “p” at position 1, 
# insert “l” at position 2, substitute “e” with “I”, and insert “g” at the end. The sequence of operations is not unique; another possibility 
# is to delete the “k” (one operation), then insert “s” “p” and “l”. Each operation incurs a cost. 
# The edit distance is the cost of the minimum-cost series of operations that accomplishes the desired transformation.
#  
# For this problem, the strings will be composed only of letters a-zA-Z. The costs of the operations are as follows:
# -	insertion of a symbol, cost 3
# -	deletion of a symbol, cost 2
# -	substitution of a vowel with another vowel, cost 0.5 (vowels are aeiouAEIOU)
# -	substitution of a symbol with another (where not both are vowels), cost 1
# 
# The program should take as arguments the two strings, and write out the edit distance (the cost of the minimum-cost sequence of operations), 
# as well as the operations themselves. 
#
# Here is the output that should be generated foir the example above:
# 
# Edit distance: 10.5
# Operations:
#   Replace character from position 0 with character s
#   Insert character p at position 1
#   Insert character l at position 2
#   Replace character from position 6 with e
#   Insert character g at position 8
# 
# If there are several sequences with the same cost, print them all out.
#
# --------------------------------


import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

import getString			# Get String 
import subVowel				# Replace vowel by vowel.
import subSymbol 			# Replace letter by letter.
import delSymbol 			# Delete letter.	
import insertSymbol 			# Insert letter.
import compDistance 			# Computes distance..
import computePermutation		# Total Distance and Operations performed..

from letter import letter		# Class: letter.

def main(argv=None):

	edits  = computePermutation.permComp();				# Get Distance and the Operations performed.
	for i in edits:
		print("Distance = " + str(i[0]));			# Print Distance.	
		for j in i[1]:
			if (type(j) != type(0)):			# Operation: *not* Delete.
				if(type(j[0]) == type(0)):		# Operation: Replace.
					print("replace character from position " + str(j[0]) + " by " + j[1]);
					a = 9;	
				else:					# Operation: Insert.
					print("insert character " + j[0] + " at position " + str(j[1]));
			else:						# Operation: Delete
				print("delete character in position " + str(j));
			
	return None;

if __name__ == '__main__':
	status = main();
	sys.exit(status);	

