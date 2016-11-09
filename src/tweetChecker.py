import tweepy
import flavours

def checker(tweet, status):
    tweet = flavours.reflavour(status.text)
    tweet = tweet.replace('@hateishate_', '{}{}'.format('@',status.user.screen_name))
    tweet = tweet.replace('@hateishate_', '')
    if len(tweet) > 121:
        tweet = '{}{}'.format(tweet[:121],'...')
    tweet = tweet + ' #AllHateIsEqual'
    return(tweet)