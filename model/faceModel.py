
import csv # for reading the csv file
import pandas as pd # uses dataframes from pandas
import numpy as np # used for arrays
from sklearn.ensemble import RandomForestClassifier # used for creating FSS score predictors --> Random Forest algorithm
from sklearn.svm import SVC
from sklearn.model_selection import KFold # for implementing k-folds
import matplotlib.pyplot as plt # used for plotting the graphs
from sklearn import tree


# FUNCTIONS:

def create_conf_matrix(y_preds, y_reals):
	TP = 0
	FN = 0
	FP = 0
	TN = 0
	falsePos = []
	falseNeg = []

	for i in range(len(y_preds)):
		pred_val = y_preds[i]
		test_val = y_reals[i]

		if test_val == 1 and pred_val == 1:
			TP += 1
		if test_val == 1 and pred_val == 0:
			FN += 1
			falseNeg.append(files[i])
		if test_val == 0 and pred_val == 1:
			FP += 1
			falsePos.append(files[i])
		if test_val == 0 and pred_val == 0:
			TN += 1

	falsePos.sort()
	falseNeg.sort()
	return [TP, FN, FP, TN]

# calculates accuracy of model results
def accuracy(matrix):
	TP = matrix[0]
	TN = matrix[3]
	acc = (TP + TN) / (matrix[0] + matrix[1] + matrix[2] + matrix[3])
	return acc

# calculates the sensitivity of model results
def sensitivity(matrix):
	TP = matrix[0]
	FN = matrix[1]
	sens = TP / (TP + FN)
	return sens

# calculates the specificity of model results
def specificity(matrix):
	TN = matrix[3]
	FP = matrix[2]
	spec = TN / (TN + FP)
	return spec



dataset = np.array(pd.read_csv(r'C:\Users\jeffe\Downloads\face_det_hardware\HumanDetection-Kinect-Mmwave\model\ThermalOcc.csv')) # dataset of confidence levels
target_data = dataset[:, 5] # UPDATE!
num_entries = len(dataset)

labels = ["ID", "CONF"] # UPDATE COLUMN TITLES
classes = ["0", "1"]

kfold = KFold(n_splits = 10, shuffle = True, random_state = 100) # creates 10-fold splits
face_preds = []
face_truths = []

for train_index, test_index in kfold.split(dataset):

	x_train, x_test = dataset[train_index], dataset[test_index]
	y_train, y_test = target_data[train_index], target_data[test_index]

	classifier = RandomForestClassifier(max_depth = 6, min_samples_leaf = 3, min_samples_split = 10, class_weight = 'balanced', bootstrap = False, max_features = "auto", random_state = 100) # generates random forest model
	classifier.fit(x_train, y_train) # trains the model using the training sets
	y_pred = classifier.predict(x_test) # predicts the data for the test dataset
	
	for i in range(len(y_pred)):
		face_preds.append(y_pred[i])
		face_truths.append(y_test[i])


matrix = create_conf_matrix(face_preds, face_truths, filePreds)
print("[TP, FN, FP, TN] = ", end = "")
print(matrix)
print("\nAccuracy: " + str(accuracy(matrix)))
print("Sensitivity: " + str(sensitivity(matrix)))
print("Specificity: " + str(specificity(matrix)) + "\n")

# fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (35, 10), dpi = 400)
# tree.plot_tree(classifier.estimators_[0], feature_names = labels, class_names = classes, filled = True, impurity = False, precision = 1, fontsize = 10)
# fig.savefig('decisionTree.png')
