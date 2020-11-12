import tweepy
import twitter_connection_setup as connect
from tweepy.streaming import StreamListener


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

#################### Collection utils functions ####################

'''
The collect function provides a way to collect tweets by search 

:param search: content of the search
:type search: string

:param max_content: the number of tweets collected
:type search: int

:param text: a boolean to know rather we want the text content or the whole tweet structure
:type text: boolean

:return: a list of tweets or a dictionary of text content with id of the tweet as index
:type: list tweet / dict str
'''
def collect(search, max_content=100, text=True):
    connexion = connect.twitter_setup()
    tweets = connexion.search(search,language="french",rpp=max_content)
    if not text:
        return tweets
    else:
        texts = {}
        for tweet in tweets:
            tweet['id_str'] = tweet['text']
        return texts

'''
Collect the last tweets of a user by its id
:param user_id: The id of the user we are gathering tweets from
:type search: int

:param max_content: the number of tweets collected
:type search: int

:return: a list of the last tweets of a user
:type: list tweet
'''
def collect_by_user(user_id, max_content=20):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = max_content)
    # for status in statuses:
    #     print(status.text)
    return statuses

'''
Collect the last tweets streamed using a listener
'''
def collect_by_streaming():
    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

'''
A function in order to disconnect properly from a tweepy stream
'''
def disconnect_from_streaming(stream):
    stream.disconnect()


# collect_by_streaming()
# collect_by_user(45343260)