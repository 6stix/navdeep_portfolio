from keras.models import Sequential, load_model
from keras.layers import Input, Dense
from keras.optimizers import SGD
import tensorflow as tf

import flask
from flask_cors import CORS
from flask import request

import requests, bs4
import numpy as np

import restModel

app = flask.Flask(__name__)
CORS(app)
my_net = None

def load_model():
	"""
	Load the model.
	"""
	global my_net
	my_net = restModel.NET(file_to_read="out.csv", mode="nn", second_mode="pre_trained", load_model_name="nn-02-09-2019-1.55am")

	global graph
	graph = tf.get_default_graph()

@app.route("/predict", methods=["GET", "OPTIONS"])
def predict():
	"""
	Makes a prediction on what emotion a phrase embodies.
	"""
	data = {"success": False}

	if flask.request.method == "GET":
		phrase = flask.request.args['phrase']
		string = ""
		phrase = collect_paragraph_elements(phrase)

		phrase = my_net.tfidf_vector.transform([phrase])
		prediction = ""
		with graph.as_default():
			prediction = my_net.nn.predict(phrase)

		reverse_mappings = {0:"worry",1:"neutral",2:"happiness",3:"sadness",4:"love",5:"surprise",6:"fun",7:"relief",8:"hate",9:"anger",10:"empty",11:"enthusiasm",12:"boredom"}
		prediction = prediction[0]
		highest_prediction = float('-inf')
		index_of_highest = 0
		for index,pred in enumerate(prediction):
			if pred > highest_prediction:
				index_of_highest = index
				highest_prediction = pred

		data["emotion"] = reverse_mappings[index_of_highest]
		data["superData"] = string
		data["success"] = True

	return flask.jsonify(data)

def collect_paragraph_elements(input_url):
	"""
	This function checks if the passed-in string is a valid url. If it is, then
	this function tries to get text with paragraph tags from the url. If there is
	an error, the original passed-in string is returned.
	"""
	input_url_copy = input_url[:]
	output = None

	# For basic functionality, limit to these three extensions
	valid_extensions = ['.com', '.org', '.net']
	url_is_valid = False
	for extension in valid_extensions:
		if extension in input_url:
			url_is_valid = True

	if url_is_valid == False:
		return input_url_copy

	try:
		response_GET = requests.get(input_url)
		response_GET.raise_for_status()

		paragraph_elements = bs4.BeautifulSoup(response_GET.text, features="html5lib")
		paragraph_elements = paragraph_elements.select('p')

		for element in paragraph_elements:
			string += element.getText()

		output = string

	except Exception as exc:
		print("Error with collecting paragraph elements:", exc)
		output = input_url_copy

	return output

if __name__ == "__main__":
	print("Loading deep-learning model for the API!")
	load_model()
	app.run()
