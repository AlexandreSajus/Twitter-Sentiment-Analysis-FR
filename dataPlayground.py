"""
Quelques fonctions utiles pour la manipulation et la visualisation de données
"""
import pandas as pd
import datetime
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

def dateToDatetime(dateString):

    """
    Convertit la date fournie par Twitter en objet datetime
    :param dateString: la date en format Twitter à convertir
    :type dateString: String
    :return: la date en entrée en format datetime
    :rtype: objet datetime
    """

    months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
    year = int(dateString[26:30])
    month = int(months[dateString[4:7]])
    day = int(dateString[8:10])
    hour = int(dateString[11:13])
    minute = int(dateString[14:16])
    second = int(dateString[17:19])

    return datetime.datetime(year,month,day,hour,minute,second)

def test_dateToDatetime():
    assert dateToDatetime("Sat Mar 29 15:31:11 +0000 2014") == datetime.datetime(2014,3,29,15,31,11)

#Dataframe de test
testDataframe = {'texte': ['le cinéma est très bien','le cinéma est bien','le cinéma est moyen','le cinéma est pas terrible','le cinéma est vraiment nul'],
'date' : ["Sat Mar 10 15:31:11 +0000 2014","Sat Mar 10 21:31:11 +0000 2014","Sat Mar 11 15:31:11 +0000 2014","Sat Mar 12 15:31:11 +0000 2014","Sat Mar 13 15:31:11 +0000 2014"]}
testDataframe = pd.DataFrame(data=testDataframe)

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
        polarites.append(textToPolarity(data['texte'][i]))
    
    return (dates,polarites)

print(polarityOverTime(testDataframe))
