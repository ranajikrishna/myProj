'''
 
 Name: Support vector analysis.

 Author: Ranaji Krishna.

 Note: The code below solve the following problem:

 Consider the following training set generated from a target function 
 f : X -> {-1, +1} where X = R^2 x1 = (1,0), y_1 = -1 x_2 = (0,1), 
 y_2 = -1 x_3 = (0,-1), y_3 = -1, x_4 = (-1,0), y_4 = +1 x_5 = (0,2), 
 y_5 = +1, x_6 = (0,-2), y_6 = +1, x_7 = (-2,0), y_7 = +1
 Transform this training set into another two-dimensional space Z
 z_1 =x_2 -2x_1-1, z_2 =x^2_1-2x_2 + 1

 Question 1:
 Using geometry (not quadratic programming), what values of w (without w0) and b 
 specify the separating plane w^Tz + b = 0 that maximizes the margin 
 in the Z space? The values of w1, w2, b are:
 -1,1,-0.5; 1,-1,-0.5; 1,0,-0.5; 0,1,-0.5 

 Question 2:
 Consider the same training set of the previous problem, but instead of 
 explicitly transforming the input space X, apply the hard-margin SVM algorithm 
 with the kernel
			K(x, x') = (1 + x^Tx')^2
 (which corresponds to a second-order polynomial transformation). 
 Set up the expression for L(\alpha1...\alpha7) and solve for the 
 optimal \alpha1, ..., \alpha7 (numerically, using a quadratic programming package). 
 The number of support vectors you get is in what range?

'''


from my_library import *

# Support Vector analysis.
def sup_vec(data, C):

	options = '-s 0 -t 1 -d 2 -r 1 -g 1 -c ' + str(C)  # Set Options.
	prob = svm.svm_problem(np.array(data[2]).tolist(),\
	                       np.array(data.loc[:, 0:1]).tolist())	# Set problem.
	model = svm.svm_train(prob, options)		# Call libsvm.
	
	return(0)

# Compute the sum the Euclidean distances between the points and the plane.
def distance (data, w):

	ecl_dis = np.dot(data, \
	                 w[0:2]) + w.loc[2, 0]*pd.DataFrame(np.ones(data.shape[0]))	

	return(abs(ecl_dis).sum())

# Classify the points (1:x>0, -1:x<0).
def classify(data, w):

	cls_pts = np.dot(data, w[0:2]) + \
			 w.loc[2, 0]*pd.DataFrame(np.ones(data.shape[0]))
	cls_pts[1] = np.sign(cls_pts[0].values) 

	return(cls_pts)

# Transform from x-axis to z-axis.
def transform(data):

	col = data.shape[1]
	data = pd.DataFrame(data)
	data[col] = [data.loc[x, 1]**2 - 2*data.loc[x, 0] - 1 for x in data.index]
	data[col + 1] = [data.loc[x, 0]**2 - 2*data.loc[x, 1] + 1 for x in data.index]

	return(data)


def main (argv = None):

	# File location.
	file_location = '/Users/vashishtha/myGitCode/ML/homeWorks/final/que11_data.xlsx'
	workbook = xlrd.open_workbook(file_location)
	sheet = workbook.sheet_by_index(0)

	# Import in-sample data from Excel.
	data_train = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] \
		       for r in range (sheet.nrows)] 
	
	data_train =  pd.DataFrame(data_train)
	data_train = transform(data_train)	# Transform into two-dim. space Z.

	# --- Question 1 ---
	w = pd.DataFrame(np.array([0, 1, -0.5], dtype = float))		# Weights.
	class_pts = classify(data_train.loc[:, 3:4], w)			# Classifcation.
	data_train[5] = class_pts[0]		# Populate matrix.
	data_train[6] = class_pts[1]		# Populate matrix.
	dist = distance(data_train.loc[:, 3:4], w)	# Sum of Euclidean distances.

	# Verification (0:match, 1:mis-match). 
	data_train[7] = [0 if data_train.loc[x, 2] == data_train.loc[x, 6] else 1 \
		  	 for x in data_train.index]

	# --- Question 2 --- 
	C = 1e6		  	            # Setting a hard boundary.
	sup_vec(data_train.loc[:, 0:2], C)  # Support vector machine evaluation. 
	
	print(sum(data_train[7]))
	print dist

	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)
