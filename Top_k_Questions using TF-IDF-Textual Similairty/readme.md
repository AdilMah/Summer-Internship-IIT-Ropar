Top-k Questions using TF-IDF(Textual Similarity)

This repository contains all the scripts that have been written for getting the top-k questions from the existing question based on the new question. The following are the detailed descriptions of the files in the repository:

Python Scripts:
“preprocess.py”-This file includes the necessary functions that are used to clean the dataset that includes tokezing the sentences, removing html tags and also removing the stop words.

“ask_question.py”- This files takes the question from the user and calculates the question title similarity with all the existing questions.

“qdet.py”- File that loads the data set in the json format and stores all the key values in the dictionary.

“Qdf.py”- File that calculates the similarity between the question description as well as calculates the overall similarity with all the existing questions and stores them it in a python dictionary.The top-k questions from the dictionary is then presented to the user.

Preprocessed dataset in JSON format:
Using the raw dataset for all the calculations would take time forever. In order to make the final processing a lot more time efficient, several preprocessed files are used that include the following:

“allwords.json”-File that consists of all the unique words in the question titles of the existing questions.

“allwordsDesc”-File that consists of all the unique words in the question description of the existing questions.

“WordDocumentCount.json”- This file consists of the inverted lists of words. An inverted list of word consists of words followed by all the question uids in which the word is present. This is extremely useful when calculating the inverse document frequency of a word.

“WordFrequencyCount.json”- Consists of all the question uids followed by the frequency of each word in the question title.
 
““WordFrequencyCountDesc.json”- Consists of all the question uids followed by the frequency of each word in the question description.”

Python NLTK package has been extremely useful for this work. Information about the rest of the package can be found by the import section of the scripts.


  
