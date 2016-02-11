'''
 Name: Classification using linear regression.

 Author: Ranaji Krishna.

 Note: The code below solves the following problem:

 We are going to experiment with linear regression for classification on the 
 processed US Postal Service Zip Code data set from Homework 8. Download the 
 data (extracted features of intensity and symmetry) for training and testing:
               http://www.amlbook.com/data/zip/features.train
		http://www.amlbook.com/data/zip/features.test
 (the format of each row is: digit intensity symmetry). We will train two types 
 of binary classifiers; one-versus-one (one digit is class +1 and another digit 
 is class -1, with the rest of the digits disregarded), and one-versus-all 
 (one digit is class +1 and the rest of the digits are class -1). When 
 evaluating Ein and Eout, use binary classification error. 
 Implement the regularized least-squares linear regression for classification 
 that minimizes
		(1/N) \sum_{n=1}^N (w^T z_n - y_n)^2 + \alpha/N w^T w
 where w includes w0.

 Question: 1
 Set \lambda = 1 and do not apply a feature transform (i.e., use 
 z = x = (1,x1,x2)). Which among the following classifiers has the lowest Ein?

 Question: 2
 Now, apply a feature transform z = (1,x1,x2,x1x2,x21,x2), and set \lambda= 1. 
 Which among the following classifiers has the lowest Eout?#

 Question: 3
 If we compare using the transform versus not using it, and apply that to 
 '0 versus all' through '9 versus all', which of the following statements is 
 correct for \lambda = 1?

 Question: 4
 Train the '1 versus 5' classifier with z = (1,x1,x2,x1x2,x21,x2) with 
 \lambda = 0.01 and \lambda = 1. Which of the following statements is correct?

'''

from my_library import *

# Compute sample error.
def sample_error(Z, w_reg, n_var):
		
	Z[n_var + 1] = np.sign(np.dot(Z.loc[: , 0:n_var-1], w_reg))	 
	Z[n_var + 2] = [0 if x[n_var]==x[n_var + 1] else 1 for x in Z.values]
	e_in = float(sum(Z[n_var + 2]))/Z.shape[0]

	return(e_in)

# Regression analysis.
def reg_least_square(Z, y, lamda):

	w_reg_tmp = (np.dot(Z,Z.T) + lamda * np.identity(Z.shape[0]))	
	
	# Regression weights.	
	w_reg = np.dot(np.dot(LA.inv(w_reg_tmp), Z).T, y.values)	
		
	return(w_reg)

def main(argv = None):

	# File location path.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/final/features.train.xlsx'	 
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	# Import in-sample data from Excel.
	data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] \
			for r in range (sheet.nrows)] 				
	data_train = pd.DataFrame(data_train, dtype = 'd')	# Training data.

	# File location path.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/final/features.test.xlsx'	 
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	# Import in-sample data from Excel.
	data_test = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] \
			for r in range (sheet.nrows)] 	
	data_test = pd.DataFrame(data_test, dtype = 'd')	# Test data.


	y = None
	lamda = 1	
	# ================= Question 1 ====================
	for v_int in range(0,10):
		if (y != None):
			# If y is set to a digit. 
			data_train = data_train[data_train[0].isin([v_int, y])]		 

		# Set classifiers as +1 and -1.
		data_train[3] = [1 if itr == v_int else -1 for itr in data_train[0]]	 
	
		# Set classifiers as +1 and -1.
		data_test[3] = [1 if itr == v_int else -1 for itr in data_test[0]]	 
		
		# --- In-sample data ---
		Z = pd.DataFrame(np.ndarray((data_train.shape[0], 3), dtype = 'd'))	 
		Z[0] = np.ones(data_train.shape[0])
		Z.loc[:, 1:2] = data_train.loc[:, 1:2].values
	
		wgt = reg_least_square(Z, data_train[3], lamda)	 # Compute Weights. 
		Z[3] = data_train[3]
		e_in = sample_error(Z, wgt, 3)			 # Compute in-sample error.
		print 'For ' + str(v_int) + ' versus all Ein = ' + str(e_in)

		# --- Out-of-sample data ---
		Y = pd.DataFrame(np.ndarray((data_test.shape[0], 3), dtype = 'd'))	 
		Y[0] = np.ones(data_test.shape[0])
		Y.loc[:, 1:2] = data_test.loc[:, 1:2].values
	
		Y[3] = data_test[3]
		# Compute out-sample error.
		e_out = sample_error(Y, wgt, 3)		
		print 'For ' + str(v_int) + ' versus all Eout = ' + str(e_out)

	# ============== Question 2, 3 and 4 =============
	lamda = 1
	y = None
	for v_int in range(0,10):
		if (y != None):
			# If y is set to a digit. 	
			data_train = data_train[data_train[0].isin([v_int, y])]		 
			# If y is set to a digit. 	
			data_test = data_test[data_test[0].isin([v_int, y])]		 

		# Set classifiers as +1 and -1.
		data_train[3] = [1 if itr == v_int else -1 for itr in data_train[0]]	 
		# Set classifiers as +1 and -1.
		data_test[3] = [1 if itr == v_int else -1 for itr in data_test[0]]	 
	
		# --- In-sample data ---	
		X = pd.DataFrame(np.ndarray((data_train.shape[0], 6), dtype = 'd'))	 
		X[0] = np.ones(data_train.shape[0])
		X.loc[:,1:2] = data_train.loc[:,1:2].values
		X[3] = data_train[1].values * data_train[2].values
		X[4] = data_train[1].values**2
		X[5] = data_train[2].values**2

		wgt = reg_least_square(X, data_train[3], lamda)		# Compute Weights.	
		
		X[6] = data_train[3].values						 		
		e_in = sample_error(X, wgt, 6)		# Compute in-sample error. 
		print 'For ' + str(v_int) + ' versus all Ein = ' + str(e_in)
		
		# --- Out-of-sample data ---
		A = pd.DataFrame(np.ndarray((data_test.shape[0], 6), dtype = 'd'))	 
		A[0] = np.ones(data_test.shape[0])
		A.loc[:,1:2] = data_test.loc[:, 1:2].values
		A[3] = data_test[1].values * data_test[2].values
		A[4] = data_test[1].values**2
		A[5] = data_test[2].values**2
	
		A[6] = data_test[3].values		
		e_out = sample_error(A, wgt, 6)		# Compute out-of-sample error.
		print 'For ' + str(v_int) + ' versus all Eout = ' + str(e_out)

	return(0)

if __name__ == '__main__':
	status = main()
	sys.exit(status)



