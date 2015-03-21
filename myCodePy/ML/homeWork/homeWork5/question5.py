#
# Name: Homework 5, Questions 5, 6 and 7.
#
# Author: Ranaji Krishna.
#
# Notes:
# Consider the non linear error surface E(u,v) = (ue^v - 2ve^-u)^2. We start at the point # (u,v) = (1,1) and minimize this error using gradient descent in the uv s# pace. 
# Use eta = 0.1 (learning rate, not step size).
# Question 5:
# How many iterations (among the given choices) does it take for the error E(u, v) to # fall below 10^-14 for the first time? In your programs, make sure to use double 
# precision to# get the needed accuracy.
# Question 6:
# After running enough iterations such that the error has just dropped below 10^-14, wh# at are the closest values (in Euclidean distance) among the following choice# to the# final (u, v) you got in Problem 5?
# Question 7:
# Now, we will compare the performance of "coordinate descent". In each iteration, we have two steps along the 
# 2 coordinates. Step 1 is to move only along the u# coordinate to reduce the error (assume first-order 
# approximation holds like in gradient descent), and step 2 is to reevaluate and move only along the v 
# coordinate to reduce the error (again, assume first-order approximation holds). Use the same learning 
# rate of eta = 0.1 as we did in gradient descent. What will the error# E(u,v) be closest to after 15 
# full iterations (30 steps)?


import sys;
import numpy as np;
import random;
import itertools;
from math import *	 # Math fxns.
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.pipeline import Pipeline
from decimal import Decimal
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit


def coord_descent(eta):				# Co-ordinate Descent method.

	error = 1;
	uv = np.array((1,1), dtype = "float");	# Starting co-ordinates of uv.
	itr = 0;
	while (itr < 15):
		dE_du = 2*(exp(uv[1]) + 2*uv[1]*exp(-uv[0]))*(uv[0]*exp(uv[1])-2*uv[1]*exp(-uv[0]));	# Partial differential wrt u.
		dE_dv = 0								
		error_vec = np.array((dE_du, dE_dv), dtype = "float");					# Error vector.
		mag = (dE_du**2 + dE_dv**2)**(0.5);							# Magnitude (not used!).
		
		v_unit = -1 * error_vec;								# Direction of steepest descent.
		uv[0] = uv[0] + eta * v_unit[0];							# New u co-ordinates.

		dE_dv = 2*(uv[0]*exp(uv[1]) - 2*exp(-uv[0]))*(uv[0]*exp(uv[1])-2*uv[1]*exp(-uv[0]));	# Partial differential wrt v.
	
		dE_de = 0;
		error_vec = np.array((dE_du, dE_dv), dtype = "float");					# Error vector.
		mag = (dE_du**2 + dE_dv**2)**(1/2);							# Magnitude (not used!).
		
		v_unit = -1 * error_vec;								# Direction of steepest descent.
		uv[1] = uv[1] + eta * v_unit[1];							# New v co-ordinates.	

		error =	(uv[0]*exp(uv[1]) - 2*uv[1]*exp(-uv[0]))**2; 					# Error.
		itr += 1;		


	return(itr, uv, error);

	
def grad_descent(eta):				# Gradient Decent method.

	error = 1;
	uv = np.array((1,1), dtype = "float");	# Starting co-ordinate.
	itr = 0;
	while (error > 10**(-14)):		# Error bound.
		dE_du = 2*(exp(uv[1]) + 2*uv[1]*exp(-uv[0]))*(uv[0]*exp(uv[1])-2*uv[1]*exp(-uv[0]));	# Partial differential wrt u.
		dE_dv = 2*(uv[0]*exp(uv[1]) - 2*exp(-uv[0]))*(uv[0]*exp(uv[1])-2*uv[1]*exp(-uv[0]));	# Partial differential wrt v.
	
		error_vec = np.array((dE_du, dE_dv), dtype = "float");					# Error vector.
		mag = sqrt(dE_du**2 + dE_dv**2);							# Magnitude (not used!).	
		
		v_unit = -1 * error_vec;								# Direction of steepest decent.	
		uv = uv + eta * v_unit;									# New (u,v) co-ordinates.	

		error =	(uv[0]*exp(uv[1]) - 2*uv[1]*exp(-uv[0]))**2; 					# Error.	
		itr += 1;		
			
	return(itr, uv);
			
	



def main (argv = None):

	eta = 0.1; 

	# --- Question 5 & 6 --- 
	[itr, uv] = grad_descent (eta);
	print 'Iterations taken = %d' %itr;
	print 'Weights = ' 
	print(uv);

	# --- Question 7 ---
	[itr, uv, error] = coord_descent (eta);
	print 'Error after 30 steps = %f' %error;



if __name__ == '__main__':
	status = main();
	sys.exit(status);
	
