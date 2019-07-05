import pickle
import flask
from flask import request, json
import boto3
import numpy as np

BUCKET_NAME = 'milan-gowin-machine-learning' #YOUR-BUCKET-NAME
SCALER_FILE_NAME = 'scaling.pkl'
MODEL_FILE_NAME = 'classifier.pkl'


S3 = boto3.client('s3')

app = flask.Flask(__name__)


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper
    

@app.route('/',methods=['POST'])
def index():
	try:
		feature_array = request.get_json(silent=True)['feature_array']

		scaler = load_model(SCALER_FILE_NAME)
		model = load_model(MODEL_FILE_NAME)

		scaled = scaler(np.array([feature_array]))
		prediction = model.predict(scaled)

		print(feature_array)
		# if feature_array == []:
		# 	return "Incomplete Request: Please enter a body for your POST request."
		if feature_array[0] > 100 or feature_array[0]<16:
			return "Be serious"
		if prediction == 0:
			return "No the person will not buy the car"
		if prediction == 1:
			return "Yes the person will buy the car"
	except ValueError:
		print("POST Request Error")

@app.route('/', methods=['GET'])
def hello():

	return "Only Post Requests allowed. Please try again"

@memoize
def load_model(key):
	response=S3.get_object(Bucket=BUCKET_NAME, Key = key)
	model_str = response['Body'].read()

	model = pickle.loads(model_str)

	return model



if __name__ == '__main__':
   app.run()