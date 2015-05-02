import string
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer


def remove_from_list(dli,dsw):
	return [value for value in dli if value!=dsw]

def processTweet(line):
	#removing stop words
	stop=stopwords.words('english')
	li=line.split()[1:]
	
	for i in range(0,len(li)):
		li[i]=li[i].lower()
	
	
	for sw in stop:
		if sw in li:
			li=remove_from_list(li,sw)
		
	
	

	
	#remove extra letters like happyyyyy at end of each word
	
	for i in range(0,len(li)):
		if re.search(r'(.)\1+',li[i]):
			li[i]=re.sub(r'(.)\1+',r'\1\1',li[i])
	
	
	print li

	
	
	#stemming of words
"""	st = LancasterStemmer()
		
	for i in range(0,len(li)):
		li[i]=st.stem(li[i])"""
	
	
	
			
	




fhandle=open('training.txt','r')

pos_tweets=[]
negative_tweets=[]

exclude=set(string.punctuation)

#line="""How?.-Mission Impossible III is really boring the second time around..-The new Cobequid health center is soooooooo nice!..."""
#line=''.join(ch for ch in line if ch not in exclude)
#processTweet(line)

for line in fhandle:
	line=''.join(ch for ch in line if ch not in exclude)
	if line[0]=='1':
		processTweet(line)
		#pos_tweets.append()
	elif line[0]=='0':
		processTweet(line)
		#neg_tweets.append()
		
