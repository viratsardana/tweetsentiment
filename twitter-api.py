import tweepy

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

consumer_key='J3NKH4h3wtsmJPbiBz3DcG37F'
consumer_secret='CrKwE0FOOxPscwkHiEcb5rNJS6BgMRBlusYgeS1cKN59m7EzEK'

access_token='1598837467-Z6Oid3Ot7rtRPB2jxA6W57AeGGXTIHyAjfiE4vZ'
access_token_secret='TLrOYZH7SFebDBr9QfkUMIB9z2TTUwTP1jA81U3xGGd58'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets=[]
public_tweets = api.home_timeline()

for tweet in public_tweets:
	print tweet.text

res=tweepy.Cursor(api.search, q='ebola').items(10)

for tweet in res:
	print tweet.text
