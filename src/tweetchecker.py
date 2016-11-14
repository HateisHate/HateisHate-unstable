import flavours

def checker(tweet, status):
	tweet = flavours.reflavour(status.text)
	tweet = tweet.replace('@hateishate_', '')
	tweet = '{}{}'.format(status.user.screen_name,tweet)
	if len(tweet) > 121:
		tweet = '{}{}'.format(tweet[:121],'...')
	tweet = tweet + ' #AllHateIsEqual'
	return(tweet)
