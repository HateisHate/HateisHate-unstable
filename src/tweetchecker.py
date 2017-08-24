import flavours

def checker(status): #this is a bad function name @todo(you) give it a better name
	hashtag = "#HateisHate"
	maximum = 140 - (len(hashtag) + 4)

	tweet = flavours.reflavour(status.text)
	if len(tweet) > maximum:
		tweet = '{}{}'.format(tweet[:maximum],'...')
	tweet = tweet + ' '
	tweet = "{}{}".format(tweet,"#HateisHate")
	return(tweet)
