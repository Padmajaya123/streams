import tweepy
from textblob import TextBlob

consumer_key = 'hYns4CIVeAY6M5DlIWx3uZvH9'
consumer_key_secret = '1FqAkvl1YQ8ATQAhr2wWsCfROphCnephPDvtG3psqoWmnpq5aq'

access_token = '1254041376922140672-SPyXIIOYJaa8FjQUEjrXDxsrmXmjvr'
access_token_secret = 'cA2sU89tAuq5mGIyXRoNXFSzkXZ9fxxNfVNDTsULakRw3'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('wall')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")
