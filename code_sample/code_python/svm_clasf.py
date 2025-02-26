
'''

 Name: Classification using support vector machines.

 Author: Ranaji Krishna.

 Notes: The code below solves the following problem: 
 
 In this problem, we will experiment with 10-fold cross validation for the 
 polynomial kernel. Because Ecv is a random variable that depends on the random 
 partition of the data, we will try 100 runs with different partitions and base 
 our answer on how many runs lead to a particular choice.:

 Question 1:
 Consider the 1 versus 5 classifier with Q = 2. We use Ecv to select 
 C = {0.0001, 0.001, 0.01, 0.1, 1}. If there is a tie in Ecv , select the smaller C . 
 Within the 100 random runs, which value of C yields the smallest Ecv most frequently?

 Question 2:
 Again, consider the 1 versus 5 classifier with Q = 2. For the winning selection
 in the previous problem, what is the average value of Ecv?

'''

from my_library import *

def compute (train, test, x, y, C, d):

	# Set Options.
	options = '-s 0 -t 1 -d ' + str(d) + ' -r 1 -g 1 -q -c ' + str(C) 	
	prob = svm.svm_problem(np.array(train[3]).tolist(), \
			       np.array(train.loc[:,1:2]).tolist())	# Set problem.
	model = svm.svm_train(prob, options)				# Call libsvm.

	# Evaluate in-sample error. 
	[labels, accuracy, values] = svm.svm_predict(np.array(test[3]).tolist(), \
				     np.array(test.loc[:,1:2]).tolist(), model, '-q')

	return(accuracy[0])

def main(argv = None):

	# File location path.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/homeWork8/features.train.xlsx'	
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	# Import in-sample data from Excel.
	data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] \
			for r in range (sheet.nrows)]  
	data_train = pd.DataFrame(data_train, dtype = 'd') 	# Training data.

	# =================== Question 1 and 2 ================= 
	x = 1 
	y = 5 
	d = 2		# Degrees.
	iteration = 100 # No. iterations.
	
	data_tr = data_train[data_train[0].isin([x,y])]		# If y is set to a digit. 	
	
	# Set classifiers as +1 and -1.
	data_tr[3] = [1 if itr == x else -1 for itr in data_tr[0]]	 

	# Store Cross-validation error.	
	e_cv = pd.DataFrame(np.ndarray((iteration, 5), dtype = float))   
	for itr in range(0, iteration):
		# Random sample of rows to be picked.
		rows = random.sample(range(0, data_tr.shape[0]), data_tr.shape[0]/10)	
		
		# Traning sample.
		data_xtr = data_tr.drop(data_tr.index[rows])				
		# Cross-validation sample.
		data_xte = data_tr.iloc[rows]						

		itr_col = 0		# Iterator for upper bound.
		
		# Compute in-sample error for different upper bounds. 
		for itr_C in range(4,-1,-1):
			# Upper bound.
			C = float(1)/10**(itr_C)					
			# Compute in-sample error.
			e_cv.loc[itr,itr_col] = 1 - \
				0.01*compute(data_xtr, data_xte, x, y, C, d) 
			itr_col +=1 

	# Index of the minimum in-sample error.	
	min_index = [(e_cv.loc[rows,:]).argmin() for rows in e_cv.index]		

	# Freq. of indices.
 	freq_idx = np.bincount(min_index)						
	
	# Average in-sample error for C = 0.001.
	mean_Ecv = np.mean(e_cv)[1]							

	print 'Frequency of selection of C = {0.0001, 0.001, 0.01, 0.1, 1}' 
	print(freq_idx)
	print 'For C = 0.001, mean in-sample error = %f' %mean_Ecv
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
