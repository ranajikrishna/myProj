#
# Name: Homework 6, Question 2, 3, 4 , 5 and 6.
#
# Author: Ranaji Krishna.
#
# Notes:
# In the following problems use the data provided in the files
#                 http://work.caltech.edu/data/in.dta
#                 http://work.caltech.edu/data/out.dta
# as a training and test set respectively. Each line of the files 
# corresponds to a two- dimensional input x = (x1, x2), so that X = R2, 
# followed by the corresponding label from Y = {-1, 1}. We are going to apply 
# Linear Regression with a non-linear transformation for classification. The nonlinear 
# transformation is given by \phi(x1, x2) = (1, x1, x2, x21, x2, x1x2, |x1 - x2|, |x1 + x2|).
# Recall that the classification error is defined as the fraction of misclassified points.:
#
# Question: 2
# Run Linear Regression on the training set after performing the non-linear 
# trans- formation. What values are closest (in Euclidean distance) to the in-sample 
# and out-of-sample classification errors, respectively?
#
# Question: 3
# Now add weight decay to Linear Regression, that is, add the term \lambda/N \sum_{i=0}^{7} w_{i=0}^2 to 
# the squared in-sample error, using \lambda = 10k. What are the closest values to the 
# in-sample and out-of-sample classification errors, respectively, for k = -3? 
# Recall that the solution for Linear Regression with Weight Decay was derived in class.
#
# Question: 4
# Now, use k = 3. What are the closest values to the new in-sample and out-of-sample 
# classification errors, respectively?
#
# Question: 5
# What value of k, among the following choices, achieves the smallest out-of-sample 
# classification error?
#
# Question: 6
# What value is closest to the minimum out-of-sample classification error achieved by 
# varying k (limiting k to integer values)?


import sys;
import numpy as np;
import random;
import itertools;
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


def weight_decay(data_IN, data_OUT, lamda, data_REG, data_REG_OUT):

	data_REG[7] = np.ones(len(data_REG))	
	Z = data_REG			# In-sample Regression Data.
	A = np.dot(Z.T, Z)			# Z * Z.
 	
	w_reg = np.dot(np.dot(np.linalg.inv(A + lamda * np.identity(8)), Z.T), data_IN[2])	# Regression weights. 
#print w_reg
	error_IN1 = (sum(abs(np.sign(np.dot(Z, w_reg)) - data_IN[2]))/2)/len(data_REG)   	# In-sample error.

	data_REG_OUT[7] = np.ones(len(data_REG_OUT))	 
	Z = data_REG_OUT			# Out-sample Regression Data.
	A = np.dot(Z.T, Z)			# Z * Z.
	error_OUT1 = (sum(abs(np.sign(np.dot(Z, w_reg)) - data_OUT[2]))/2)/len(data_REG_OUT)	# Out-sample error.
	
	return(error_IN1, error_OUT1)


def ols(data_IN, data_OUT):
	
	data_REG = pd.DataFrame(np.ndarray((len(data_IN),7), dtype = float))	# In-sample Regression Data.
	# ---- Populate ----  
	data_REG[0] = data_IN[0]
	data_REG[1] = data_IN[1]
	data_REG[2] = data_IN[0]**2
	data_REG[3] = data_IN[1]**2
	data_REG[4] = data_IN[0]*data_IN[1]
	data_REG[5] = abs(data_IN[0] - data_IN[1])
	data_REG[6] = abs(data_IN[0] + data_IN[1])

	linReg = LinearRegression()
	linReg.fit(np.array(data_REG), np.array(data_IN[2]).T)			# Regression.
	
	error_IN = (sum(abs(np.sign(linReg.predict(data_REG)) - data_IN[2]))/2)/len(data_IN)	# In-sample error.
	
	data_REG_OUT = pd.DataFrame(np.ndarray((len(data_OUT),7), dtype = float))		# Out-sample Regression Data.
	# --- Populate ---- 
	data_REG_OUT[0] = data_OUT[0]
	data_REG_OUT[1] = data_OUT[1]
	data_REG_OUT[2] = data_OUT[0]**2
	data_REG_OUT[3] = data_OUT[1]**2
	data_REG_OUT[4] = data_OUT[0]*data_OUT[1]
	data_REG_OUT[5] = abs(data_OUT[0] - data_OUT[1])
	data_REG_OUT[6] = abs(data_OUT[0] + data_OUT[1])

	error_OUT = (sum(abs(np.sign(linReg.predict(data_REG_OUT)) - data_OUT[2]))/2)/len(data_OUT)	# Out-sample error.

	return(error_IN, error_OUT, data_REG, data_REG_OUT)

def main(argv = None):

	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork6/data.xlsx'			# File location path.
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	data_IN = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]	# Import in-sample data from Excel.
	data_IN = pd.DataFrame(data_IN, dtype = float)

	sheet = workbook.sheet_by_index(1)
	data_OUT = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]	# Import out-sample data from Excel. 
	data_OUT = pd.DataFrame(data_OUT, dtype = float)

	# --- Question 2 ---	
	[in_err, out_err, data_REG, data_REG_OUT]= ols(data_IN, data_OUT)	# OLS regression.
	print 'In-sample error %f' %in_err
	print 'Out-of-sample error %f' %out_err
	
	# --- Question 3, 4, 5 and 6 ---
	k = -2	
	labda = 10**k
	[in_err1, out_err1]= weight_decay(data_IN, data_OUT, labda, data_REG, data_REG_OUT)	# Weight Decay optimization.
	print 'In-sample error with weight decay %f' %in_err1
	print 'Out-of-sample error with weight decay %f' %out_err1

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)

