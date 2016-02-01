
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

import getString			# Get String
import compDistance			# Compute distance.

from letter import letter		# Class: letter.

def permComp():
	strArray1 = raw_input("Enter first letter: ");					# String1.
	strArray2 = raw_input("Enter second letter: ");					# String2.
	
	[uniqLetters, oriWord, tgtWord] = getString.getString(strArray1,strArray2);		# Get unique letters.
	actList = [ ];									# *** Active List: letters that require operations to be performed [to reduce number of permutations] ***
	j = 0;
	for i in uniqLetters:								# Populate Active List.
		if (i.isActive() != 0): 
			actList.append(i.alpha);
			j += 1;
		
	permutations = ["".join(x) for x in itertools.permutations(actList, len(actList))];	# All permutations.

	orgLetter = numpy.ndarray((len(actList),),  dtype = numpy.object);			# Store letters organised as per the order in the permutation.
	strOriWord = list(oriWord);								# String1 as list.
	chk_list = [];										# Store the operations that have been performed before.
	edits_list = [];									# Store unique operations performed and the distance incurred.
	j = 0;
	for i in permutations:									# Iterae through permutations.
		n = 0;
		[uniqLetters, oriWord, tgtWord] = getString.getString(strArray1,strArray2);		# Re-initialise uniqLetters.
		
		for k in list(i):								# Populate orgLetter.
			for m in uniqLetters: 
				if (k == m.alpha): 
					orgLetter[n] = letter();
					orgLetter[n] = m; 
					n +=1 ; 

		[tmp_dis, tmp_oriWord, tmp_edits] = compDistance.distance (orgLetter, list(oriWord), list(tgtWord));		# Compute Distance (sum of costs) & operations performed.
		if (tmp_oriWord == list(tgtWord)):								# If the modified wprd = string2.
			if (sorted(tmp_edits) in chk_list):					# Check if the operation is unique.
				continue;
			else:
				chk_list.append(sorted(tmp_edits));				# Populate chk_list.
				edits_list.append([tmp_dis,tmp_edits]);				# Populate the edits_list.

		oriWord = list(strOriWord);							# Re-initialise to string1.
		j += 1;
 
	return(edits_list);

