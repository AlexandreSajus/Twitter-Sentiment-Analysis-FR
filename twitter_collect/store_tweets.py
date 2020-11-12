import json
import os

def store_tweets_json(tweets,filename):
    """
    Stocke les informations utiles contenues dans les tweets passés en argument dans un fichier json
    :param tweets: La liste des tweets dont on veut récupérer les informations
    :type tweets: List
    :param filename: Chemin et nom du fichier où stocker les informations
    :type filename: Str
    """
    try :
        os.remove(filename)
    except :
        pass
    with open(filename,'a',encoding='utf-8') as db :
        my_tweets_dictionnaries = []
        for tweet in tweets :
            dico = {}
            dico["text"] = tweet.text
            dico["user_id"] = tweet.user.id
            dico["date"] = str(tweet.created_at)
            dico["tweet_id"] = tweet.id
            dico["retweets"] = tweet.retweet_count
            dico["is_a_retweet"] = tweet.retweeted
            dico["favorites"] = tweet.favorite_count
            my_tweets_dictionnaries.append(dico)
        json.dump(my_tweets_dictionnaries,db,indent = 4)