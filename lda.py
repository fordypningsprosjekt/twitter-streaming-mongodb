from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import json
from tools import twokenize

f = open("27jan_tweets.json", "r")

lines = f.readlines()

#tweets = [json.loads(line)["text"] for line in lines]

tweets = []

for line in lines:
	try:
		tweets.append(json.loads(line)["text"])
	except:
		continue

print len(tweets)
print len(lines)

p_stemmer = PorterStemmer()

en_stop = get_stop_words("en")

texts = [[p_stemmer.stem(token) for token in tokenizer.tokenize(doc.lower()) if not token in en_stop] for doc in tweets]

"""
tokens = [twokenize.simpleTokenize(doc.lower()) for doc in tweets]

stemmed = [[p_stemmer.stem(i) for i in token] for token in tokens]

texts = [i for i in stemmed if i not in en_stop]
"""

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = models.ldamodel.LdaModel(corpus, num_topics = 5, id2word = dictionary, passes=2)
print "Twokenize"
print ldamodel.print_topics(num_topics=5, num_words=10)
