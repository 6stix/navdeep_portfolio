from keras.models import Sequential, load_model
from keras.layers import Input, Dense
from keras.optimizers import SGD

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

class NET:
	"""
	This class initializes a neural net.
	"""
	def __init__(self, file_to_read, mode, second_mode, model_name=None, load_model_name=None):
		pre_data, labels = read_file(file_to_read, mode)

		data, vect_transformed = tfidf_data(pre_data)
		self.tfidf_vector = vect_transformed

		if second_mode == "pre_trained":
			self.pre_trained_neural_net(load_model_name=load_model_name)

		else:
			x_train, x_test, y_train, y_test = train_test_split(data, labels, train_size=0.75)
			self.neural_net(x_train, x_test, y_train, y_test, model_name=model_name)

	def neural_net(self, x_train, x_test, y_train, y_test, model_name):
		"""
		This function would be used to train a new model. I trained the saved one
		before, so we do not have to train now.

        This neural net is composed of three layers: an input layer, a hidden layer,
        and an output layer. We are using Stochastic Gradient Descent to find the
        best weights we can without overfitting to our training data.
		"""
		self.nn = Sequential()

		number_of_features = x_train.shape[1]
		number_of_emotions = 13

		self.nn.add(Dense(units=250, activation='relu', input_shape=(number_of_features,)))
		self.nn.add(Dense(units=100, activation='relu'))
		self.nn.add(Dense(units=number_of_emotions, activation='softmax'))
		self.nn.summary()

		sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
		self.nn.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

		self.nn.fit(x_train, np.array(y_train), epochs=30, batch_size=32)
		self.nn.save(model_name + '.h5')

		self.test(x_test, y_test)

	def pre_trained_neural_net(self, load_model_name):
		"""
		Load the model (I pre-trained it!)
		"""
		self.nn = load_model(load_model_name + '.h5')

	def test(self, x_test, y_test):
		"""
		Test neural net.
		"""
		predictions = self.nn.predict(x_test)

		correct = 0
		total = 0

		for i in range(len(predictions)):
			curr_pred = predictions[i]
			curr_truth = y_test[i]

			for j in range(len(curr_pred)):
				temp_pred = 0
				if curr_pred[j] > 0.5:
					temp_pred = 1

				if temp_pred == curr_truth[j]:
					correct += 1

				total += 1

		print("Accuracy:", correct/total)

def tfidf_data(data):
	"""
	Convert data into tfidf vector representation, where less common words receive
	greater weight than more common/popular words.
	"""
	tfidf_v = TfidfVectorizer()
	x_data = tfidf_v.fit_transform(data)

	return x_data, tfidf_v

def knn(x_train, x_test, y_train, y_test):
	"""
	I experimented with K-Nearest Neighbors for this problem.
	"""
	knn = KNeighborsClassifier(n_neighbors=100)
	knn.fit(x_train, y_train)

	print(kN.score(x_test, y_test))

def logistic_regression(x_train, x_test, y_train, y_test):
	"""
	I also experimented with Logistic Regression for the problem.
	"""
	log_reg_model = LogisticRegression()
	log_reg_model = log_reg_model.fit(x_train, y_train)

	predicted_labels = log_reg_model.predict(x_test)
	print(log_reg_model.score(x_test, y_test))

def read_file(f_input, mode):
	"""
	Reads in a file line-by-line and stores each phrase with its corresponding
	emotion tag for training and testing the model(s).
	"""
	x = []
	y = []

	mappings = {"worry":0, "neutral":1, "happiness":2, "sadness":3, "love":4, "surprise":5, "fun":6, "relief":7, "hate":8, "anger":9, "empty":10, "enthusiasm":11, "boredom":12}

	with open(f_input, 'r') as f:
		data = f.read().split('\n')[1:30000]

	for line in data:
		line = line.rpartition(',')

		if mode == "nn":
			x.append(line[0])
			y_emotions_one_hot = np.zeros(13)
			y_emotions_one_hot[mappings[line[2]]] = 1
			y.append(y_emotions_one_hot)

		else:
			x.append(line[0])
			y.append(line[2])

	return x, y
