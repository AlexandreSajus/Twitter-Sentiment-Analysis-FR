
import pandas as pd
import numpy as np

import json
import csv

from textblob import TextBlob

def get_tweets_opinion(tweets):
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []
    sentiment = {'polarity': [], 'subjectivity': [], 'opinion': []}

    for index, row in tweets.iterrows():
        raw_text = TextBlob(row["text"])
        lang = raw_text.detect_language()

        if lang != 'en':
            raw_text = raw_text.translate(to='en')

        sent = raw_text.sentiment
        sentiment['polarity'].append(sent.polarity)
        sentiment['subjectivity'].append(sent.subjectivity)
        pol = sent.polarity
        if pol > 0.0:
            sentiment['opinion'].append('positive')
            pos_tweets.append(row)
        elif pol < 0.0:
            sentiment['opinion'].append('negative')
            neg_tweets.append(row)
        else:
            sentiment['opinion'].append('neutral')
            neu_tweets.append(row)

    return {
        'polarity': {'pos_tweets': pos_tweets, 'neg_tweets': neg_tweets, 'neu_tweets': neu_tweets},
        'sentiment': sentiment
    }

def collectPolarity(keywordsList):
    import twitter_collect as tc
    tweets = tc.collect_tweet_candidate_data.get_tweets_from_candidates_search_queries(keywordsList)
    dataframe = tc.export_tweets.export_tweets_to_dataframe(tweets)
    tweets = dataframe
    opinion = get_tweets_opinion(tweets)
    sentiment = opinion['sentiment']
    tweets['polarity'] = sentiment['polarity']
    tweets['subjectivity'] = sentiment['subjectivity']
    tweets['opinion'] = sentiment['opinion']
    return tweets