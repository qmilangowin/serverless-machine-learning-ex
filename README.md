# Serverless Machine Learning

1. Create a virtual-env `virtualenv environment_name -p python3.6` (zappa doesn't support python3.7 yet) then `source environment_name/bin/activate`. 
2. `pip install sklearn, numpy, flask, boto3, scipy, zappa`. 
3. `zappa init`. 
4. Take a look at `zappa_settings.json`. You app should reside in a directory called `api`  
5. Edit `zappa_settings.json` to have function name as: `api.appname.app` (not `appname.py`). 
6. Ensure that the following key/value is in the `zappa_settings.json`. Edit if needed:  
    <code>“slim_handler”: true</code>. <-- this is needed to upload large dependencies/files
7. Finally `zappa deploy dev`
8. Upload `scaling.pkl` and `classifier.pkl` files to your S3 bucket and edit code accordingly.

***Misc***  
What does this do?  

Simple classification model to check serverless deployment. Takes the age and salary and will predict if the person will buy a car or not. To be clear, this repo is not about doing ML but rather how to get your ML into a serverless environment and run predictions via a REST query.

I have two pickled files, one for the the StandardScaler and one for the Model.

`POST` requests needs to be in `JSON` format and should look like this the following:  

<code>
  {  
	"feature_array":[18,2450]  
  }  
  </code>
  
  where the first value is the age and the 2nd is the salary.

  There is no error correction or handling of bad requests. This is for demo purposes only of how to deploy a Machine Learning model and use AWS Lambda for it.
  
You can try sending a `POST` request to the following endpoint that I have setup. See above for the JSON content to send in the `POST` request. This endpoint is a simple ML model running in AWS Lambda and will predict whether a person will purchase a car based on their salary and age. Use Insomnia/Postman or CURL:

https://3d8yngsqvh.execute-api.us-east-1.amazonaws.com/dev
