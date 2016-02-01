
import sys;
import numpy as np;
import random;
import itertools;
from math import *		        # Math fxns.
import pandas as pd


def percepAlgo(perWgt, data):

	n_iter = 0;
	error = "TRUE";
	
	while(error=='TRUE'):
		error = "FALSE";
		data.iloc[:,5] = np.sign(np.dot(data.iloc[:,0:2],perWgt[1:3]) + perWgt[0]); # Perceptron Classification.	
		for i in range(0,len(data)):
			if(data.iloc[i,5] != data.iloc[i,2]):				      
				perWgt[1:3] = perWgt[1:3] + data.iloc[i,2]*data.iloc[i,0:2];	      # Weight update.
				perWgt[0] = perWgt[0] + data.iloc[i,2]*1;
				n_iter += 1;
				error = "TRUE";
		
				
	return(perWgt,n_iter);
