
'''

 Name: Classification using SVM with RBF kernel.

 Author: Ranaji Krishna.

 Notes: The code below solves the following problem:
 
 Consider the radial basis function (RBF) kernel 
 K(xn, xm) = exp (-|xn - xm|^2) in the soft-margin SVM approach. 
 Focus on the 1 versus 5 classifier.

 Question 1:
 Which of the following values of C results in the lowest Ein?

 Question 2:
 Which of the following values of C results in the lowest Eout?

'''

from my_library import *

def compute (data_tr, data_te, x, y, C):

	if (y != None):
		data_tr = data_tr[data_tr[0].isin([x,y])]		   # If y is set to a digit. 	
		data_te = data_te[data_te[0].isin([x,y])]		   # If y is set to a digit. 	
	
	data_tr[3] = [1 if itr == x else -1 for itr in data_tr[0]]	   # Set classifiers as +1 and -1.
	data_te[3] = [1 if itr == x else -1 for itr in data_te[0]]	   # Set classifiers as +1 and -1.

	options = '-s 0 -t 2 -g 1 -q -c ' + str(C) 			   # Set Options.
	prob = svm.svm_problem(np.array(data_tr[3]).tolist(), \
			       np.array(data_tr.loc[:,1:2]).tolist())	   # Set problem.
	model = svm.svm_train(prob, options)				   # Call libsvm.

	# ***** Evaluate in-sample error. For out-sample error (Question 2) change data_tr to data_te ***** 
	[labels, accuracy, values] = svm.svm_predict(np.array(data_tr[3]).tolist(), \
						     np.array(data_tr.loc[:,1:2]).tolist(), model, '-q')

	return(accuracy[0])

def main(argv = None):
	
	# File location path.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.train.xlsx'	
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] \
			for r in range (sheet.nrows)] 		# Import in-sample data from Excel.
	data_train = pd.DataFrame(data_train, dtype = 'd')	# Training data.

	# File location path.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.test.xlsx'	
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	data_test = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] \
		       for r in range (sheet.nrows)]	 	# Import in-sample data from Excel.
	data_test = pd.DataFrame(data_test, dtype = float)	# Testing data.

	# --- Question 1 & 2 ---
	x = 1 
	y = 5 
	for itr in range(-6,3, 2):
		C = float(1)/10**(itr)						# Set value of C.
		e_in = 1 - 0.01 * compute(data_train, data_test, x, y, C) 	# Compute in-sample error.
		print 'For C = ' + str(C) + ' Ein = ' + str(e_in)	

	return(0)



if __name__ == '__main__':
	status = main()
	sys.exit(status)
