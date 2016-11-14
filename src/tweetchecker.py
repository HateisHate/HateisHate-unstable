import flavours

def checker(tweet, status): #this is a bad function name @todo(you) give it a better name
	tweet = flavours.reflavour(status.text)
	tweet = tweet.replace('@hateishate_', '')
	tweet = '{}{}'.format(status.user.screen_name,tweet)
	if len(tweet) > 121:
		tweet = '{}{}'.format(tweet[:121],'...')
	tweet = tweet + ' #AllHateIsEqual'
	return(tweet)

def get_retweet_text(link, browser):
	"""
	preconditions:
	link is a valid link to a tweet containing retweeted text

	postconditions:
	returns the retweeted text of the tweet
	if the preconditions are not met it bad things will happen
	--maybe it throws an exception
	"""
	# if not isinstance(browser,"<class 'mechanicalsoup.browser.Browser'>"):#not sure what 2nd arg should be
	# 	return None

	#not sure how to check if link is valid, coding stuff assuming it is valid will help me find out
	retweet = browser.get(link)
	retweet = retweet.soup.findAll('div', class_="QuoteTweet-text")[0]
	retweet = retweet.text
	return retweet