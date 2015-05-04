from tokenization import s_pos_tweet_words,s_neg_tweet_words
from sklearn import svm

words_features=s_pos_tweet_words+s_neg_tweet_words
words_features.sort()

#print words_features

#print len(words_features)

f_handler=open("new_training.txt","r")

x=[]
y=[]

for line in f_handler:
	s_line=line.split()
	
	tmp=[]
	
	for word in words_features:
		if word in s_line:
			tmp.append(1)
		else:
			tmp.append(0)
	
	x.append(tmp)
	
	if s_line[0]=='1':
		#positive tweet
		y.append(1)
	elif s_line[0]=='0':
		#negative tweet
		y.append(0)


#print x[0]
#print y

f_test_handler=open('new_test.txt','r')

li_test=[]

for test_line in f_test_handler:
	li_test=test_line.split()
	#print li_test

test_tweet=[]

for word in words_features:
	if word in li_test:
		test_tweet.append(1)
	else:
		test_tweet.append(0)

print test_tweet

clf=svm.SVC()
clf.fit(x,y)

print clf.predict([test_tweet])
	
