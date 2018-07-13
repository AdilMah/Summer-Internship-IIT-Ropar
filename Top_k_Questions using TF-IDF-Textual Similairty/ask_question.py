import nltk.corpus
from qdet import list2
import json
from nltk.tokenize import RegexpTokenizer
import re
import math
from collections import OrderedDict
from preprocess import*

#Load all the preprocessed files containing word frequency count, document count,etc
idf=getJSON('wordDocumentCount.json')
allWords=getJSON('allWords.json')
wordList=getJSON('wordFrequencyCount.json')
data=getJSON("android_questions.json")


tfidfA={}			#dictionary to store the tf-idf values of the question words
newQuestionCount={}	#frequency of words in the new Question
scores={}			#cosine similarity between common words
magnitude={}		#stores the sum of products of tfidf of the input question words
magnitudeB={}		#stores the sum of the products of the tfidf of commonwords
finalScores={}		#stores the cosine similarity between question titles
countuid={}			#stores the number of common words between the input question and individual questions
uid1=[]				#stores the question id of all the questions which have common words both in title and description
totalQuestions=len(list2)

def calculateTFIDFA():  #Function that calculates the tf-idf value of the new question words
	for word in newQuestionWords:
		if word in allWords: #Checking whether that word is present in the existing wordlist as we have to take only the common words
			tfidfA[word]=(1+math.log(newQuestionCount[word]))*math.log(totalQuestions/(len(idf[word])+1))#(1+log(wordfrequency in the title)*log(totalQuestions/no. of questions containg the word)

def calculateTFIDFB(uid,word):#Function that calculates the tf-idf value of the common words in all question titles
	if word in wordList[uid]:
		return (1+math.log(wordList[uid][word])*math.log(totalQuestions/(len(idf[word])+1)))
	else:
		return math.log(totalQuestions/(len(idf[word])+1))


print("Please enter the Question")
newQuestion="How can I find a good bash terminal emulation for Android Gingerbread?"
print(newQuestion)
newQuestionWords=preprocess(newQuestion)

fdist = nltk.FreqDist(newQuestionWords)#To calculate the frequency of all the words in the new questions
for word, frequency in fdist.most_common(100):
	newQuestionCount[word]=frequency
calculateTFIDFA()

#Initialising all the dictionaries
for word in newQuestionWords:
	if word in allWords:
		for uid in idf[word]:
			countuid[uid]=0
			scores[uid]=0
			magnitude[uid]=0
			magnitudeB[uid]=0


for word in newQuestionWords:
	if word in allWords:
		for uid in idf[word]:
			x=calculateTFIDFB(uid,word) #Calculates the TF-IDF of the all the exisiting question words
			#print(word,x)
			countuid[uid]+=1
			scores[uid]+=tfidfA[word]*x #Scores that is required to calculate the similarity between the new question and existing question 
			magnitude[uid]+=x*x
			magnitudeB[uid]+=(tfidfA[word])*(tfidfA[word])
			uid1.append(uid) #Keeps track of all the uids that have atleast a single word matching with the new question words

for word in newQuestionWords:
	if word in allWords:
		for uid in idf[word]:
			if countuid[uid]>1: #Calculates the final similarity between all the exisitng question and new question pairs. 
				finalScores[uid]=scores[uid]/(magnitude[uid]**0.5 * magnitudeB[uid]**0.5)
			else:
				finalScores[uid]=0
#Sortign the dicitonary of quesiton simlarity vales in descending order.
dd = OrderedDict(sorted(finalScores.items(), key=lambda x: x[1]))
