#
# Name: Homework 5, Question 8, 9.
#
# Author: Ranaji Krishna.
#
# Notes:
# In this problem you will create your own target function f (probability in this case) and data set D to see 
# how Logistic Regression works. For simplicity, we will take f to be a 0/1 probability so y is a deterministic 
# function of x.
# Take d=2 so you can visualize the problem, and let X = [-1, 1]x[-1, 1] with uniform probability of picking 
# each x \ismem X . Choose a line in the plane as the boundary between f(x) = 1 (where y has to be +1) and f(x) = 0
# (where y has to be -1) by taking two random, uniformly distributed points from X and taking the line passing through
# 4 them as the boundary between y = +1 or -1. Pick N = 100 training points at random from X, and evaluate the outputs 
# yn for each of these points xn. Run Logistic Regression with Stochastic Gradient Descent to find g, and 
# estimate Eout (the cross entropy error) by generating a sufficiently large, separate set of points to evaluate the 
# error. Repeat the experiment for 100 runs with different targets and take the average. Initialize the weight 
# vector of Logistic Regression to all zeros in each run. Stop the algorithm when |w(t-1) - w(t)| < 0.01, 
# where w(t) denotes the weight vector at the end of epoch t. An epoch is a full pass through the N data points 
# (use a random permutation of 1, 2, . . . , N to present the data points to the algorithm within each epoch, 
# and use different permutations for different epochs). Use a learning rate of 0.01.

# Question: 8
# Which of the following is closest to Eout for N = 100?
#
# Question: 9
#
# How many epochs does it take on average for Logistic Regression to converge for N = 100 using the above 
# initialization and termination rules and the specified learning rate? Pick the value that is closest to 
# your results.
#

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
from random import randint

def logistic(tmpSample, eta):					 # Logistic Regression.
	n_train = 100;						 # Training sample.
	w_old = np.array((1,1,1), dtype = float);		 # Old weights.
	w = np.array((0,0,0), dtype = float);			 # New weights.
	perm_array = range(0, n_train);				 # Permutation of poins in training sample.
	epoch = 0;						 # No. epoch iterations.
	error = 0;
	while (np.linalg.norm(w - w_old) > eta):
		epoch += 1;
		w_old = w;
		i = 0;
		while (i < n_train):
			w = w +  eta * (tmpSample[3][perm_array[i]] * tmpSample.iloc[perm_array[i]][0:3])/(1 + exp(tmpSample[3][perm_array[i]] * np.dot(tmpSample.iloc[perm_array[i]][0:3], w)));	# Weight update.
			i += 1;
		
		random.shuffle(perm_array);			 # New permutation of points.
	
	error = 0;
	for i in range (n_train, np.size(tmpSample[0])):
		error += log(1 + exp(-tmpSample[3][i] * np.dot(tmpSample.iloc[i][0:3], w)));	# Cross Entropy error.	
	
	E_out = error/(np.size(tmpSample[0]) - n_train);	 # Out-of-sample error.
	return(E_out,epoch);

def compute(n_samples, eta):

	X = np.random.uniform(-1,1,4);				# Random pts. for True classification line.
	inSample = np.ndarray((n_samples,4), dtype = float);	# Matrix to store values (cols: x-values, y-values, intercept(=-1), identification).
	
	inSample[:,0] = np.random.uniform(-1,1,n_samples);	# x1-values. 
 	inSample[:,1] = np.random.uniform(-1,1,n_samples);	# x2-values.
 	inSample[:,2] = -1*np.ones(n_samples);			# intercept.

	linear_regression_true = LinearRegression();		# Separation line on x-y plane (pts. above this line are identified as +1).
	linear_regression_true.fit(X.reshape((2,2))[:,0:1], X.reshape((2,2))[:,1:2]);	# Fit: Tru.
	
	inSample[:,3,np.newaxis] =  np.sign(inSample[:,1,np.newaxis] - linear_regression_true.predict(inSample[:,0,np.newaxis]));	# Identification.  

	inSample = pd.DataFrame(inSample);			# Convert to DataFrame.
	
	[E_out, epoch] = logistic(inSample, eta);		# Logistic Regression.

	return(E_out,epoch);


def main(arg=None):

	n_samples = 1000;					# Training and testing sample.
	n_reps = 10;
	eta = 0.01;						# Learning rate.
	str_Val = np.ndarray((n_reps,2), dtype = float);
	for i in range(0,n_reps):
		[str_Val[i,0], str_Val[i,1]] = compute(n_samples, eta);
		print i;	

	return(0);

if __name__ == '__main__':
	status = main();
	sys.exit(status);
