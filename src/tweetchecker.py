import tweepy
import flavours

def checker(tweet, status):
    tweet = flavours.reflavour(status.text)
    tweet = tweet.replace('@hateishate_', '')
    tweet = '{}{}'.format(tweet,status.user.screen_name)
    if len(tweet) > 121:
        tweet = '{}{}'.format(tweet[:121],'...')
    tweet = tweet + ' #AllHateIsEqual'
    return(tweet)