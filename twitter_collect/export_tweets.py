import pandas as pd
import json

def export_tweets_to_dataframe(tweets):
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