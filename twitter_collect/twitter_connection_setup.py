import tweepy
import credentials as cred


# Initialize auth

def twitter_setup():
    """
    Initie une connexion à l'API Twitter

    :return: Connexion à Twitter
    :rtype: ???
    """
    auth = tweepy.OAuthHandler(cred.CONSUMER_KEY, cred.CONSUMER_SECRET)
    auth.set_access_token(cred.ACCESS_TOKEN, cred.ACCESS_SECRET)

    api = tweepy.API(auth)
    return api