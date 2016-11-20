#!/usr/bin/env python3
import nltk
import hatedict
SLURDICT = hatedict.slurdict()

def unflavour_slurs(tweet):
	'''
	preconditions: @param tweet is a flavourful tweet containing hateful slurs referring to people
	postconditions: @param tweet has its slurs unflavoured
	example:
	in "I wanna take my dick and shove it in a dumb slut and show that bitch who is boss."
	out [I wanna take my dick and shove it in a dumb", ["slur_misogyny",0], " and show that", ["slur_misogny",1], " who is boss."]
	This replaces the old unflavour() function
	
	note to self(aaron) don't replace slur nouns that are possessive to the first person
	'''
	pass #@todo(aaron) code this
