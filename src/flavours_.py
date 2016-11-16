#!/usr/bin/env python3
import hatedict
from random import choice

d = hatedict.dict()
FLAVOURS = hatedict.flavours()

def determine_flavours(tweet):
	'''
	preconditions: @param tweet is the text of a hateful tweet
	postconditions: returns a list of every flavour of hate contained in the tweet
	'''
	flavours = []
	for flavour in FLAVOURS:
		for slur in d[flavour]:
			if slur in tweet and flavour not in flavours:
				flavours.append(flavour)			
	return flavours


def unflavour(tweet):
	'''
	preconditions: @param tweet is the text of a hateful message
	postconditions: returns a list containing the number of flavours and slurs required from each flavour along with an unflavoured hateful message
	example output:
	[{'hate_flavour_1' : 2, 'hate_flavour_2 : 1},
	"i wish all [flavour:0,slur:1] would kill all the [flavour:1,slur:0] so we'd only have [flavour:0,slur:0] left over"]
	'''
	flavours = determine_flavours(tweet)
	flavour_index = 0
	tasteless = [{i : 0 for i in flavours}]
	for flavour in flavours:
		slur_index = 0
		for slur in d[flavour]:
			if slur == '':
				continue
			elif slur in tweet:
				tweet = tweet.replace(slur,"<flavour:{},slur:{}>".format(flavour_index,slur_index))
				slur_index = slur_index + 1
		flavour_index = flavour_index + 1
		tasteless[0][flavour] = slur_index
	tasteless.append(tweet)
	return tasteless


def flavourize(tweet, unused_flavours=None):
	'''
	preconditions: @param tweet is an unflavoured hateful message
					@param notused is (optionally) a list of 
	postconditions: returns the tweet converted to be hateful containing random slurs that are offensive to random
	'''
	#generate a list of flavours to be used in the tweet. if the
	if unused_flavours == None:
		newflavs = []
		for i in range(len(tweet[0])):
			pick = choice(FLAVOURS)
			while pick in newflavs:
				pick = choice(FLAVOURS)
			newflavs.append(pick)
	else:
		usable_flavours = []
		for flavour in FLAVOURS:
			if flavour not in unused_flavours:
				usable_flavours.append(flavour)
		#this code has some logical errors.
		newflavs = []
		unused_usable_flavours = list(usable_flavours) #some bad and confusing variable names
		for i in range(len(tweet[0])):
			if len(unused_usable_flavours) > 0:
				pick = choice(unused_usable_flavours)
				unused_usable_flavours.remove(pick)
			else:
				pick = choice(usable_flavours)

			newflavs.append(pick)


	#generate a list of slurs to be used for the freshly flavoured tweet
	newslurs = []
	for i in range(len(newflavs)):
		new_flavour = newflavs[i]
		old_flavour = unused_flavours[i] #this will crash if you call the function with out unused_flavours.
		unused_slurs = list(d[new_flavour])
		slurlist = []						#my code is actually so bad it's making me dizzy
		for n in range(tweet[0][old_flavour]):
			if len(unused_slurs) > 0:
				pick = choice(unused_slurs)
				unused_slurs.remove(pick)
			else:
				pick = choice(d[new_flavour])
			slurlist.append(pick)
		newslurs.append(slurlist)

	#give the flavourless tweet some flavour
	tweet = tweet[1]
	current_flavour_id = 0
	for i in range(len(newflavs)):
		for n in range(len(newslurs[i])):
			tweet = tweet.replace("<flavour:{},slur:{}>".format(i,n),newslurs[i][n])
	return tweet



def reflavour(tweet):
	'''
	preconditions: @param tweet is a hateful message
	postconditions: returns tweet converted to different flavours of hate
	'''
	flavours = determine_flavours(tweet)
	tweet = unflavour(tweet)
	tweet = flavourize(tweet,flavours)
	return tweet
