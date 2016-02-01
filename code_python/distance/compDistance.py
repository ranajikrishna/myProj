
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

import subVowel				# Replace vowel by vowel.
import subSymbol 			# Replace letter by letter.
import delSymbol 			# Delete letter.	
import insertSymbol 			# Insert letter.

from letter import letter		# Class: letter

def distance(letter, oriWord, tgtWord):							# Compute the distance.
	cost = 0; old_cost = 0.1;
	edits = [];									# List to store the operations performed.
	while (cost != old_cost):
		old_cost = cost;
		[cost, oriWord, edits] = subVowel.sub_vowel(letter, cost, oriWord, edits);	# Replace vowels by vowels.
	
	old_cost = 0.1;	
	while (cost != old_cost):
		old_cost = cost;
		[cost, oriWord, edits] = subSymbol.sub_symbol(letter, cost, oriWord, edits);	# Replace letters by letters
	
	[cost, oriWord, edits] = delSymbol.del_symbol(letter, cost, oriWord, edits);		# Delete letters.

	[cost, oriWord, edits] = insertSymbol.ins_symbol(letter, cost, oriWord, tgtWord, edits);	# Insert Letters.

	return(cost, oriWord, edits);

