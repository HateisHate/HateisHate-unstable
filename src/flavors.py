#!/usr/bin/python
'''

'''


'''
preconditions: @param tweet is a hateful tweet
postconditions: returns the flavour of tweet
'''
def determine_flavour(tweet):
	pass #@todo implement this


'''
preconditions: @param tweet is a hateful message
postconditions: returns tweet converted to unflavoured hate
'''
def unflavour(tweet):
	flavour = determine_flavour(tweet)
	#@todo implement this


'''
preconditions: @param tweet is an unflavoured hate, @param flavour is a valid hate flavour
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
