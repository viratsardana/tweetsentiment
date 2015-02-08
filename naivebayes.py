#tweet sentiment using naive bayes

import nltk
import string


fhandle=open('training.txt','r')

pos_tweets=[]
neg_tweets=[]


##need to remove all the punctuations from the string## 
exclude=set(string.punctuation)

for line in fhandle:
	line=''.join(ch for ch in line if ch not in exclude)
	if(line[0]=='1'):
		pos_tweets.append((line[2:len(line)-1],'positive'))
	elif(line[0]=='0'):
		neg_tweets.append((line[2:len(line)-1],'negative'))

#print pos_tweets
#print neg_tweets

tweets=[]



for (words,sentiment) in pos_tweets + neg_tweets:
	words_filtered=[word.lower().rstrip('?:!.,;').lstrip('?:!.,;') for word in words.split() if len(word)>=3]
	tweets.append((words_filtered,sentiment))

#print tweets

def get_words_in_tweets(tweets):
	words_list=[]
	for(words,sentiment) in tweets:
		words_list.extend(words)
	return words_list

def get_word_feature(words_list):
	words_dict=nltk.FreqDist(words_list)
	words_features=words_dict.keys()
	return words_features


words_features=get_word_feature(get_words_in_tweets(tweets))

#may need improvement..not sure what to do with emoticons at the moment
print words_features

def extract_features(document):
	document_words=set(document)
	features={}
	for word in words_features:
		features['contains(%s)' %word]=(word in document_words)
	return features
		
	


