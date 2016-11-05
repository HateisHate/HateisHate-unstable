import tweepy, time, sys
import testconfig
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = testconfig.CONSUMER_KEY#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = testconfig.CONSUMER_SECRET#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = testconfig.ACCESS_KEY#keep the quotes, replace this with your access token
ACCESS_SECRET = testconfig.ACCESS_SECRET#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes