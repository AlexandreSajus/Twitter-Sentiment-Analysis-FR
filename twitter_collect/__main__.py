import collect_tweet_candidate_data as datam
import collect_tweet_streaming as streaming
import collect_tweet_actuality as acuality
import store_tweets as storage
import export_tweets as export
import tweepy
import twitter_connection_setup as connexion

conn = connexion.twitter_setup()

def collect_actuality(num_candidate,nb_tweets):
    """
    Renvoie les réponses faites à un candidat
    """
    data = []
    candidate_tweets = conn.user_timeline(id = num_candidate, count = nb_tweets)
    for tweet in candidate_tweets :
        tweet_id = tweet.id
        data = data + acuality.get_replies_to_candidate(num_candidate,tweet_id)
    return data

def collect_wanted_data(candidate_number,path,is_keyword,is_hashtag):
    """
    Renvoie les tweets comprenant les mots clés demandés dans les documents fournis par le client
    """
    data = datam.get_tweets_from_candidates_search_queries(datam.get_candidate_query(candidate_number,path,is_keyword,is_hashtag))
    return data

def start_listener(keyword):
    """
    Ecoute les réponses aux tweets du candidat, ainsi que les retweets des tweets du candidat
    """
    stream1 = streaming.listen_tweets(keyword)
    return stream1

def stop_listener(stream):
    """
    Arrête l'écoute.
    """
    streaming.close_stream(stream)