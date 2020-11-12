import pandas as pd
import json

def export_tweets_to_dataframe(tweets):
    """
    Transforme une liste de tweets en un dataframe. Attention : la structure du dataframe n'est pas souple !
    :param tweets: La liste des tweets à traiter
    :type tweets: List

    :return: Le dataframe contenant les informations contenues dans les tweets
    :rtype: Pandas.Dataframe
    """
    n = len(tweets)
    dataframe = pd.DataFrame(columns=['text','user_id','date','tweet_id','retweets','is_a_retweet','favorites'])
    for i in range(n):
        dico = {}
        dico["text"] = tweets[i].text
        dico["user_id"] = tweets[i].user.id
        dico["date"] = tweets[i].created_at
        dico["tweet_id"] = tweets[i].id
        dico["retweets"] = tweets[i].retweet_count
        dico["is_a_retweet"] = tweets[i].retweeted
        dico["favorites"] = tweets[i].favorite_count
        dataframe = dataframe.append(dico,ignore_index=True)
    return dataframe


def export_json_to_dataframe(filepath):
    """
    Exporte les informations contenues dans un fichier json dans un dataframe Pandas
    :param filepath: Le chemin d'acces du fichier json à traiter
    :param filepath: Str

    :return: Le dataframe contenant les informations du json
    :rtype: Pandas.Dataframe
    """
    return pd.read_json(filepath).loc[::,["text","user_id","date","tweet_id","retweets","is_a_retweet","favorites"]]