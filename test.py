import sys
import json
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem.porter import PorterStemmer

def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():

    def empty_set(some_set):
        return some_set == set()

    def results():
        res = set(i for i in ls if subs in i)
        if empty_set(res) == False: print (str(res))


    tokenizer = RegexpTokenizer(r'\w+')

    df = pd.read_csv ('internal.csv')
    ls = df['Word'].tolist()

    words = []

    # ENTER QUERY HERE
    subs = read_in()
    FINAL = []
    FINAL.append([i for i in ls if subs in i])
    #if empty_set(res1) == False: print (str(res1))

    raw = subs.lower()
    tokens = tokenizer.tokenize(raw)
    stop_words = set(stopwords.words('english'))
    stopped_tokens = [subs for subs in tokens if not subs in stop_words]
    words.append(stopped_tokens)

    #words = subs.split()
    for each in words:
        for subs in each:
            #res = set(i for i in ls if subs in i)
            #if empty_set(res) == False: 
            FINAL.append([i for i in ls if subs in i])
                #print (str(res), end=',')
            i=1
            if i==0:
                synonyms = []
                for syn in wordnet.synsets(subs):
                    #print(syn)
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                
                final = list(dict.fromkeys(synonyms))
                for new in final:
                    #res = set(i for i in ls if subs in i)
                    FINAL.append([i for i in ls if subs in i])
                #print(final)

    new = []
    i = 0
    for string in FINAL:
        if(i<=100):
            if len(string) != 0:
                new.append(string)
            i=i+1
        else: break

    # PRECISION and RECALL

    recall = 0.0
    count_rev=0
    count_tot=0
    for i in ls:
            if subs in i:
                count_rev = count_rev+1
    for i in FINAL[1]:
        if subs in i:
            count_tot=count_tot+1
    recall = count_tot/count_rev

    precision = 0.0
    count_rev=0
    count_tot=0
    for j in range(2):
        for i in FINAL[j]:
            if subs in i:
                count_rev = count_rev+1

    for i in ls:
            if subs in i:
                count_tot = count_tot+1

    #if duplicates       
    if count_rev>count_tot: count_rev=count_tot

    precision = count_rev/count_tot

    new = [[precision] + [recall]] + new

    for string in new:
        if len(string) != 0:
            print(string, end=',')


    '''
    lines = read_in()
    n = ["Holiday package", "Vacation"]
    for i in n:
        print(i,end=',');
'''
if __name__ == '__main__':
    main()
