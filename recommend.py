from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora
import gensim

tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()

import pandas
df = pandas.read_csv('phrases.csv')
ls = df['Word'].tolist()

# list for tokenized documents in loop
texts = []
doc_set = ls

for i in doc_set:

    # clean and tokenize
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stop_words = set(stopwords.words('english'))
    stopped_tokens = [i for i in tokens if not i in stop_words]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)

# id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert to a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=60, id2word = dictionary, passes=50)

unseen_document = 'tourism package'
tokens = tokenizer.tokenize(unseen_document.lower())
unseen_document = [i for i in tokens if not i in stop_words]
bow_vector = dictionary.doc2bow(unseen_document)
for index, score in sorted(ldamodel[bow_vector], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, ldamodel.print_topic(index, 5)))