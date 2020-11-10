import pandas as pd

data = pd.read_csv('dataset.csv', engine = 'python')

#pd.options.display.max_colwidth = 100

def ctrlF(text):
    return data[data['tweet'].str.contains(text)]

def tweetFromId(id):
    temp = data.loc[data['id_tweet'] == id]['tweet']
    return temp.values[0]

def plotLikeVsRT():
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.show()

