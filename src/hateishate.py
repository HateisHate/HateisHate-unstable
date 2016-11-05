#!/user/bin/python
import tweepy, time, sys
import config
 
#put your keys in config.py
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_KEY = config.ACCESS_KEY
ACCESS_SECRET = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	pass
	#check for mentions
	#convert the hate
	#reply to the mentioning tweet