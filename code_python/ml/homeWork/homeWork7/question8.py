#
'''
 Name: Homework 7, Question 8 - 10.

 Author: Ranaji Krishna.

 Notes:
 Notice: Quadratic Programming packages sometimes need tweaking and have numeri- cal issues, and this 
 is characteristic of packages you will use in practical ML situations. Your understanding of support
 vectors will help you get to the correct answers.
 In the following problems, we compare PLA to SVM with hard margin1 on linearly separable data sets.
 For each run, you will create your own target function f and data set D. Take d = 2 and choose a random
 line in the plane as your target function f (do this by taking two random, uniformly distributed
 points on [-1, 1] x [-1, 1] and taking the line passing through them), where one side of the line 
 maps to +1 and the other maps to -1. Choose the inputs xn of the data set as random points 
 in X = [-1, 1] x [-1, 1], and evaluate the target function on each xn to get the corresponding 
 output yn. If all data points are on one side of the line, discard the run and start a new run.
 Start PLA with the all-zero vector and pick the misclassified point for each PLA iteration at 
 random. Run PLA to find the final hypothesis gPLA and measure the disagreement between f 
 and gPLA as P[f(x) ~= gPLA(x)] (you can either calculate this exactly, or approximate it by 
 generating a sufficiently large, separate set of points to evaluate it). Now, run SVM
 on the same data to find the final hypothesis gSVM by solving
 			min (w,b)  0.5 * w^Tw
			s.t. y_n(w^T* x_n + b) >= 1
 using quadratic programming on the primal or the dual problem. 
 Measure the dis-agreement between f and gSVM as P[f(x) ~= gSVM(x)], and count the number of 
 support vectors you get in each run.
 Question 8:
 For N = 10, repeat the above experiment for 1000 runs. How often is gSVM better than gPLA in approximating f?
 Question 9:
 For N = 100, repeat the above experiment for 1000 runs. How often is gSVM better than gPLA in approximating f? 
 Question 10:
 For the case N = 100, which of the following is the closest to the average number of support 
 vectors of gSVM (averaged over the 1000 runs)?
'''

import sys
import numpy as np
import random
import itertools
from math import *	 # Math fxns.
import pandas as pd
import xlrd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.pipeline import Pipeline
from decimal import Decimal
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from random import randint
from cvxopt import blas, lapack, matrix, solvers
solvers.options['show_progress'] = 0
from scipy import linalg as LA
from numpy.linalg import matrix_rank

import percepAlgo


def compute(n_samples, outSamples, que):

	X = np.random.uniform(-1,1,4)				# Random pts. for True classification line.
	inSample = np.ndarray((n_samples,4), dtype = float)	# Matrix to store values (cols: x-values, y-values, identification, classification, verification).
	
	inSample[:,0] = np.random.uniform(-1,1,n_samples)	# x1-values. 
 	inSample[:,1] = np.random.uniform(-1,1,n_samples)	# x2-values.

	linear_regression_true = LinearRegression()		# Separation line on x-y plane (pts. above this line are identified as +1).
	linear_regression_true.fit(X.reshape((2,2))[:,0:1], X.reshape((2,2))[:,1:2])	# Fit: Tru.
	
	inSample[:,2,np.newaxis] =  np.sign(inSample[:,1,np.newaxis] - linear_regression_true.predict(inSample[:,0,np.newaxis]))	# Identification.  
	
	inSample = pd.DataFrame(inSample)			# Convert to DataFrame.

	# --- Perceptron Learning Algorithm ---	
	n_iter = 0
	if (que != 0):
		[percepWgt, n_iter] = percepAlgo.percepAlgo([0,0,0], inSample)
	
	outSample = np.ndarray((outSamples,7), dtype = float)
 	outSample[:,0] = np.random.uniform(-1,1,outSamples)	# x1-values. 
 	outSample[:,1] = np.random.uniform(-1,1,outSamples)	# x2-values.

	outSample[:,2,np.newaxis]= np.sign(outSample[:,1,np.newaxis] - linear_regression_true.predict(outSample[:,0,np.newaxis]))	# Estimate value, True.

	outSample = pd.DataFrame(outSample)			# Convert to DataFrame.

	outSample[3] = np.sign(percepWgt[0] + np.dot(percepWgt[1:3],outSample.loc[:,0:1].T))	# Estimate value, True.

	outSample[4] = np.where(outSample[2] != outSample[3],0,1)	# Perceptron Classification Verificaion.	

	# --- Support Vector Machines ---
 	m = matrix(inSample.loc[:,0:1].as_matrix(), tc = 'd')
	M = m * m.T
 	y = matrix(inSample.loc[:,2].as_matrix(), tc = 'd')
        Y = y * y.T
	P = matrix(np.multiply(M,Y), tc = 'd')
	q = matrix(-1 * np.ones(n_samples), tc = 'd')
	A = matrix(inSample[2], tc = 'd')
	b = matrix(np.zeros(1), tc = 'd')
	G1 = matrix(np.diag(np.ones(n_samples) * -1), tc = 'd')
	G2 = matrix(np.diag(np.ones(n_samples)), tc = 'd')
	G  = matrix([[G1,G2]])
	h1 = matrix(np.zeros(n_samples), tc = 'd')
	h2 = matrix(np.ones(n_samples) * float("inf"), tc = 'd')
	h  = matrix([[h1,h2]])
	
	# ---- Convex Optimization ----
	solvers.options['abstol'] = 1e-9	 
	solvers.options['reltol'] = 1e-8	 
	solvers.options['feastol'] = 1e-9	 
	
	sol = solvers.qp(P,q,G1,h1,A.T,b)	# Run convex optimisation.
	alpha = np.ravel(sol['x'])	# Alpha's.
	position = np.where(alpha>1)		# All \alpha > 0.
	max_itr = np.argmax(alpha)		# \alpha chose to calculate intercept (b).
	# -----------

	w = sum(matrix(np.multiply(matrix(np.array(alpha)), matrix(inSample[2])), tc = 'd') * inSample.loc[:,0:1].as_matrix())	# SVM weights.
	
        c = inSample.loc[max_itr, 2] - np.dot(w, inSample.loc[max_itr, 0:1].T)
	
	outSample[5] = np.sign(np.dot(w, outSample.loc[:,0:1].T) + c)	# Estimate value using SVM, True.
	outSample[6] = np.where(outSample[2] != outSample[5],0,1)	# SVM Classification Verificaion.	
	return(sum(outSample[4]), sum(outSample[6]), len(position[0]))

def main(argv = None):

	n_inSample = 10	# Training sample size.
	n_outSample = 1000	# Testing sample size.
	n_runs = 100		# No. repeated trials.
	count_ = 0		# Out-performance of SVM over PLA.
	tot_sv = 0		# Total no. Support Vectors.

	for i in range(0,n_runs):
		[pla, svm, n_sv]= compute(n_inSample, n_outSample, 1)	# Return: Correct classifications by pla, svm and number of support vetors. 
		tot_sv += n_sv						# Sum the no. support vectors.
		#print(i);
		if (pla <= svm):
			count_ += 1					# No. times svm is better than pla.
		
	per_outPer = 100 * float(count_) / n_runs	# Percentage out-performance of SVM over PLA.
	av_sv = float(tot_sv)/n_runs			# Average no. Support Vectors.

	print 'Percentage of out-performance of SVM over PLA = %f' %per_outPer
	print 'Average Number of Support-Vectors = %f' %av_sv
	
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
