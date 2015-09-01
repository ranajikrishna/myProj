'''
Name: ML with Scikit-learn.
Author: Ranaji Krishna.

*** Notes ***:

'''

from myLib import *
from sklearn.datasets      import load_iris
from sklearn.svm           import LinearSVC
from sklearn.datasets      import load_digits
from sklearn.datasets      import make_s_curve
from sklearn.datasets 	   import fetch_olivetti_faces
from sklearn		   import neighbors
from sklearn.linear_model  import LinearRegression
from sklearn.decomposition import PCA
from sklearn.cluster       import KMeans
from sklearn.neighbors 	   import KNeighborsClassifier
from sklearn.metrics 	   import confusion_matrix
from sklearn.svm 	   import SVC 		         	# "Support Vector Classifier"
from sklearn.tree 	   import DecisionTreeClassifier
from sklearn.ensemble      import RandomForestClassifier
from sklearn 		   import metrics

from sklearn.cross_validation 		import train_test_split
from sklearn.datasets.samples_generator import make_blobs

import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

def plot_estimator(estimator, X, y):
    	estimator.fit(X, y)
    	x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    	y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    	xx, yy = np.meshgrid(np.linspace(x_min, x_max, 50), np.linspace(y_min, y_max, 50))
    	Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    	# Put the result into a color plot
    	Z = Z.reshape(xx.shape)
    	plt.figure()
    	plt.pcolormesh(xx, yy, Z, alpha=0.3)

    	# Plot also the training points
    	plt.scatter(X[:, 0], X[:, 1], c=y, s=50)
    	plt.axis('tight')
    	plt.axis('off')
    	plt.tight_layout()
	
	return(0)

def decisionTreesAndRandomForests():
	X, y = make_blobs(n_samples=300, centers=4,random_state=0, cluster_std=0.60)
	#plt.scatter(X[:, 0], X[:, 1], c=y, s=50)
	
	clf = DecisionTreeClassifier(max_depth=10)
	#plot_estimator(clf, X, y)
			
	clf = RandomForestClassifier(n_estimators=10, random_state=0)
	#plot_estimator(clf, X, y)

	# ---- Digit Classifier ----
        digits = load_digits()
	X = digits.data
	y = digits.target

	Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
	clf = DecisionTreeClassifier(max_depth=5)
	clf.fit(Xtrain, ytrain)
	ypred = clf.predict(Xtest)

	plt.imshow(metrics.confusion_matrix(ypred, ytest), interpolation='nearest', cmap=plt.cm.binary)
	plt.colorbar()
	plt.xlabel("true label")
	plt.ylabel("predicted label")

	return(0)

def plot_svc_decision_function(clf):
   	 """Plot the decision function for a 2D SVC"""
    	x = np.linspace(plt.xlim()[0], plt.xlim()[1], 30)
    	y = np.linspace(plt.ylim()[0], plt.ylim()[1], 30)
    	Y, X = np.meshgrid(y, x)
    	P = np.zeros_like(X)
    	for i, xi in enumerate(x):
        	for j, yj in enumerate(y):
            		P[i, j] = clf.decision_function([xi, yj])


	return plt.contour(X, Y, P, colors='k', levels=[-0.8, 0, 0.8], linestyles=['--', '-', '--'])

def supportVecMachine():

	X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
	plt.scatter(X[:, 0], X[:, 1], c=y, s=50)

	#clf = SVC(kernel='linear')
	#clf.fit(X, y)
	
	#plot_svc_decision_function(clf)
	#plt.show()

	clf = SVC(kernel='rbf')
	clf.fit(X, y)
	
	plot_svc_decision_function(clf)
	plt.show()

	return(0)


def KMeansCluster(X_reduced):

	k_means = KMeans(n_clusters=4, random_state=0)
	k_means.fit(X_reduced)
	y_pred = k_means.predict(X_reduced)

	plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_pred)
	plt.show()

	return(0)

def pcaAnalysis(iris):

	X , y = iris.data, iris.target
	pca = PCA(n_components=2)
	pca.fit(X)
	X_reduced = pca.transform(X)
	print "Reduced dataset shape:", X_reduced.shape

	plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
	return(X_reduced)

