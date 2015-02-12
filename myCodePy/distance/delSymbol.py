
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

def del_symbol(letter, cost, oriWord, edits):						# Delete letters.
	rec_del = [];									# Record positions of letters deleted.
	for i in letter:
		if (i.isActive != 0):
			while (i.getFreq()[0] > i.getFreq()[1]):
				i.setFreqOne(i.getFreq()[0] - 1);
				adj_del = sum(k < i.pos[0] for k in rec_del);		# Adjust position of delete if position of previous delete is less than the positiono of current delete.
				del[oriWord[i.pos[0] - adj_del]];			# Delete letter.
				rec_del.append(i.pos[0]);				# Record the position of deleted letter.
				edits.append((i.pos[0] - adj_del));			# Store values for printing the operations performed.
				i.pos.pop(0);						# Position of remaning letter.
				cost = cost + 2;					# Update cost.

	return (cost, oriWord, edits);

