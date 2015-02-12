

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

