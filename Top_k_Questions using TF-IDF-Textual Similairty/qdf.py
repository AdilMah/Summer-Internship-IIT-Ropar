from qdet import list2
from ask_question import finalScores,uid1
from collections import OrderedDict
import json
import collections
import re
from nltk.tokenize import RegexpTokenizer
import math
import nltk
import operator
from preprocess import*


tfidfADesc={}
scoresDesc={}
magnitudeDesc={}
magnitudeBDesc={}
finalScoresDesc={}
x=0
total=len(list2)
newQuestionCountDesc={}
similarity={}
uid2=[]

idfDesc=getJSON('wordDocumentCountDesc.json')
allWordsDesc=getJSON('allWordsDesc.json')
wordListDesc=getJSON('wordFrequencyCountDesc.json')
data=getJSON("android_questions.json")

def calculateTFIDFA():
	for word in newQuestionWordsDesc:
		if word in allWordsDesc:
			tfidfADesc[word]=(1+math.log(newQuestionCountDesc[word]))*math.log(total/(len(idfDesc[word])+1))


def calculateTFIDFB(uid,word):
	if word in wordListDesc[uid]:
		return (1+math.log(wordListDesc[uid][word])*math.log(total/(len(idfDesc[word])+1)))
	else:
		return math.log(total/(len(idfDesc[word])+1))
	
newQuestionDesc="I want to install a bash terminal emulation on my factory Android Gingerbread mobile? Is this even possible without a rooted gingerbread? Where can I find a good bash terminal emulation? I need it for remote server application."#"Is it possible to change the alert sound when a new message arrives for Google Talk? My colleague and I both have Galaxy Nexus' running Jelly Bean and when either of us get a Google Talk message its very confusing! :)</p>\n\n<p>I can't see a setting for it in Google Talk and it doesn't seem to use the \"Default notification\" sound that is set under Settings -> Sound -> System.</p>\n\n<p>Thanks!</p>\n"
print(newQuestionDesc)
newQuestionWordsDesc=preprocess(cleanhtml(newQuestionDesc))


fdist = nltk.FreqDist(newQuestionWordsDesc)
for word, frequency in fdist.most_common(100):
	newQuestionCountDesc[word]=frequency
calculateTFIDFA()


for word in newQuestionWordsDesc:
	if word in allWordsDesc:
		for uid in idfDesc[word]:
			scoresDesc[uid]=0
			magnitudeDesc[uid]=0
			magnitudeBDesc[uid]=0

for word in newQuestionWordsDesc:
	if word in allWordsDesc:
		for uid in idfDesc[word]:
			x=calculateTFIDFB(uid,word)
			scoresDesc[uid]+=tfidfADesc[word]*x
			magnitudeDesc[uid]+=x*x
			magnitudeBDesc[uid]+=(tfidfADesc[word])*(tfidfADesc[word])
			uid2.append(uid)

for word in newQuestionWordsDesc:
	if word in allWordsDesc:
		for uid in idfDesc[word]:
			finalScoresDesc[uid]=scoresDesc[uid]/(magnitudeDesc[uid]**0.5 + magnitudeBDesc[uid]**0.5)

for uid in list2:
	if uid in uid1:
		similarity[uid]=0.6*finalScores[uid]
	else:
		similarity[uid]=0
	if uid in uid2:
		similarity[uid]+=0.4*finalScoresDesc[uid]
	else:
		similarity[uid]+=0

sorted_d = sorted(similarity.items(), key=operator.itemgetter(1),reverse=True)
count=0
sorted_d=dict(sorted_d)
dkeys=sorted_d.keys()
print("The top 10 questions are")
for uid in dkeys:
	print(data[uid].get("title"))
	count+=1;
	if count>50:
		break