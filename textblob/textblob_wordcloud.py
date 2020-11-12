from wordcloud import WordCloud
from textblob import TextBlob
from textblob_utils import extract

import numpy as np

import json

f = open('../data/data.json')
tweets = np.array(json.load(f))

wc = WordCloud(background_color='white', width = 300, height=300, margin=2)

txt = ""
for t in tweets:
    txt += t["text"]
sentences = TextBlob(txt)
words = sentences.words.lower().lemmatize()
text = ' '.join(words)

wc.generate(text)
wc.to_file('tweet.png')

f.close()