import yake
import csv
from nltk.corpus import wordnet
import numpy as np

kw_extractor = yake.KeywordExtractor()
text = """holiday packages"""
language = "en"
max_ngram_size = 1
deduplication_threshold = 0.9
numOfKeywords = 5
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

synonyms = []
for fw in keywords:
    print(fw)

for i in range(len(keywords)):
    for syn in wordnet.synsets(keywords[i][0]):
        for l in syn.lemmas():
            synonyms.append(l.name())

print(synonyms)

final = list(dict.fromkeys(synonyms))

for i in final:
    if '_' in i:
        final.remove(i)


with open('URL.csv', encoding="utf8", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def common(a,b): 
    c = [value for value in a if value in b] 
    return c

d=common(data,final)