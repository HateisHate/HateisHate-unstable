#!/usr/bin/python
'''
this module should contain functions and shit that implement the anti bullying ideas I had
tl;dr of the ideas
open dms on the bot
dm the username of a cyberbully
every time the cyberbully posts an abusive tweet reply to them "Hey stop that!"
use bark api to determine if the tweets are abusive
if a tracked cyberbully stops being abusive then they will stop being tracked and the person(s) who originally reported them will be notified
'''

#todo(aaorn) code this
#so we have to probably have a database for storing all the data about the people's hatefulness
'''
keep info about their average hate level
some messages....
You're always so hateful, can you tone it down?
That's not nice!
Hey, stop that!
Don't bully!
etc
also it compares their current hate level to their average level. if they are at the highest level displays more intense messages
'''


'''
WHEW!
Looks like I'm going to actually need some practical dba knowledge of dba...
Figure out how to structure the databse and then build the program on that.

if by databse you mean a fuckload of JSON files then you're right.
not only will this be a bad idea and result in an unmanageable 'database' but it will also
be a very very valuable lesson. then i'll learn some proper dba skills (but not enough of them)
'''
#SHOUT OUTS TO FUTURE ME
#I BET HES GONNA LOVE THIS idea
#LIKE WOW I CAN TOTALLY DO THIS WHEE
#heheheEHEHEHEHEHHHhdhdhdhdhdhdheheheheh
#but rught now its 5:12 am and i wnna go some sleep, too bad this room is so alien
import tweepy
import tweetchecker

#honetly this isn't really the time for object oriented programming, but it might make my life easier
class BullyRanger:
	def __init__(self, loadfile, BARK_TOKEN):
		f = open(loadfile)
		wRiTe_A_bEtTeR_vArNaMe = f.read()
		f.close()
		dmdb = ['dmdb'] #dmdb stands for Direct Message Database
		last_unprocessed_dm = ['last_unprocessed_dm']
		DEFAULT_REPUATION = None #how does reputation work?
		ENTRY_TEMPLATE = {"bully" : None, "reputation" : DEFAULT_REPUATION, "dmid" : None}

	def run():
		#get a stream of dms
			#process the dms
				#check for people reporting cyberbullies
					#people are going to report it differently	
						#enforce a syntax (safe option, no chance for misfies)
						#try to parse natural langage (i will probably never write this)
		#get a stream of monitored tweets
			#process the tweets
				#if hateful reset reutation
				#if not hateful tweet improve reputation
		#repeat
		pass