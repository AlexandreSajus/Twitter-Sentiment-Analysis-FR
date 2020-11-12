import tweepy
import json
import twitter_connection_setup as connexion
from tweepy.streaming import StreamListener

conn = connexion.twitter_setup()

class StdOutListener(tweepy.StreamListener):  #Stocker puis exporter les tweets reçus à la fermeture
    
    def on_data(self, data):
        my_data = json.loads(data)
        try :
            print(my_data['text'])
        except :
            print("il n'y avait pas de texte")
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def listen_tweets(keyword) :
    """
    Ecoute et capture les tweets relatifs au candidat, ainsi que les réponses à ses tweets
    :param num_candidate: Le numéro du candidat concerné : il s'agit de son id Tweeter
    :type num_candidate: Int

    :return: La liste des retweets du tweet donné en argument
    :rtype: List
    """
    username = candidate_username
    listener1 = StdOutListener()
    stream1=tweepy.Stream(auth = conn.auth, listener=listener1)
    stream1.filter(track=[keyword])
    return stream1

def close_stream(stream):
    stream.disconnect()