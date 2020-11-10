from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.wordnet import Synset

# wiki = TextBlob("Python is a high-level, general-purpose programming language.")

# print(wiki.tags)
# print(wiki.noun_phrases)

# testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
# print(testimonial.sentiment)
# print(testimonial.sentiment.polarity)

# zen = TextBlob("blablou")
# for sentence in zen.sentences:
#     print(sentence.sentiment)

# w = Word("octopus")
# print(w.lemmatize())
# print(w.synsets)

# print(Word("hack").get_synsets(pos=VERB))
# print(Word("black").definitions)

# test = Synset('test.n.01')
# analysis = Synset('analysis.n.05')
# print(analysis.path_similarity(test))


'''
This function extracts all words from an array of tweets adn return a set of these lemmatized words.

:param arr: list of string tweets
:type arr: str

:return: the list of unique lemmatized lowered words
:type: list str
'''
def extract(arr):
    sentences = TextBlob('. '.join(arr))
    words = sentences.words.lower().lemmatize()
    return set(words)


'''
This function extracts all unique words from an array of tweets.
It works by parsing all unique lemmatized and lowered words before checking their count in the sentences and return the list of unique words.

:param arr: list of string tweets
:type arr: str

:return: the list of unique lemmatized lowered words which appear once
:type: list str
'''
def extract_unique(arr):
    lst = []
    sentences = TextBlob('. '.join(arr))

    for word in set(sentences.words.lower().lemmatize()):
        if sentences.words.count(word, case_sensitive=False) == 1:
            lst.append(Word(word.lower()))
    return lst

lst = extract_unique(["this is a test", "The test is a pretty little chick. ", "yes it is the pretty"])
print(lst)