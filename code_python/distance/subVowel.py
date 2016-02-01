
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

def sub_vowel(letter, cost, oriWord, edits):						# Replace vowels by vowels.
	for i in letter:
		for j in letter:
			if (i.vowel != 0 and j.vowel != 0):
				if(i.isActive() < 0 and j.isActive() > 0):
					freq_i = i.getFreq()[0] - 1;			# Replace letters.
					freq_j = j.getFreq()[0] + 1;
					i.setFreqOne(freq_i);				# Update freq.
					j.setFreqOne(freq_j);
					oriWord[i.pos[0]] = j.alpha;			
					edits.append((i.pos[0], j.alpha));		# Store values for printing the operations performed. 
					i.pos.pop(0);					# Position of remaining letter.
					cost = cost + 0.5;				# Update cost.

	return (cost, oriWord, edits);
