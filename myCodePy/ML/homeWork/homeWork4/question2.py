
#
# Name: Home Work 4, Question 2 and 3.
# Author: Ranaji Krishna.
#
# Question 2:
# There are a number of bounds on the generalization error, all holding with
# probability at least 1-delta. Fix dvc = 50 and delta = 0.05 and plot these bounds as a
# function of N. Which bound is the smallest for very large N, say N = 10, 000?
# 
# Question 3:
# For the same values of dvc and delta of Problem 2, but for small N, say N = 5,
# which bound is the smallest?
#

import sys
import numpy as np
import random
import itertools
from math import *	 # Math fxns.
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.pipeline import Pipeline
from decimal import Decimal

def compute (n_samples, start, k, delta, d_vc):
	strValues = pd.DataFrame(np.ndarray((4, (n_samples+5*k-start)/k), dtype = float))		# Store Generalization error values.
	j = 0		
	for i in range(start, n_samples + 5*k, k):
		strValues.iloc[0][j] = sqrt(8./i * log((4*(2*i)**d_vc)/delta)) 			# Original VC Bound.
		strValues.iloc[1][j] = sqrt(2*log(2*i*i**d_vc)/i) + sqrt(2./i * log(1./delta) + 1./i)  # Rademacher Penalty bound.
		m = 1./i + 0.5 * sqrt(4./i * (1./i + log((6*(2*i)**d_vc)/delta))) 			# Parrondo and Van der Broek.
		if (m < 0):
			strValues.iloc[2][j] = 1./i - 0.5 * sqrt(4./i * (1./i + log((6*(2*i)^d_vc)/delta))) 
		else:
			strValues.iloc[2][j] = m

		m = 4./(2*i - 4) + 0.5 * sqrt((4./(2*i - 4))**2 + 4 * (log(4)+2*d_vc*log(i)-log(delta)) /(2*i - 4)) 	# Devroye. 
		
		if (m < 0):
			strValues.iloc[3][j] =  4./(2*i - 4) - 0.5 * sqrt((4./(2*i - 4))**2 + 4 * (log(4)+2*d_vc*log(i)-log(delta)) /(2*i - 4))
		else:
			strValues.iloc[3][j] = m
	
		j += 1

	# --- Plot ---
	x_axis = range(start, n_samples+5*k, k)
	plt.plot(x_axis, strValues.iloc[0], color = 'r', label = "a")
	plt.plot(x_axis, strValues.iloc[1], color = 'b', label = "b")
	plt.plot(x_axis, strValues.iloc[2], color = 'g', label = "c")
	plt.plot(x_axis, strValues.iloc[3], color = 'k', label = "d")

	plt.xlabel("No. samples")
	plt.ylabel("Generalization error")

	plt.grid()
	plt.legend()
	
	plt.show()
	# ---- #

	return(0)


def main(argv = None):

	delta = 0.05		# Bound.	
	d_vc = 50		# VC - dimensions.

	# --- Question 2 ---
	N = 10000		# No. samples.
	step = 100		# Increament steps.
	compute(N, step, step, delta, d_vc)
	
	# --- Question 3 ---
	N = 5			# No. samples.
	step = 1		# Increment steps.
	start = 3		# Starting point.
	compute(N, start, step, delta, d_vc)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
