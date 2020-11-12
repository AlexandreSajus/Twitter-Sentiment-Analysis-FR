import json


def store_tweets_json(tweets,filename):
    try :
        existence_test = open(filename,'r')
        existence_test.close()
    except IOError :
        create_file = open(filename,'w')
        create_file.close()
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
