#This file is for processing the dataset that includes tokenising the paragraphs, 
#removing html tags and removing stop words.
import json
from nltk.tokenize import RegexpTokenizer
import re
import nltk

#The function to open the json file and return the file as a json object
def getJSON(filePathAndName):
	with open(filePathAndName,'r') as fp:
		return json.load(fp)

def preprocess(sentence):
	stopwords = set(nltk.corpus.stopwords.words('english'))
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	words = [word for word in tokens if len(word) > 1]
	words = [word for word in tokens if not word.isnumeric()]
	filtered_words = [w for w in words if not w in stopwords]
	return (filtered_words)

#Fucntion to remove the html tags from the document 
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
