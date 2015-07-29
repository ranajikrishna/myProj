

# ---------------------------
#
# Name: Homework 2, Question 5,6 and 7.
#
# Author: Ranaji Krishna.
# 
# Notes:  In these problems, we will explore how Linear Regression for classification works. As
# with the Perceptron Learning Algorithm in Homework # 1, you will create your own
# target function f and data set D. Take d = 2 so you can visualize the problem, and
# assume X = [1, -1] x [1, -1] with uniform probability of picking each x \mem X . In
# each run, choose a random line in the plane as your target function f (do this by
# taking two random, uniformly distributed points in [1, -1] x [1, -1] and taking the
# line passing through them), where one side of the line maps to +1 and the other maps
# to -1. Choose the inputs xn of the data set as random points (uniformly in X ), and
# evaluate the target function on each xn to get the corresponding output yn.
#
# Question 5:
# Take N = 100. Use Linear Regression to find g and evaluate Ein, the fraction of
# in-sample points which got classified incorrectly. Repeat the experiment 1000
# times and take the average (keep the g's as they will be used again in Problem
# 6). Which of the following values is closest to the average Ein? (Closest is the
# option that makes the expression |your answer - given option| closest to 0. Use
# this definition of closest here and throughout.)
#
# Question 6: 
# Now, generate 1000 fresh points and use them to estimate the out-of-sample 
# error Eout of g that you got in Problem 5 (number of misclassified out-of-sample points / total number of out-of-sample points).
# Again, run the experiment 1000 times and take the average. Which value is closest to the average Eout?
#
# Question 7:
# Now, take N = 10. After finding the weights using Linear Regression, use them as a vector 
# of initial weights for the Perceptron Learning Algorithm. Run PLA until it converges to a 
# final vector of weights that completely separates all the in-sample points. Among the choices below, 
# what is the closest value to the average number of iterations (over 1000 runs) that PLA takes to converge?
# (When implementing PLA, have the algorithm choose a point randomly from the set of misclassified points at each iteration)
#
# ---------------------------


import sys;
import numpy as np;
import random;
import itertools;
from math import *		        # Math fxns.
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import percepAlgo

def compute(n_samples,outSamples,que):

	X = np.random.uniform(-1,1,4);				# Random pts. for True classification line.
	inSample = np.ndarray((n_samples,7), dtype = float);	# Matrix to store values (cols: x-values, y-values, identification, classification, verification).
	
	inSample[:,0] = np.random.uniform(-1,1,n_samples);		# x1-values. 
 	inSample[:,1] = np.random.uniform(-1,1,n_samples);		# x2-values.

	linear_regression_true = LinearRegression();			# Separation line on x-y plane (pts. above this line are identified as +1).
	linear_regression_true.fit(X.reshape((2,2))[:,0:1], X.reshape((2,2))[:,1:2]);	# Fit: Tru.
	
	inSample[:,2,np.newaxis] =  np.sign(inSample[:,1,np.newaxis] - linear_regression_true.predict(inSample[:,0,np.newaxis]));	# Identification.  
	
	linear_regression_model = LinearRegression();
	linear_regression_model.fit(inSample[:,0:2], inSample[:,2,np.newaxis]);			# Fit: Model
	inSample[:,3,np.newaxis] = np.sign(linear_regression_model.predict(inSample[:,0:2]));	# Regression Classification. 
	
	inSample = pd.DataFrame(inSample);			# Convert to DataFrame.
	inSample[4]=np.where(inSample[2] != inSample[3],0,1);	# Regression Verificaion.	

	# ---- Code for question 6 ---

	outSample = np.ndarray((outSamples,5), dtype = float);
 	outSample[:,0] = np.random.uniform(-1,1,outSamples);		# x1-values. 
 	outSample[:,1] = np.random.uniform(-1,1,outSamples);		# x2-values.

	outSample[:,2,np.newaxis]= np.sign(outSample[:,1,np.newaxis] - linear_regression_true.predict(outSample[:,0,np.newaxis]));	# Estimate value, True.
	outSample[:,3,np.newaxis]= np.sign(linear_regression_model.predict(outSample[:,0:2]));	                # Regression Classification.

	outSample = pd.DataFrame(outSample);				# Convert to DataFrame.
	outSample[4]=np.where(outSample[2] != outSample[3],0,1);	# Regression Verificaion.	
	# --------  

	# ----- Code for question 7 ---
	n_iter = 0
	if (que != 0):
		[percepWgt, n_iter] = percepAlgo.percepAlgo([linear_regression_model.intercept_[0], linear_regression_model.coef_[0][0], linear_regression_model.coef_[0][1]], inSample);



	return(sum(inSample[4]), sum(outSample[4]), n_iter);	

def main (agrv = None):
	
	# --- Question 5 ----
	n_trials = 1000; 	# Total no. trials. 
	n_samples = 100;	# Sample points for Regression classification. 
	inSample_success = np.ndarray((n_trials), dtype = int);	# Store success ratio of each trial.
	# ----
	
	# --- Question 6 ----
	out_samples = 1000;	# Total no. out-sample points.
	outSample_success = np.ndarray((n_trials), dtype = int); # Store success ratio of each trial.
	# -----
	
	for i in range(0,n_trials):
		tmp= compute(n_samples,out_samples,0);	#  In- and out- samples classification analysis.
		inSample_success[i]= tmp[0];	# Compute total no. success classification, in-sample. 
		outSample_success[i]= tmp[1];	# Compute total no. success classification, out-sample. 
		
	print 'In-sample incorrect classification = ', 1- np.mean(inSample_success)/n_samples;
	print 'Out-sample incorrect classification = ', 1- np.mean(outSample_success)/out_samples;

	# --- Question 7 ---
	n_samples = 10;				           # Sample points for Perceptron classification.
	perCep_iter = np.ndarray((n_trials), dtype = int); # Store success ratio of each trial.
	
	for i in range(0,n_trials):
		tmp= compute(n_samples,out_samples,1);	# Perceptron Analysis.
		perCep_iter[i]= tmp[2];			# Store iteration for Perceptron to converge. 

	print 'Average no. iterations for Perceptron convergence = ', np.mean(perCep_iter);
	
	return(0);

if __name__ == '__main__':
	status = main();
	sys.exit(status);
