
import sys;
import numpy;
import random;
import itertools;
from math import *		        # Math fxns.

from letter import letter		# Class : letter.

def getString(strArray1,strArray2):			# Get the statistics of letters.
	
	tmpList = list(strArray1);
	tmpList.extend(list(strArray2));
	tmpList = sorted(set(tmpList));			# Unique letters.
	
	allLetter = numpy.ndarray((len(tmpList),),  dtype = numpy.object);
	
	dtry1 = {x:strArray1.count(x) for x in strArray1};
	dtry2 = {x:strArray2.count(x) for x in strArray2};
	j = 0;
	for i in tmpList:
		allLetter[j] = letter();
		allLetter[j].alpha = i;
		if (i in ['a','e','i','o','u']):	# Check if letter is vowel. 
			allLetter[j].vowel = 1;		
		if (i in dtry1.keys()):
			allLetter[j].setFreqOne(dtry1[i]);					   # Store freq. in string1.
			allLetter[j].pos = [k for k, n in enumerate(strArray1) if n == i];     	   # Store multiple positions.
		else:
			allLetter[j].setFreqOne(0);						   # Set freq. = 0 if letter is not in string1.
		if (i in dtry2.keys()):
			allLetter[j].setFreqTwo(dtry2[i]);					   # Store freq. in string2.
			if (allLetter[j].pos == None):
				allLetter[j].pos = [k for k, n in enumerate(strArray2) if n == i]; # Store position if letter appears in string2 only.
		else:
			allLetter[j].setFreqTwo(0);						   # Set freq- = 0 if letter is not in string2.
		j += 1;
	
	return (allLetter, strArray1, strArray2);

