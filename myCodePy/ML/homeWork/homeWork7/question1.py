#
'''
 Name: Homework 7, Question 1, 2, 3, 4 and 5..

 Author: Ranaji Krishna.

 Notes:
 In the following problems, use the data provided in the files in.dta and out.dta for Homework # 6. 
 We are going to apply linear regression with a nonlinear transformation for classification 
 (without regularization). The nonlinear transformation is given by φ0 through φ7 which transform (x1, x2) into
 			1 x1 x2 x21 x2 x1x2 |x1 -x2| |x1 + x2|
 To illustrate how taking out points for validation affects the performance, we will consider the hypotheses 
 trained on Dtrain (without restoring the full D for training after validation is done).

 Question: 1
 Split in.dta into training (first 25 examples) and validation (last 10 examples). Train on the 25 examples only, 
 using the validation set of 10 examples to select between five models that apply linear regression to \phi_0 
 through \phi_k, with k = 3,4,5,6,7. smallest?

 Question: 2
 Evaluate the out-of-sample classification error using out.dta on the 5 models to see how well the validation 
 set predicted the best of the 5 models. For which model is the out-of-sample classification error smallest?

 Question: 3
 Reverse the role of training and validation sets; now training with the last 10 examples and validating 
 with the first 25 examples. For which model is the classification error on the validation set smallest?

 Question: 4
 Once again, evaluate the out-of-sample classification error using out.dta on the 5 models to see how well 
 the validation set predicted the best of the 5 models. For which model is the out-of-sample classification error smallest?

 Question: 5
 What values are closest in Euclidean distance to the out-of-sample classification error obtained
 for the model chosen in Problems 1 and 3, respectively

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


def ols(data_REG, data_REG_OUT, k, N, M):

	linReg = LinearRegression()
	linReg.fit(np.array(data_REG.loc[0:N,0:k]), np.array(data_REG.loc[0:N,7]).T)	# Regression.

	error_IN = (sum(abs(np.sign(linReg.predict(data_REG.loc[23:M,0:k])) - data_REG.loc[23:M,7]))/2)/len(data_REG.loc[23:M,7])       	# In-sample error.
	
	error_OUT = (sum(abs(np.sign(linReg.predict(np.array(data_REG_OUT.loc[:, 0:k]))) - data_REG_OUT.loc[:, 7]))/2)/len(data_REG_OUT)	# Out-sample error.
	
	return(error_IN, error_OUT)


def compute(data_IN, data_OUT):

	data_REG = pd.DataFrame(np.ndarray((len(data_IN),8), dtype = float))	    # In-sample Regression Data.

	# ---- Populate ----  
	data_REG[0] = data_IN[0]
	data_REG[1] = data_IN[1]
	data_REG[2] = data_IN[0]**2
	data_REG[3] = data_IN[1]**2
	data_REG[4] = data_IN[0]*data_IN[1]
	data_REG[5] = abs(data_IN[0] - data_IN[1])
	data_REG[6] = abs(data_IN[0] + data_IN[1])
	data_REG[7] = data_IN[2]

	data_REG_OUT = pd.DataFrame(np.ndarray((len(data_OUT),8), dtype = float))  # Out-sample Regression Data.

	# --- Populate ---- 
	data_REG_OUT[0] = data_OUT[0]
	data_REG_OUT[1] = data_OUT[1]
	data_REG_OUT[2] = data_OUT[0]**2
	data_REG_OUT[3] = data_OUT[1]**2
	data_REG_OUT[4] = data_OUT[0]*data_OUT[1]
	data_REG_OUT[5] = abs(data_OUT[0] - data_OUT[1])
	data_REG_OUT[6] = abs(data_OUT[0] + data_OUT[1])
	data_REG_OUT[7] = data_OUT[2]
	
	k = 2
	N = 24					# Training sample size.
	M = len(data_IN)-1			
	j = 0

	error_IN = np.ndarray(5)		# Store In-sample error.
	error_OUT = np.ndarray(5)		# Store Out-sample error.
	for itr_k in range (k,7):
	 	[error_IN[j], error_OUT[j]] = ols(data_REG, data_REG_OUT, itr_k, N, M)		# Regression.
		j += 1

	k = 2			
	N = 9					# Training sample size.
	M = len(data_IN)-1
	j = 0

	error_IN_REV = np.ndarray(5)		# Store In-sample error.
	error_OUT_REV = np.ndarray(5)		# Store Out-sample error.
	for itr_k in range (k,7):
	 	[error_IN_REV[j], error_OUT_REV[j]] = ols(data_REG, data_REG_OUT, itr_k, N, M)	# Regresson.
		j += 1
	
	return(error_IN, error_OUT, error_IN_REV, error_OUT_REV)


def main(argv = None):

	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork7/data.xlsx'			# File location path.
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	data_IN = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]	# Import in-sample data from Excel.
	data_IN = pd.DataFrame(data_IN, dtype = float)

	sheet = workbook.sheet_by_index(1)
	data_OUT = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)]	# Import out-sample data from Excel. 
	data_OUT = pd.DataFrame(data_OUT, dtype = float)

	# --- Question 1-5 ---
	err_in = np.ndarray(5)		# Store in-sample error; training size = 25.
	err_out = np.ndarray(5)	# Store out-sample error; training size = 25.	
	err_in_rev = np.ndarray(5)	# Store in-sample error; training size = 10.
	err_out_rev = np.ndarray(5)	# store out-sample error; training size = 10.
	[err_in, err_out, err_in_rev, err_out_rev] = compute(data_IN, data_OUT)
		
	print 'In-sample error with 25 training pts.'
	print err_in
	print 'Out-sample error with 25 training pts.' 
	print err_out
	print 'In-sample error with 10 training pts.'
	print err_in_rev
	print 'In-sample error with 10 training pts.'  
	print err_out_rev

	return(0)
	
if __name__ == '__main__':
	status = main()
	sys.exit(status)

