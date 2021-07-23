import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem.porter import PorterStemmer

def empty_set(some_set):
    return some_set == set()

def results():
    res = set(i for i in ls if subs in i)
    if empty_set(res) == False: print (str(res))

tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()

df = pd.read_csv ('internal.csv')
ls = df['Word'].tolist()

words = []

# ENTER QUERY HERE
subs = 'buy phone'
results()

raw = subs.lower()
tokens = tokenizer.tokenize(raw)
stop_words = set(stopwords.words('english'))
stopped_tokens = [subs for subs in tokens if not subs in stop_words]
words.append(stopped_tokens)

#words = subs.split()
for each in words:
    for subs in each:
        res = set(i for i in ls if subs in i)
        if empty_set(res) == False: print (str(res))
        
        else:
            synonyms = []
            for syn in wordnet.synsets(subs):
                #print(syn)
                for l in syn.lemmas():
                    synonyms.append(l.name())
            
            final = list(dict.fromkeys(synonyms))
            for new in final:
                res = set(i for i in ls if subs in i)
                if empty_set(res) == False: print (str(res))
            #print(final)