import flavours

def checker(status): #this is a bad function name @todo(you) give it a better name
	hashtag = "#HateisHate"
	maximum = 280 - (len(hashtag) + 4) #the 4 is a magic number, idk what it's for...

	tweet = flavours.reflavour(status.text)
	if len(tweet) > maximum:
		tweet = '{}{}'.format(tweet[:maximum],'...')
	tweet = tweet + ' '
	tweet = "{}{}".format(tweet,"#HateisHate")
	return(tweet)
