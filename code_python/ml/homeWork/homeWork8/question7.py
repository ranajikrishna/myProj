
#
# Name: Homework 8, Question 7 & 8.
#
# Author: Ranaji Krishna.
#
# Notes: In the next two problems, we will experiment with 10-fold cross validation for the 
# polynomial kernel. Because Ecv is a random variable that depends on the random partition 
# of the data, we will try 100 runs with different partitions and base our answer on how 
# many runs lead to a particular choice.:
#
# Question 7:
# Consider the 1 versus 5 classifier with Q = 2. We use Ecv to select 
# C = {0.0001, 0.001, 0.01, 0.1, 1}. If there is a tie in Ecv , select the smaller C . Within the 
# 100 random runs, which value of C yields the smallest Ecv most frequently?
#
# Question 8:
# Again, consider the 1 versus 5 classifier with Q = 2. For the winning selection
# in the previous problem, what is the average value of Ecv?
#




import sys;
import numpy as np;
import random;
import itertools;
from math import *;	 # Math fxns.
import pandas as pd;
import xlrd;

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

import svmutil as svm


def compute (train, test, x, y, C, d):

	options = '-s 0 -t 1 -d ' + str(d) + ' -r 1 -g 1 -q -c ' + str(C); # Set Options.
	prob = svm.svm_problem(np.array(train[3]).tolist(), np.array(train.loc[:,1:2]).tolist());	# Set problem.
	model = svm.svm_train(prob, options);				   # Call libsvm.

	# Evaluate in-sample error. 
	[labels, accuracy, values] = svm.svm_predict(np.array(test[3]).tolist(), np.array(test.loc[:,1:2]).tolist(), model, '-q');

	return(accuracy[0]);

def main(argv = None):

	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.train.xlsx';	 # File location path.
	workbook = xlrd.open_workbook(file_location);
	sheet = workbook.sheet_by_index(0);

	data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]; # Import in-sample data from Excel.
	data_train = pd.DataFrame(data_train, dtype = 'd');						 # Training data.

	# --- Question 7 to 8 ---
	x = 1; y = 5; 
	d = 2;		 # Degrees.
	iteration = 100; # No. iterations.
	
	data_tr = data_train[data_train[0].isin([x,y])];		 # If y is set to a digit. 	
	data_tr[3] = [1 if itr == x else -1 for itr in data_tr[0]];	 # Set classifiers as +1 and -1.

	e_cv = pd.DataFrame(np.ndarray((iteration, 5), dtype = float));  # Store Cross-validation error.	
	for itr in range(0, iteration):
		rows = random.sample(range(0, data_tr.shape[0]), data_tr.shape[0]/10);	# Random sample of rows to be picked.
		data_xtr = data_tr.drop(data_tr.index[rows]);				# Traning sample.
		data_xte = data_tr.iloc[rows];						# Cross-validation sample.

		itr_col = 0;								# Iterator for upper bound.
		# Compute in-sample error for different upper bounds. 
		for itr_C in range(4,-1,-1):
			C = float(1)/10**(itr_C);					# Upper bound.
			e_cv.loc[itr,itr_col] = 1 - 0.01 * compute(data_xtr, data_xte, x, y, C, d); # Compute in-sample error.
			itr_col +=1 ;
	
	min_index = [(e_cv.loc[rows,:]).argmin() for rows in e_cv.index];		# Index of the minimum in-sample error.
 	freq_ = np.bincount(min_index);							# Freq. of indices.
	mean_Ecv = np.mean(e_cv)[1];							# Average in-sample error for C = 0.001.
	print 'Frequency of selection of C = {0.0001, 0.001, 0.01, 0.1, 1}' 
	print(freq_);
	print 'For C = 0.001, mean in-sample error = %f' %mean_Ecv;
	return(0);


if __name__ == '__main__':
	status = main();
	sys.exit(status);
