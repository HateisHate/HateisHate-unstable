import tweepy

import config
import tweetchecker

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)
sampleValue = 0
class StdOutListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status):
        parent_id = status.in_reply_to_status_id
        parent_status = api.get_status(parent_id)
        tweet_text = tweetchecker.checker(parent_statuss)
        api.update_status(tweet_text, parent_id)


    def on_error(self, status_code):
        print("on_error")
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening


    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
	listener = StdOutListener()
	print("ping!")
	stream = tweepy.Stream(auth, listener)
	stream.filter(track=['@hateishate_'])
