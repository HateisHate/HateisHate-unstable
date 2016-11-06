#!/usr/bin/python
'''
Don't call people any of these words, it's not nice.
This list is incomplete, contributions are welcome.
'''

HATEDICT = {"sexism_misogyny" : ["maid", #this one will be difficult to do right, could also refer to hispanics
								"slut",
								"whore",
								"bitch",
								"cunt"
								"cumslut" #slut is in cumslut, might be redundant
				],
			"sexism_misandry" : ["no balls",
								"pussy",
								"dick",
								"fuckboy",
								"fuckboi",
								"douchebag"
				],
			"sexism_transphobia" : ["tranny",
								"he-she",
								"thot",
								"shemale"
				],
			"sexism_heterophobia" : ["cishet"
								"het",
								"vanilla",
								"cis"
				],
			"sexism_homophobia" : ["fairy",
								"faggot",
								"dyke",
								"twink",
								"queer",
								"gay",
								"fag"
				],
			"racism_asain" : ["chink",
								"squinty",
								"kimchi",
								"curry-muncher",#just curry?
								"ching-chong",#ching.chong so it matches space or hyphen?
								"gook",
								"yigger",
								"winky",
								"rice nigger"
				],
			"racism_african" : [#"nigger",
								"spook",
								"crow",
								"monkey",#just monkey?
								"coon",
								"mosshead",
								"sausage lips",
								"african't",
								"ape"
				],
			"racism_caucasian" : ["wigger",
								"whitey",
								"cracker",
								"klansman",
								"cornfed",
								"white bread",
								"redneck",
								"hick"
				],
			"racism_middle-eastern" : ["turban"
								"towel head",
								#"sand nigger",
								"goatfucker"
				],
			"racism_antisemitism" : ["abe",
								"big nose",
								"kike",
								"kyke",
								"goyim",
								"oven-dweller"
				],
			"racism_native_american": ["prarie nigger",
								"savage",
								"redskin",
								"injun",
								"half-breed",#use a . for regex?
								"chug"
				]
	
}

FLAVOURS = ["sexism_misogyny",
			"sexism_misandry",
			"sexism_transphobia",
			"sexism_heterophobia",
			"sexism_homophobia",
			"racism_asain",
			"racism_african",
			"racism_caucasian",
			"racism_middle-eastern",
			"racism_antisemitism",
			"racism_native_american"]

#returns the hatedictionary
def dict():
	return HATEDICT

#returns a list of the flavours of hate the hatedictionary currently supports
def flavours():
	return FLAVOURS