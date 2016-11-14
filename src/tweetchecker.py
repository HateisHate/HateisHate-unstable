import flavours
import mechanicalsoup

def checker(tweet, status):
	tweet = flavours.reflavour(status.text)
	tweet = tweet.replace('@hateishate_', '')
	tweet = '{}{}'.format(status.user.screen_name,tweet)
	if len(tweet) > 121:
		tweet = '{}{}'.format(tweet[:121],'...')
	tweet = tweet + ' #AllHateIsEqual'
	return(tweet)

def get_retweet_text(link):
	"""
	preconditions:
	link is a valid link to a tweet containing retweeted text

	postconditions:
	returns the retweeted text of the tweet
	if link is not valid then it returns None (@todo(aaron) make it return something more useful)
	-more useful things it might return in the future:
	--maybe it throws an exception
	"""
	pass