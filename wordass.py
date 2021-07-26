import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

text = ""
text = re.sub("[\[].*?[\]]", "", text)
text = re.sub(r"[^a-zA-Z0-9.]+", ' ', text)
text = str(text).lower() 


stop_words = stopwords.words('english')
desirable_tags = ['NN']

word_list = []

for sent in text.split('.'):
    for word in sent.split():
        if word not in word_list and word not in stop_words and nltk.pos_tag([word])[0][1] in desirable_tags:
            word_list.append(word)

table = np.zeros((len(word_list), len(word_list)), dtype=int)

for sent in text.split('.'):
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] in sent and word_list[j] in sent:
                table[i, j] += 1

df = pd.DataFrame(table, columns=word_list, index=word_list)

all_words = pd.DataFrame(np.zeros((len(df), 2)), columns=['Word', 'Count'])
all_words.Word = df.index

for sent in text.split('.'):
    count = 0
    for word in sent.split():
        if word in word_list:
            all_words.loc[all_words.Word == word, 'Count'] += 1

df.values[np.triu_indices_from(df, 0)] = 0  

assoc_df = pd.DataFrame(
    columns=['Word 1', 'Word 2', 'Association Strength (Word 1 -> Word 2)'])
for row_word in df:
    for col_word in df:
        assoc_df = assoc_df.append({'Word 1': row_word, 'Word 2': col_word,
                                    'Association Strength (Word 1 -> Word 2)': df[row_word][col_word]/all_words[all_words.Word == row_word]['Count'].values[0]}, ignore_index=True)

print(assoc_df.sort_values(by='Association Strength (Word 1 -> Word 2)', ascending=False))
