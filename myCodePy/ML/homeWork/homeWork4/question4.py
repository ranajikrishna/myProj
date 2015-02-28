#
# Name: Homework 4, Questions 4, 5, 6 and 7.
#
# Author: Ranaji Krishna.
#
# Notes:
# Consider the case where the target function f :[-1,1] -> R is given by f(x) = sin(pi*x)
# and the input probability distribution is uniform on [-1,1]. Assume that the training
# set has only two examples (picked independently), and that the learning algorithm
# produces the hypothesis that minimizes the mean squared error on the examples.
#
# Question: 4
# Assume the learning model consists of all hypotheses of the form h(x) = ax.
# What is the expected value, \hat{g}(x), of the hypothesis produced by the learning
# algorithm (expected value with respect to the data set)? Express your \hat{g}(x) as
# \hat{a}x , and round \hat{a} to two decimal digits only, then match exactly to one of the
# following answers.
#
# Question: 5
# What is the closest value to the bias in this case? 
#
# Question: 6
# What is the closest value to the variance in this case?
#
# Question: 7
# Now, let us chang H. Which of the following learning models has the least
# expected value of out-of-sample error?
# 
# --------------------- 

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


def func_c(x, a, b):			# Hypothesis: ax + b.
	return(a*x + b);

def func_e(x, a, b):			# Hypothesis: ax^2 + b.
	return(a*x**2 + b);


def compute(n_iter):

	uni_rand = np.random.uniform (-1, 1, 2*n_iter);	 # Uniformly distributed random numbers.

	# --- Store coefficients ----
	str_coef_b = pd.DataFrame(np.ndarray((n_iter,1), dtype = float));	
	str_coef_a = pd.DataFrame(np.ndarray((n_iter,1), dtype = float));
	str_coef_c = pd.DataFrame(np.ndarray((n_iter,2), dtype = float));
	str_coef_d = pd.DataFrame(np.ndarray((n_iter,1), dtype = float));
	str_coef_e = pd.DataFrame(np.ndarray((n_iter,2), dtype = float));

	str_bias = pd.DataFrame(np.ndarray((n_iter,5), dtype = float));		# Store bias.
	str_var = pd.DataFrame(np.ndarray((n_iter,5), dtype = float));		# Store variance.

	linReg = LinearRegression();

	# --- Compute coefficients ---
	for i in range(0, n_iter):

	        str_coef_b.iloc[i] = (sin(pi * uni_rand[i]) * uni_rand[i] + sin(pi * uni_rand[i+1]) * uni_rand[i+1])/ (uni_rand[i]**2 + uni_rand[i+1]**2); 	# Hypothesis: ax.	
	
		str_coef_a.iloc[i] = 0.5 * (sin(pi * uni_rand[i]) + sin(pi * uni_rand[i+1]));									# Hypothesis: b.
		
		#linReg.fit(np.array([uni_rand[i],uni_rand[i+1]])[np.newaxis].T,np.array([sin(pi*uni_rand[i]),sin(pi*uni_rand[i+1])])[np.newaxis].T);
		#str_coef_c.iloc[i] = [linReg.coef_[0],linReg.intercept_];	# Compute coeff. of ax + b using Linear regression. 
		str_coef_c.iloc[i] = curve_fit(func_c, np.array([uni_rand[i], uni_rand[i+1]]), np.array([sin(pi * uni_rand[i]), sin(pi * uni_rand[i+1])]))[0];	# Hypothesis: ax + b.			
		
		str_coef_d.iloc[i] = (sin(pi * uni_rand[i]) * uni_rand[i]**2 + sin(pi * uni_rand[i+1]) * uni_rand[i+1]**2)/ (uni_rand[i]**4 + uni_rand[i+1]**4);# Hypothesis: ax^2.
	
		str_coef_e.iloc[i] = curve_fit(func_e, np.array([uni_rand[i], uni_rand[i+1]]), np.array([sin(pi * uni_rand[i]), sin(pi * uni_rand[i+1])]))[0];	# Hypothesis: ax^2 + b.			
	# --- Compute bias and variance ---
	uni_rand = np.random.uniform (-1, 1, 2*n_iter);
	for i in range(0, n_iter):
		str_bias.iloc[i][0] = (np.mean(str_coef_b[0])*uni_rand[i] - sin(pi * uni_rand[i]))**2;					# Hypothesis: ax.
		str_var.iloc [i][0] = (str_coef_b.iloc[i][0] * uni_rand[i] - np.mean(str_coef_b[0]) * uni_rand[i])**2;		
		
		str_bias.iloc[i][1] = (np.mean(str_coef_a[0]) - sin(pi * uni_rand[i]))**2;						# Hypothesis: b.
		str_var.iloc[i][1] = (np.mean(str_coef_a.iloc[i][0]) - np.mean(str_coef_a[0]) * uni_rand[i])**2;
		
		str_bias.iloc[i][2] = (np.mean(str_coef_c[0]) * uni_rand[i] + np.mean(str_coef_c[1]) - sin(pi * uni_rand[i]))**2;	# Hypothesis: ax + b.
		str_var.iloc [i][2] = (str_coef_c.iloc[i][0] * uni_rand[i] + str_coef_c.iloc[i][1] - (np.mean(str_coef_c[0]) * uni_rand[i] + np.mean(str_coef_c[1])))**2;
		
		str_bias.iloc[i][3] = (np.mean(str_coef_d[0]) * uni_rand[i]**2 - sin(pi * uni_rand[i]))**2;				# Hypothesis: ax^2.
		str_var.iloc [i][3] = (str_coef_d.iloc[i][0] * uni_rand[i]**2 -  np.mean(str_coef_d[0]) * uni_rand[i]**2)**2;
		
		str_bias.iloc[i][4] = (np.mean(str_coef_e[0]) * uni_rand[i]**2 + np.mean(str_coef_e[1]) - sin(pi * uni_rand[i]))**2;	# Hypothesis: ax^2 + b.
		str_var.iloc [i][4] = (str_coef_e.iloc[i][0] * uni_rand[i]**2 + str_coef_e.iloc[i][1] - (np.mean(str_coef_e[0]) * uni_rand[i]**2 + np.mean(str_coef_e[1])))**2;

	return(np.mean(str_coef_b), np.mean(str_bias), np.mean(str_var));

def main(argv = None):

	n_samples = 10000;				# No. samples.

	[coeff, bias, variance] = compute(n_samples);	# Analysis.

	# --- Question 5 & 6 ---
	print 'Average coefficient %f' %coeff;
	print 'Bias %f' %bias[0];
	print 'Variance %f' %variance[0];

	# --- Question 7 ---
	
	Eout = bias + variance; 			# Out-of-sample error. 
	print 'Out-of-sample error'; 
	print(Eout);


if __name__ == '__main__':
	status = main();
	sys.exit(status);l
