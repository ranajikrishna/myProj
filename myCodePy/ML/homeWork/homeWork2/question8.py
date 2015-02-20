
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


def compute(n_samples):
	
	# Matrix to store values (cols: x-values, y-values, identification,  classification (non-trans), 
	# verification (non. trans), classify (trans.), verify (trans.)).
	X = pd.DataFrame(np.ndarray((n_samples,7), dtype = float));

	X[0] = np.random.uniform(-1,1,n_samples);	# x1_value. 	
	X[1] = np.random.uniform(-1,1,n_samples);	# x2_value.
	X[2] = np.sign(X[0]**2 + X[1]**2 - 0.6);	# y_value.

	select = random.sample(range(1, 1000), 100);	# Select 10% rando pts. to add noise
	X[2][select] = X[2][select]*-1;			# Flip the signs to add noise.

	linReg_non = LinearRegression();		# Linear regression on non-tranformed fxn.
	linReg_non.fit(X[[0,1]],X[2]);			# Regress.

	X[3] = np.sign(linReg_non.predict(X[[0,1]]));	# Classification.
	
	X[4] = np.where(X[2] != X[3],0,1);		# Non- transformed regression verificaion.
	
	# ---- Question 9 ----
	linReg = LinearRegression();
	
	tmpData = [X[0], X[1], X[0]*X[1], X[0]**2, X[1]**2];
	data = pd.concat(tmpData, axis = 1);
	linReg.fit(data, X[2]);

	X[5] = np.sign(linReg.predict(data));		# Classification.

	X[6] = np.where(X[2] != X[5],0,1);		# Transformed regression verificaion.

	wgt = [linReg.intercept_, linReg.coef_];

	# ---- Question 10 ----
	
	X_out = pd.DataFrame(np.ndarray((n_samples,5), dtype = float));	# Matrix to store values (cols: x-values, y-values, identification, classification, verification).

	X_out[0] = np.random.uniform(-1,1,n_samples);	# x1_value. 	
	X_out[1] = np.random.uniform(-1,1,n_samples);	# x2_value.
	X_out[2] = np.sign(X_out[0]**2 + X_out[1]**2 - 0.6);	# y_value.

	select = random.sample(range(1, 1000), 100);	# Select 10% rando pts. to add noise
	X_out[2][select] = X_out[2][select]*-1;		# Flip the signs to add noise.
	
	tmpData = [X_out[0], X_out[1], X_out[0]*X_out[1], X_out[0]**2, X_out[1]**2];
	data = pd.concat(tmpData, axis = 1);
	linReg.fit(data, X_out[2]);

	X_out[3] = np.sign(linReg.predict(data));	# Classification

	X_out[4] = np.where(X_out[2] != X_out[3],0,1);	# Transformed regression verificaion.

	return(sum(X[4]), wgt, sum(X_out[4]));




def main(argv = None):
	
	n_trials = 1000;	# No. trials.
	n_samples = 1000;	# No. samples.
	str_Ein = pd.DataFrame(np.ndarray((n_trials), dtype = float));		# In-sample Error.
	str_coeff = pd.DataFrame(np.ndarray((n_trials,6), dtype = float));	# Coefficients.
	str_Eout = pd.DataFrame(np.ndarray((n_trials), dtype = float));		# Out-sample Error
	for i in range(0,n_trials):
		tmp = compute(n_samples);		# Analysis.
		str_Ein[0][i] = tmp[0];
		str_coeff.iloc[i][0] = tmp[1][0];
		str_coeff.iloc[i][1:6] = tmp[1][1];
		str_Eout[0][i] = tmp[2];

	print 'Average in-sample error', 1-np.mean(str_Ein[0])/n_samples; 	
	print 'Coefficients \n', np.mean(str_coeff); 	
	print 'Average out-sample error', 1-np.mean(str_Eout[0])/n_samples; 	

	return(0);	
	

if __name__ == '__main__':
	status = main();
	sys.exit(status);
