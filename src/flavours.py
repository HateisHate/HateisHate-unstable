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
	flavour = determine_flavour(tweet)
	#@todo implement this


'''
preconditions: @param tweet is the text of an unflavoured hateful message, @param flavour is a valid hate flavour
postconditions: returns the tweet converted to hate of the specified flavour
				throws some exception if given flavoured hate
'''
def flavourize(tweet, flavour):
	pass #@todo implement this


'''
preconditions: @param tweet is a hateful message, @param flavour is a valid flavour of hate
postconditions: returns tweet converted to the specified flavour
'''
def reflavour(tweet, flavour):
	pass #@todo implement this
