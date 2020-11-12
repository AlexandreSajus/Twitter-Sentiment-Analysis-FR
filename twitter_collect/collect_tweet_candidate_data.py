"""
Format des documents à placer en entrée : Tous les mots clés en ligne, séparés par des virgules, sur une seule ligne.
NE PAS METTRE D'ESPACES AVANT OU APRES LES VIRGULES !!!!
Pour les hashtag, le symbole # DOIT être inclus dans le document pour chaque entrée
Les normes de nom des fichiers sont celles du sujet, à savoir :
    - le fichier des mots clés est keywords_candidate_x.txt où x est le numéro du candidat
    - le fichier des hashtags est hashtags_candidate_x.txt où x est le numéro du candidat
"""

import tweepy
import twitter_connection_setup as connexion

conn = connexion.twitter_setup()

def get_candidate_query(candidate_number,path,is_keyword,is_hashtag):
    """
    Renvoie la liste des requêtes associées au candidat candidate_number
    :param candidate_number: Numéro du candidat concerné
    :type candidate_number: Int
    :param path: chemin jusqu'aux fichiers de données fournis par le client
    :type path: Str
    :param is_keyword: Y a-t-il un fichier de mots-clés ?
    :type is_keyword: Bool
    :param is_hashtag: Y a-t-il un fichier de hashtags ?
    :type is_hashtag: Bool

    :return: Liste des requêtes à effectuer
    :rtype: List
    """
    try :
        klist = []
        hlist = []
        if is_keyword :
            kfile_name = "keywords_candidate_" + str(candidate_number) + ".txt"
            with open(path + '/' + kfile_name,'r') as kfile : 
                lignes = kfile.readlines()[0].split(',')
                klist = lignes

        if is_hashtag :
            hfile_name = "hashtags_candidate_" + str(candidate_number) + ".txt"
            with open( path + '/' + hfile_name,'r') as hfile : 
                lignes = hfile.readlines()[0].split(',')
                hlist = lignes
        return hlist + klist
    except OSError:
        print('OSError : probably wrong path. Beware of candidate number which could be false')
    except :
        print("unexpected error : probably not a path problem")


def get_tweets_from_candidates_search_queries(queries) :
    """
    Récupère les tweets correspodants aux mot-clés entrés en paramètre
    :param queries: La liste de tous les mots clés ou hashtag que l'on doit rechercher dans Twitter
    :type queries: List
    :param twitter_api: La connexion à l'API twitter
    :type twitter_api: ??? (tweepy.API)

    :return: La liste des tweets qui correspondent aux mots clé demandés
    :rtype: List
    """
    tweets = []
    for element in queries :
        try :
            tweets_wanted = conn.search(element,rpp=100)
        except tweepy.TweepError :
            print("an error occured on query " + element + ".")
            try :
                print("The error is " + tweepy.TweepError.response.text)
            except :
                pass
        except :
            print("unexpected error occured, probably not directly related to tweepy")
        for tweet in tweets_wanted :
            tweets.append(tweet)

    return tweets