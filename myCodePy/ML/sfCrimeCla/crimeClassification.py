'''
Name:   Classification of Crimes in San Francisco.

Author: Ranaji Krishna.

*** Notes ***:
Predict the category of crimes that occurred in the city by the bay
From 1934 to 1963, San Francisco was infamous for housing some of the world's most notorious criminals on the inescapable island of Alcatraz. Today, the city is known more for its tech scene than its criminal past. But, with rising wealth inequality, housing shortages, and a proliferation of expensive digital toys riding BART to work, there is no scarcity of crime in the city by the bay. From Sunset to SOMA, and Marina to Excelsior, this competition's dataset provides nearly 12 years of crime reports from across all of San Francisco's neighborhoods.
Given time and location, you must predict the category of crime that occurred.
We're also encouraging you to explore the dataset visually. What can we learn about the city through visualizations like this Top Crimes Map? The top most up-voted scripts from this competition will receive official Kaggle swag as prizes. 

'''

from myLib import *


def classify(data):

	data_sub = data[data['Bin']==1]
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(data_sub['X'],data_sub['Y'],data_sub['Time'])

	#plt.show()
	
	with open('objs.pickle') as trnTstData: trndata, tstdata = pickle.load(trnTstData)
	
	trndata = ClassificationDataSet(3,1, nb_classes = 39)
	[trndata.addSample(data.iloc[k, 0:3], data['Bin'][k]) for k in xrange(1, int( ceil(0.75 * len(data))))]
	
	tstdata = ClassificationDataSet(3,1, nb_classes = 39)
	[tstdata.addSample(data.iloc[k, 0:3], data['Bin'][k]) for k in xrange(int( ceil(0.75 * len(data))) + 1, len(data))]
	
	trndata._convertToOneOfMany()
	tstdata._convertToOneOfMany()

	n = buildNetwork(trndata.indim, 28, trndata.outdim, outclass=SoftmaxLayer, bias=True)	
	trainer = BackpropTrainer(n, dataset = trndata, momentum=0.1, learningrate=0.01 , verbose=True, weightdecay=0.01) 

	trainer.trainEpochs(100)

	print (percentError(trainer.testOnClassData (dataset=tstdata), tstdata['class']))
	return(0);


def main (argv = None):

	store = pd.HDFStore('store_data.h5')
	
	train = pd.concat([store['data_train'][0], store['data_train'][7], store['data_train'][8], store['data_train'][1], pd.DataFrame([0] * (np.size(store['data_train'][0])-1))], axis=1)
	train = train.drop(train.index[[0]])
	train.columns = ['Time','X','Y','Category','Bin']
	
	[u, ind] = np.unique(train['Category'], return_index=True)
	k = 0;
	for i in u:
		train.loc[train['Category'] == i,'Bin'] = k
		k += 1

	weight = classify(train[0:10000])
	return(0)	

#train = store['data_train'];
	store.close()
	return(0)


if __name__ == '__main__':
	status = main()
	sys.exit(status)


# ----- Convert data to storable HDFS objects -----	
#file_location = '/Users/vashishtha/myGitCode/myProj/myCodePy/ML/sfCrimeCla/train.xlsx';	 # File location path.
#workbook = xlrd.open_workbook(file_location);
#sheet = workbook.sheet_by_index(0);

#data_train = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)];  # Import in-sample data from Excel.
#data_train = pd.DataFrame(data_train, dtype = 'd');						  # Training data.
#store['data_train'] = data_train;	
	
#file_location = '/Users/vashishtha/myGitCode/myProj/myCodePy/ML/sfCrimeCla/test.xlsx';	 # File location path.
#workbook = xlrd.open_workbook(file_location);
#sheet = workbook.sheet_by_index(0);

#data_test = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range (sheet.nrows)];  # Import in-sample data from Excel.
#data_test = pd.DataFrame(data_test, dtype = 'd');						 # Testing data.
#store['data_test'] = data_test;	
# -----------

# ----- Example of Olivetti Faces --- 
#	from sklearn import datasets
#	olivetti = datasets.fetch_olivetti_faces()
#	X, y = olivetti.data, olivetti.target	
#
#	trndata = ClassificationDataSet(4096, 1 , nb_classes=40)
#	for k in xrange(int(ceil(0.75*len(X)))): trndata.addSample(np.ravel(X[k]),y[k])
#
#	tstdata = ClassificationDataSet(4096, 1 , nb_classes=40)
#	for k in xrange(int(ceil(0.25*len(X)))): tstdata.addSample(np.ravel(X[k]),y[k])
#	
#	trndata._convertToOneOfMany()
#	tstdata._convertToOneOfMany()
#
#	print trndata['input'], trndata['target'], tstdata.indim, tstdata.outdim
#
#	fnn = buildNetwork( trndata.indim, 64 , trndata.outdim, outclass=SoftmaxLayer )
#	trainer = BackpropTrainer( fnn, dataset=trndata, momentum=0.1, learningrate=0.01 , verbose=True, weightdecay=0.01) 
#
#	trainer.testOnClassData (dataset=tstdata)
# ----------
