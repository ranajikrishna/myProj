#
# Name: Homework 7, Question 7..
#
# Author: Ranaji Krishna.
#
# Notes:
# You are given the data points (x, y): (-1, 0), (\rho, 1), (1, 0), \rho >= 0, 
# and a choice between two models: constant { h0(x) = b } and linear { h1(x) = ax + b }. 
# For which value of \rho would the two models be tied using leave-one-out 
# cross-validation with the squared error measure?


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


def ols(data_REG):

	wgt = np.ndarray(2);				# Store weights.
	linReg = LinearRegression();
	X = data_REG.loc[:,0];	Y = data_REG.loc[:,1];	# Ind. variable.
	linReg.fit(X[:,np.newaxis], Y);	# Regression.
	wgt[0] = linReg.coef_;				# a.
	wgt[1] = linReg.intercept_;			# b.

	w_con = np.mean(data_REG.loc[:,1]);		# 0.5 * (y1 + y2).

	return(wgt,w_con);
	
def compute(rho):

	data = pd.DataFrame(np.ndarray((3,4), dtype = float));	# Store x, y, linear est., constant.

	# --- Populate 'data' ---
	data.loc[0][0] = -1;  data.loc[0][1] = 0;
	data.loc[1][0] = rho; data.loc[1][1] = 1;
	data.loc[2][0] = 1;   data.loc[2][1] = 0;

	w_lin = np.ndarray(2);	
	for i in range(0,3):
		[w_lin, data.loc[i,3]]  = ols(data.drop([i])); 	# Regression.
		# Cross-validation
		data.loc[i,2] = w_lin[0] * data.loc[i,0] + w_lin[1] * data.loc[i,1];
	
	return(data);

def main(argv = None):

	rho = sqrt(sqrt(3) + 4);
	data = compute(rho);
	# Mean-square error. 
	mse = 0.5 * ((data.loc[0,2] - data.loc[0,3])**2 + (data.loc[2,2] - data.loc[2,3])**2);
	print 'For (a), mse = %f' %mse;

	rho = sqrt(sqrt(3) - 1);
	data = compute(rho);
	# Mean-square error. 
	mse = 0.5 * ((data.loc[0,2] - data.loc[0,3])**2 + (data.loc[2,2] - data.loc[2,3])**2);
	print 'For (b), mse = %f' %mse;
	
	rho = sqrt(4*sqrt(6) + 9);
	data = compute(rho);
	# Mean-square error. 
	mse = 0.5 * ((data.loc[0,2] - data.loc[0,3])**2 + (data.loc[2,2] - data.loc[2,3])**2);
	print 'For (c), mse = %f' %mse;

	rho = sqrt(-1*sqrt(6) + 9);
	data = compute(rho);
	# Mean-square error. 
	mse = 0.5 * ((data.loc[0,2] - data.loc[0,3])**2 + (data.loc[2,2] - data.loc[2,3])**2);
	print 'For (d), mse = %f' %mse;
	
	return(0);

if __name__ == '__main__':
	status = main();
	sys.exit(status);

