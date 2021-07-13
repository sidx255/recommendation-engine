import io
import codecs
import csv
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

file1 = codecs.open('phrases.csv', 'r', 'utf-8')
line = file1.read()
words = line.split()

for r in words:
    if not r in stop_words:
        appendFile = open('phrases1.csv', 'a', encoding='utf-8')
        appendFile.write(r)
        appendFile.write("\n")
        appendFile.close()
        

time.sleep(1)
"""
with open('phrases.csv','r') as in_file, open('phrases1.csv','w') as out_file:
    seen = set() # O(1)
    for line in in_file:
        if line in seen: continue # skip duplicate
        seen.add(line)
        out_file.write(line)
        """