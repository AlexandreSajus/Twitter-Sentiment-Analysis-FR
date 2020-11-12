import tweepy

import twitter_connection_setup as connexion



conn = connexion.twitter_setup()



def get_replies_to_candidate(num_candidate,tweet) :



    """

    Trouve les réponses à un tweet donné du candidat num_candidate

    :param num_candidate: Le numéro du candidat concerné : il s'agit de son id Tweeter

    :type num_candidate: Int

    :param tweet: Le tweet dont on veut trouver les réponses

    :type tweet: tweet (résultat d'une requête search)

    :return: La liste des tweets émis en réponse au tweet donné en argument

    :rtype: List

    """



    name = num_candidate

    tweet_id = tweet

    replies=[]

    for tweet in tweepy.Cursor(conn.search,q='to:'+name, result_type='recent', timeout=999999).items(10):

        if hasattr(tweet, 'in_reply_to_status_id_str'):

            if (tweet.in_reply_to_status_id_str==tweet_id):

                replies.append(tweet)

    return replies