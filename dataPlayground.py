"""
Quelques fonctions utiles pour la manipulation et la visualisation de données
"""
import pandas as pd
import datetime
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import matplotlib
import matplotlib.pyplot as plt

def dateToDatetime(date):

    """
    Convertit la date fournie par Twitter en objet datetime
    :param dateString: la date en format timestamp à convertir
    :type dateString: timestamp
    :return: la date en entrée en format datetime
    :rtype: objet datetime
    """

    return datetime.datetime.utcfromtimestamp(pd.Timestamp.to_datetime64(date).tolist()/1e9)

#Dataframe de test, importé en json
testDataframe = pd.read_json (r'tweets_sample.json')

def textToPolarity(text):

    """
    Donne la polarité (ressenti positif ou négatif dégagé du texte) de l'entrée texte
    :param text: texte d'entrée
    :type text: String
    :return: la polarité du texte en entrée soit une valeur flottante entre -1 et 1 (-1 pour négatif; 1 pour positif)
    :rtype: Float
    """

    x = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return x.sentiment[0]

def polarityOverTime(data):

    """
    Extrait les dates et les polarités des tweets dans data sous la forme (dates, polarites)
    :param data: dataframe contenant les tweets avec une colonne 'date' et une colonne 'texte'
    :type data: dataframe
    :return: (dates, polarites) dates une liste avec les dates des tweets de data, et polarites avec les polaritées
    :rtype: tuple
    """

    dates = []
    polarites = []

    for i in range(len(data['date'])):
        dates.append(dateToDatetime(data['date'][i]))
        polarites.append(textToPolarity(data['text'][i]))
    
    return (dates,polarites)

def plotPolarityOverTime(dates, polarites):

    """
    Plot la polarite des tweets en fonction du temps
    :param data: dates en format datetime.datetime
    :type data: List
    :param polarites: polarites en float de -1 à 1
    :type polarites: List
    """

    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, polarites)
    plt.show()

(dates, polarites) = polarityOverTime(testDataframe)
plotPolarityOverTime(dates, polarites)