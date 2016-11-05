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
	returnme = []
	for flavour in f:
		for slur in d[flavour]:
			if slur in tweet:
				returnme.append(flavour)
	return returnme


'''
preconditions: @param tweet is the text of a hateful message
postconditions: returns tweet converted to unflavoured hate
'''
def unflavour(tweet):
	flavours = determine_flavours(tweet)
	flav_i = 0
	for flavour in flavours:
		slur_i = 0
		for slur in d[flavour]:
			if slur == '': #for some reason d[flavour] had lots of empty strings
				continue
			tweet =tweet.replace(slur,"[flavour:{},slur:{}]".format(slur_i,flav_i))
			slur_i = slur_i + 1
		flav_i = flav_i + 1
	return tweet
	


'''
preconditions: @param tweet is the text of an unflavoured hateful message
				@param notused is (optionally) a list of 
postconditions: returns the tweet converted to be hateful containing random slurs that are offensive to random
'''
def flavourize(tweet, notused=None):
	pass #@todo implement this


'''
preconditions: @param tweet is a hateful message
postconditions: returns tweet converted to the specified flavour
'''
def reflavour(tweet):
	flavours = determine_flavours(tweet)
	tweet = unflavour(tweet)
	tweet = flavourize(tweet,flavours)
	return tweet
