import json
#Function to load the dataset which is in JSON(JavaScript Object Notation)
def getJSON(filePathAndName):
	with open(filePathAndName,'r') as fp:
		return json.load(fp)

data=getJSON('android_questions.json')#The data is loaded as a string in Python
list2=data.keys()		      #The unique ID's of the question are separated 

