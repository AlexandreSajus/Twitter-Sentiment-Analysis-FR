from . import collect_tweet_candidate_data as datam
from . import collect_tweet_streaming as streaming
from . import collect_tweet_actuality as acuality
from . import store_tweets as storage
from . import export_tweets as export
import tweepy
from . import twitter_connection_setup as connexion

conn = connexion.twitter_setup()

def collect_actuality(num_candidate,nb_tweets):
    """
    Renvoie les réponses faites à un candidat pour ses derniers tweets
    :param num_candidate: id du compte twitter dont on souhaite observer les réponses
    :type num_candidate: Int
    :param nb_tweets: Nombre de tweets dont on souhaite obtenir les réponses
    :type nb_tweets: Int

    :return: List des réponses aux derniers tweets du compte désiré
    :rtype: List
    """
    data = []
    candidate_tweets = conn.user_timeline(id = num_candidate, count = nb_tweets)
    for tweet in candidate_tweets :
        tweet_id = tweet.id
        data = data + acuality.get_replies_to_candidate(num_candidate,tweet_id)
    return data

def collect_wanted_data(num_candidate,path,is_keyword,is_hashtag):
    """
    Renvoie les tweets comprenant les mots clés demandés dans les documents fournis par le client
    :param num_candidate: id du compte twitter dont on souhaite observer les réponses
    :type num_candidate: Int
    :param path: chemin des fichiers où sont stockés les mots clés et hashtags à rechercher
    :type path: String
    :param is_keyword: Y a-t-il un fichier de mots clés ?
    :type is_keyword: Bool
    :param is_hashtag: Y a-t-il un fichier de hashtags ?
    :type is_hashtag: Bool

    :return: Liste des tweets correspondants à la recherche effectuée
    :rtype: List
    """
    data = datam.get_tweets_from_candidates_search_queries(datam.get_candidate_query(num_candidate,path,is_keyword,is_hashtag))
    return data

def start_listener(keyword):
    """
    Ecoute les tweets contenant le mot-clé demandé
    :param keyword: Mot clé sur lequel on effectue la recherche
    :type keyword: String

    :return: Objet stream twitter
    :rtype: StdOutListener (objet personnalisé)
    """
    stream1 = streaming.listen_tweets(keyword)
    return stream1

def stop_listener(stream):
    """
    Arrête le stream passé en argument
    :param stream: Un stream twitter à fermer
    :type stream: StdOutListener (objet personnalisé)
    """
    streaming.close_stream(stream)

"""
Typical test : do not remove
tweets = collect_wanted_data(1,'data/candidate_data',True,False)
storage.store_tweets_json(tweets,'tempfile.json')
dataframe = export.export_json_to_dataframe('tempfile.json')
print(dataframe['date'])
"""