import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import json

from textblob import TextBlob

tweets = pd.read_json('../data/data.json').loc[::,['id_str', 'created_at', 'text', 'lang', 'retweet_count', 'source']]

# print(tweets.head())
# print(tweets.loc[3])


def get_tweets_opinion(tweets):
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []
    sentiment = {'polarity': [], 'subjectivity': [], 'opinion': []}

    for index, row in tweets.iterrows():
        # print(row["text"])
        raw_text = TextBlob(row["text"])
        lang = raw_text.detect_language()

        if lang != 'en':
            raw_text = raw_text.translate(to='en')

        sent = raw_text.sentiment
        #sentiment[tweet['id_str']] = sent
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

opinion = get_tweets_opinion(tweets)
sentiment = opinion['sentiment']
tweets['polarity'] = sentiment['polarity']
tweets['subjectivity'] = sentiment['subjectivity']
tweets['opinion'] = sentiment['opinion']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(tweets, x="polarity", y="subjectivity",color="opinion", color_discrete_sequence=['orange', 'green', 'red'])

app.layout = html.Div([
    html.H1('Sentiment Analysis Application'),
    html.Div([
        html.H3('Keywords and Hastgs query'),
        dcc.Input(value='Search query', type='text'),
    ]),
    html.Div([
        html.Label('Sentiment analysis graph'),
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure=fig
        )
    ]),
    html.Div([
        html.Label('Result'),
        dcc.Slider(
            min=-10,
            max=10,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(-10, 10)},
            value=0,
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)