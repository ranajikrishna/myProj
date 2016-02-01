
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

def ins_symbol(letter, cost, oriWord, tgtWord, edits):					# Insert letters.
	for i in range(len(tgtWord)):
		if (len(oriWord) == len(tgtWord)):					
			break;								# *** Break if the length of modified word > target word [to reduce iterations].***
		elif (len(oriWord) == i):						# Insert letters at the end of the modified word.
			oriWord.insert(i,tgtWord[i]);					# Insert letter
			edits.append((oriWord[i], i));					# Store values for printing the operations performed.
			cost = cost + 3;						# Update cost.
		else:		
			if (oriWord[i] != tgtWord[i]):					# Insert letter at the start or in the middle of the modified word.
				oriWord.insert(i,tgtWord[i]);	
				edits.append((oriWord[i], i));
				cost = cost + 3;

	return(cost, oriWord, edits);

