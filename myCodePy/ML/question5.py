

# ---------------------------
#
# Name: Question 5, Homework 2.
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
# Take N = 100. Use Linear Regression to find g and evaluate Ein, the fraction of
# in-sample points which got classified incorrectly. Repeat the experiment 1000
# times and take the average (keep the g's as they will be used again in Problem
# 6). Which of the following values is closest to the average Ein? (Closest is the
# option that makes the expression |your answer - given option| closest to 0. Use
# this definition of closest here and throughout.)
#
# ---------------------------


import sys;
import numpy as np;
import random;
import itertools;
from math import *		        # Math fxns.

import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def compute(n_samples):

	X = np.random.uniform(-1,1,4);			# Random pts. for True classification line.
	pts = np.ndarray((n_samples,5), dtype = float);	# Matrix to store values (cols: x-values, y-values, identification, classification, verification).
 	pts[:,0] = np.random.uniform(-1,1,100);		# x-values. 
 	pts[:,1] = np.random.uniform(-1,1,100);		# y-values.

	linear_regression_true = LinearRegression();
	linear_regression_true.fit(X[0:2, np.newaxis], X[2:4]);		# Fit: True.


	pts[:,2] = pts[:,1] - linear_regression_true.predict(pts[:,0,np.newaxis]);	# "Disturbances".  

	for i in range(0,n_samples):
		if(pts[i,2] < 0):
			plt.scatter(pts[i,0], pts[i,1], color = "red");			
			pts[i,2] = -1;							# Identification: +ve Disturbances (above True line).
		else:
			plt.scatter(pts[i,0], pts[i,1], color = "green");
			pts[i,2] = +1;							# Identification: -ve Disturbances (below True line). 

	linear_regression_model = LinearRegression();
	linear_regression_model.fit(pts[:,0, np.newaxis], pts[:,1]);			# Fit: Model
	pts[:,3] = pts[:,1] - linear_regression_model.predict(pts[:,0,np.newaxis]);	# 
	
	pts[:,4] = np.ones(100);
	for i in range(0,n_samples):
		if(pts[i,3] < 0):
			pts[i,3] = -1;							# Classification.
			if(pts[i,2]!=pts[i,3]):
				pts[i,4] = 0;						# Verification: 1 = correct classification (= success).	
		else:
			pts[i,3] = +1;
			if(pts[i,2]!=pts[i,3]):						# Classification.
				pts[i,4] = 0;						# Verification: 1 = correct classification (= success).

	ax = plt.subplot(1,1,1);
    	plt.setp(ax, xticks=(), yticks=());
   	X_test = np.linspace(-1, 1, n_samples);							# Points for plotting.
    	plt.plot(X_test, linear_regression_true.predict(X_test[:, np.newaxis]), label="True");  # Plot True line.
    	plt.plot(X_test, linear_regression_model.predict(X_test[:, np.newaxis]), label="Model", color = "black");   # Plot MOdel line.
	plt.xlim((-1, 1));	# Limits: x-axis [-1,1].
    	plt.ylim((-1, 1));	# Limits: y-axis [-1,1].
    	plt.xlabel("x");	# Lable: x-axis.
    	plt.ylabel("y");	# Lable: y-axis.
   	plt.legend(loc="best"); # Legend.
	#plt.show();		# Show plot.
	return(sum(pts[:,4]));	

def main (agrv = None):
	
	n_trials = 10;		# Total no. trials. 
	n_samples = 100;	# Sample points. 
	str_success = np.ndarray((n_trials), dtype = int);	# Store success ratio of each trial.
	for i in range(0,n_trials):
		str_success[i]= compute (n_samples);		# Compute total no. success classification. 

	print 'Incorrect classification = ', 1- np.mean(str_success)/100;	
	return(0);

if __name__ == '__main__':
	status = main();
	sys.exit(status);