def linearRegression (X,y):

	model = LinearRegression(fit_intercept=True)
	model.fit(X, y)
	print "Model coefficient: %.5f, and intercept: %.5f" % (model.coef_, model.intercept_)

	# Plot the data and the model prediction
	X_test = np.linspace(0, 1, 100)[:, np.newaxis]
	y_test = model.predict(X_test)
	plt.plot(X.squeeze(), y, 'o')
	plt.plot(X_test.squeeze(), y_test)
	
	return(0)

def neighborsClassification (iris):
	
	X, y = iris.data, iris.target
	knn = neighbors.KNeighborsClassifier(n_neighbors=1)
	knn.fit(X,y)

	#unknown = knn.predict([[1,4,3,2]])	
	#print(unknown[0]) 			# Unknown data point.
	print iris.target_names[knn.predict([[3, 5, 4, 2]])]
	
	y_pred = knn.predict(X)			# In-sample testing.
	print(np.all(y == y_pred))
	print(confusion_matrix(y, y_pred))	# Confusion matrix.

	Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
	knn.fit(Xtrain, ytrain)
	ypred = knn.predict(Xtest)
	print(confusion_matrix(ytest, ypred))	

	return(0)

def plot_digits_projection(digits):

	# set up the figure
	fig = plt.figure(figsize=(6, 6))  # figure size in inches
	fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

	# plot the digits: each image is 8x8 pixels
	for i in range(64):
    		ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
	    	ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest') # label the image with the target value
    		ax.text(0, 7, str(digits.target[i]))

	plt.show()
	
	return(0)

def plot_iris_projection(x_index, y_index, iris):
    	
	# this formatter will label the colorbar with the correct target names
    	formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

   	plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
   	plt.colorbar(ticks=[0, 1, 2], format=formatter)
    	plt.xlabel(iris.feature_names[x_index])
    	plt.ylabel(iris.feature_names[y_index])

	plt.show()

	return(0)

def plot_faces_projection(faces):

	# set up the figure
	fig = plt.figure(figsize=(10, 5))  # figure size in inches
	fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.01)

	# plot the digits: each image is 8x8 pixels
	for i in range(400):
    		ax = fig.add_subplot(20, 20, i + 1, xticks=[], yticks=[])
	    	ax.imshow(faces.images[i], cmap=plt.cm.bone, interpolation='nearest') # label the image with the target value
    		ax.text(0, 63, str(faces.target[i]))

	plt.show()
	
	return(0)

	
def main (argv = None):

	# ---- Iris ----	
	iris = load_iris()
	n_samples, n_features = iris.data.shape
	target_names=iris.target_names

	X, y = iris.data, iris.target
	#plt.figure()	
	#plot_iris_projection(0, 0, load_iris())
	#plt.figure()	
	#plot_iris_projection(0, 1, load_iris())
	#linearCla(X,y)
	
	# ---- Digits ----
	#digits = load_digits()
	#plot_digits_projection(load_digits())

	# ---- S-curve ----
	#data, colors = make_s_curve(n_samples=10000)	
	#ax = plt.axes(projection='3d')
	#ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=colors)
	#ax.view_init(10, -60)	
	#plt.show()

	# ---- Oviletti faces ----
	#faces = fetch_olivetti_faces()
	#plot_faces_projection(fetch_olivetti_faces())

	# ---- K-Neighbours Classification ----
	#neighborsClassification (load_iris())

	# ---- Linear Regression ----
	# Create some simple data
	np.random.seed(0)
	X = np.random.random(size=(20, 1))
	y = 3 * X.squeeze() + 2 + np.random.normal(size=20)	

	#linearRegression(X,y)

	# ---- PCA Analysis ----
	#reduced_data = pcaAnalysis(load_iris())

	# ---- K-Mean Clusters ----
	#KMeansCluster(reduced_data)
	#iris = load_iris()
	#KMeansCluster(iris.data)

	# ---- Support Vector Machines ----
	#supportVecMachine()	

	# ---- Decision Trees and Random Forests ----
	decisionTreesAndRandomForests()

	return(0)

	# ---- 


if __name__ == '__main__':
        status = main()
        sys.exit(status)


