import json
import numpy as np
from textblob import TextBlob

# pos_tweets = []
# neu_tweets = []
# neg_tweets = []
'''
A simple function to get the list of text content of all tweets.

:param data: dictionary of tweets
:type data: dict

:return: the list of text content of all data
:type: list str
'''
def get_tweets_text(data, length):
    return np.array([data[i]["text"] for i in range(length)])

'''
This function extracts the opinion of all tweets.
It can process non english tweets by translating them and using the TextBlob english sentiment analyser.

:param arr: list of string tweets
:type arr: list

:return: a dictionary with the sentiment of all tweets based on their id and the polarity (pos, neg, neu)
:type: dict
'''
def get_tweets_opinion(tweets):
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []
    sentiment = {}

    for tweet in tweets:
        raw_text = TextBlob(tweet["text"])
        lang = raw_text.detect_language()

        if lang != 'en':
            raw_text = raw_text.translate(to='en')

        sent = raw_text.sentiment
        sentiment[tweet['id_str']] = sent
        pol = sent.polarity
        if pol > 0.0:
            pos_tweets.append(tweet)
        elif pol < 0.0:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)

    return {
        'polarity': {'pos_tweets': pos_tweets, 'neg_tweets': neg_tweets, 'neu_tweets': neu_tweets},
        'sentiment': sentiment
    }


if __name__ == "__main__":
    f = open('../data/data.json')

    tweets = np.array(json.load(f))
    length = len(tweets)

    opinion = get_tweets_opinion(tweets)
    pos_tweets = opinion['polarity']['pos_tweets']
    neg_tweets = opinion['polarity']['neg_tweets']
    neu_tweets = opinion['polarity']['neu_tweets']

    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/length))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/length))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/length))

    print(opinion['sentiment'])
    print(get_tweets_text(tweets, length))
    
    f.close()
