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
	
	rem=[]
	
	for i in range(0,len(li)):
		li[i]=li[i].lower()
		if not (ord(li[i][0]) >= 97 and ord(li[i][0])<=122):
			rem.append(li[i])
	
	
	#print rem
	
	for r in rem:
		li=remove_from_list(li,r)
	
	for sw in stop:
		if sw in li:
			li=remove_from_list(li,sw)
		
	
	

	
	#remove extra letters like happyyyyy at end of each word
	
	for i in range(0,len(li)):
		if re.search(r'(.)\1+',li[i]):
			li[i]=re.sub(r'(.)\1+',r'\1\1',li[i])
	
	
	

	
	#print li
	
	#stemming of words
	st = LancasterStemmer()
		
	for i in range(0,len(li)):
		li[i]=st.stem(li[i])
	
	
	#print li
	
	return li			
	




fhandle=open('training.txt','r')

pos_tweets=[]
neg_tweets=[]

exclude=set(string.punctuation)

#line="""im kinda sad that da vinci code sucked("""
#line=''.join(ch for ch in line if ch not in exclude)
#processTweet(line)

for line in fhandle:
	line=''.join(ch for ch in line if ch not in exclude)
	line = line.replace("'m", " am")
	line = line.replace("'d", " would")
	line = line.replace("'ve", " have")
	line = line.replace("'ll", " will")
	line = line.replace("'s", " is")
	line = line.replace("'re", " are")
	line = line.replace("cant", "can not")
	line = line.replace("can't", "can not")
	line = line.replace("wont", "would not")
	line = line.replace("won't", "would not")
	line = line.replace("n't", " not") 
	line = line.replace("y'all", "you all")
	line = line.replace("didn't", "did not")
	
	

	if line[0]=='1':
		pos_tweets.extend(processTweet(line))
	elif line[0]=='0':
		neg_tweets.extend(processTweet(line))
	

s_pos_tweet_words=list(set(pos_tweets))
s_neg_tweet_words=list(set(neg_tweets))

#print s_neg_tweet_words
#print s_neg_tweet_words
	
	
		
		
