import yake
import csv
from nltk.corpus import wordnet

"""Extract keywords from SEARCH QUERY"""
kw_extractor = yake.KeywordExtractor()
text = """holiday packages"""
language = "en"
max_ngram_size = 1
deduplication_threshold = 0.9
numOfKeywords = 5
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

"""Find synonyms of  keywords from SEARCH QUERY"""
synonyms = []
for fw in keywords:
    print(fw)

for i in range(len(keywords)):
    for syn in wordnet.synsets(keywords[i][0]):
        for l in syn.lemmas():
            synonyms.append(l.name())

final = list(dict.fromkeys(synonyms))

"""Find if the extracted synonyms are in URL.csv"""
with open('URL.csv', encoding="utf8", newline='') as f:
    reader = csv.reader(f)
    reader = [row[0].split("-")[0] for row in reader]
    data = list(reader)

def common(a,b): 
    c = [value for value in a if value in b] 
    return c

d=common(data,final)
print(d)
