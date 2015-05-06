#
#
# Name: Homework 7, Question 8 - 10.
#
# Author: Ranaji Krishna.
#
# Notes:


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


def compute (data_tr, data_te, x, y, C, d):

	if (y != None):
		data_tr = data_tr[data_tr[0].isin([x,y])];		   # If y is set to a digit. 	
	
	data_tr[3] = [1 if itr == x else -1 for itr in data_tr[0]];	   # Set classifiers as +1 and -1.

	options = '-s 0 -t 1 -d ' + str(d) + ' -r 1 -g 1 -q -c ' + str(C); # Set Options.
	prob = svm.svm_problem(np.array(data_tr[3]).tolist(), np.array(data_tr.loc[:,1:2]).tolist());	# Set problem.
	model = svm.svm_train(prob, options);				   # Call libsvm.

	# Evaluate in-sample error. 
	[labels, accuracy, values] = svm.svm_predict(np.array(data_tr[3]).tolist(), np.array(data_tr.loc[:,1:2]).tolist(), model, '-q');

	return(accuracy[0]);

def main(argv = None):

	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.train.xlsx';	 # File location path.
	workbook = xlrd.open_workbook(file_location);
	sheet = workbook.sheet_by_index(0);

	data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]; # Import in-sample data from Excel.
	data_train = pd.DataFrame(data_train, dtype = 'd');						 # Training data.

	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.test.xlsx';	 # File location path.
	workbook = xlrd.open_workbook(file_location);
	sheet = workbook.sheet_by_index(0);

	data_test = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)];	 # Import in-sample data from Excel.
	data_test = pd.DataFrame(data_test, dtype = float);						 # Testing data.

	# --- Question 2 to 4 ---
	x = 0; y = None; 
	C = 0.01;	# Upper bound.
	d = 2;		# Degrees.
	for itr in range(x,10,2):
		e_in = 1 - 0.01 * compute(data_train, data_test, itr, y, C, d);	# Compute in-sample error.
		print 'Ein for ' + str(itr) + ' versus all = ' + str(e_in);	

	# --- Question 5 ---
	x = 1; y = 5; 
	d = 2;		# Degrees.
	for itr in range(3,-1, -1):
		C = float(1)/10**(itr);
		e_in = 1 - 0.01 * compute(data_train, data_test, x, y, C, d);  # Compute in-sample error.
		print 'Ein for C = ' + str(C) + ' is = ' + str(e_in);	

	# --- Question 6 ---
	x = 1; y = 5; 
	C = 0.01;	# Upper bound.
	d = 2;		# Degrees.
	
	e_in = 1 - 0.01 * compute(data_train, data_test, x, y, C, d);         # Compute in-sample error.
	print 'Ein for C = ' + str(C) + ' and Q = ' + str(d) + ' is = ' + str(e_in);	

	return(0);



if __name__ == '__main__':
	status = main();
	sys.exit(status);


