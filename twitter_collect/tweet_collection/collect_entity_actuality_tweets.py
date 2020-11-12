import tweepy
import twitter_connection_setup as connect


def get_tweets_from_candidates_search_queries(queries, twitter_api):
    connexion = connect.twitter_setup()
    tweets_list = []
    for query in queries:
        try:
            tweets = connexion.search(query,language="french",rpp=5)
            for tweet in tweets:
                tweets_list.append(tweet)
        except tweepy.TweepError:
            print('TweepError')
        except tweepy.RateLimitError:
            print('RateLimitError')
    return tweets_list