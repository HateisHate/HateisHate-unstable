import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'QaOoBbqePcDo7MAPzm4TaFko6'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Mt9uDjF8BesRVcf9WRBr4jpMekfhhSIxTdSsQTeqayKpnYT8OS'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '794962026376335360-wb0z18a5LV6Nkg8bYbeIbeDdMXCDfAa'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'ITpsMfQdi19o6hQiWCYcxw5i1tZYpSOLacVDxx5EG3XF5'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes