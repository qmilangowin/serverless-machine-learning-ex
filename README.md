# Serverless Machine Learning

1. Create a virtual-env `virtualenv environment_name` and `source environment_name/bin/activate. 
2. `pip install sklearn, numpy, flask, boto3, scipy, zappa`. 
3. `zappa init`. 
4. Take a look at `zappa_settings.json`. You app should reside in a directory called `api`  
5. Edit `zappa_settings.json` to have function name as: `api.appname.app` (not `appname.py`). 
6. Ensure that the following key/value is in the `zappa_settings.json`. Edit if needed:  
    <code>“slim_handler”: true</code>. <-- this is needed to upload large dependencies/files
7. Finally `zappa deploy dev`


***Misc***
What does this do?
Simple classification model to check serverless deployment. Takes the age and salary and will predict if the person will buy a car or not.

I have two pickled files, one for the the StandardScaler and one for the Model.

`POST` requests should be of the following:
<code>
  {
	"feature_array":[9,2450]
  }
  </code>
  
  where the first value is the age and the 2nd is the salary
  
  
