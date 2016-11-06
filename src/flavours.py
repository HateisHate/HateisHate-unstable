#!/usr/bin/python
import hatedict
'''
some functions for working with various hateful things
'''

d = hatedict.dict()
f = hatedict.flavours()

'''
preconditions: @param tweet is the text of a hateful tweet
postconditions: returns a list of every flavour of hate contained in the tweet
'''
def determine_flavours(tweet): #what if there's more than one flavour?
	flavours = []
	for flavour in f:
		for slur in d[flavour]:
			if slur in tweet:
				if flavour not in flavours:
					flavours.append(flavour)			
	return flavours

'''
preconditions: @param tweet is the text of a hateful message
postconditions: returns a list containing the number of flavours and slurs required from each flavour along with an unflavoured hateful message
example output:
[{'hate_flavour_1' : 2, 'hate_flavour_2 : 1},
"i wish all [flavour:0,slur:1] would kill all the [flavour:1,slur:0] so we'd only have [flavour:0,slur:0] left over"]
'''
#RUBBER FUCKIN Ducks this is the old version of unflavour 
#BOTH DONT WORK, BUT IT TURNS OUT determine_flavours() WAS BROKEN AND I FIXED IT HAHA
def unflavour(tweet):
	flavours = determine_flavours(tweet)
	print(str(flavours)+"flacass")
	flav_i = 0
	for flavour in flavours:
		slur_i = 0
		for slur in d[flavour]:
			if slur == '': #for some reason d[flavour] had lots of empty strings
				continue
			tweet = tweet.replace(slur,"[flavour:{},slur:{}]".format(slur_i,flav_i))
			slur_i = slur_i + 1
		flav_i = flav_i + 1
	return tweet

def unflavour_(tweet):
	flavours = determine_flavours(tweet)
	returnme = [{i : 0 for i in flavours}]
	flav_i = 0
	for flavour in flavours:
		slur_i = 0
		fai = False #flav_i already incremented (only want to increment it once per flavour)
		for slur in d[flavour]:
			if slur == '': #for some reason d[flavour] had lots of empty strings
				continue
			if slur in tweet:
				if not fai:
					fai = True
					flavr_i = flav_i + 1
				slur_i = slur_i + 1
				tweet = tweet.replace(slur,"[flavour:{},slur:{}]".format(slur_i,flav_i))
		returnme[0][flavour] = slur_i

	returnme.append(tweet)
	return returnme
	


'''
preconditions: @param tweet is the text of an unflavoured hateful message
				@param notused is (optionally) a list of 
postconditions: returns the tweet converted to be hateful containing random slurs that are offensive to random
'''
def flavourize(tweet, notused=None):
	#determine the number of flavours which need to be used
	#randomly select new flavours
	#determine how many slurs are needed from each flavour
	#randomly select new slurs
	#populate the generic hate message with freshly chosen flavourful slur
	pass


'''
preconditions: @param tweet is a hateful message
postconditions: returns tweet converted to different flavours of hate
'''
def reflavour(tweet):
	flavours = determine_flavours(tweet)
	tweet = unflavour(tweet)
	tweet = flavourize(tweet,flavours)
	return tweet
