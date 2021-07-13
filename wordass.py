import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

# The first paragraph of Wikipedia's article on itself - you can try with other pieces of text with preferably more words (to produce more meaningful word pairs)
text = ""
# Remove brackets and anything inside it.
text = re.sub("[\[].*?[\]]", "", text)
# Remove special characters except spaces and dots
text = re.sub(r"[^a-zA-Z0-9.]+", ' ', text)
text = str(text).lower()  # Convert everything to lowercase
# Can add other preprocessing steps, depending on the input text, if needed.


stop_words = stopwords.words('english')

# We want only nouns - can also add 'NNP', 'NNS', 'NNPS' if needed, depending on the results
desirable_tags = ['NN']

word_list = []

for sent in text.split('.'):
    for word in sent.split():
        '''
        Extract the unique, non-stopword nouns only
        '''
        if word not in word_list and word not in stop_words and nltk.pos_tag([word])[0][1] in desirable_tags:
            word_list.append(word)


'''
Construct the association matrix, where we count 2 words as being associated 
if they appear in the same sentence.

Later, I'm going to define associations more properly by introducing a 
window size (say, if 2 words seperated by at most 5 words in a sentence, 
then we consider them to be associated)
'''


table = np.zeros((len(word_list), len(word_list)), dtype=int)

for sent in text.split('.'):
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] in sent and word_list[j] in sent:
                table[i, j] += 1

df = pd.DataFrame(table, columns=word_list, index=word_list)


# Count the number of occurrences of each word in word_list

all_words = pd.DataFrame(np.zeros((len(df), 2)), columns=['Word', 'Count'])
all_words.Word = df.index

for sent in text.split('.'):
    count = 0
    for word in sent.split():
        if word in word_list:
            all_words.loc[all_words.Word == word, 'Count'] += 1


# Sort the word pairs in decreasing order of their association strengths

df.values[np.triu_indices_from(df, 0)] = 0  # Make the upper triangle values 0

assoc_df = pd.DataFrame(
    columns=['Word 1', 'Word 2', 'Association Strength (Word 1 -> Word 2)'])
for row_word in df:
    for col_word in df:
        '''
        If Word1 occurs 10 times in the text, and Word1 & Word2 occur in the same sentence 3 times,
        the association strength of Word1 and Word2 is 3/10 - Please correct me if this is wrong.
        '''
        assoc_df = assoc_df.append({'Word 1': row_word, 'Word 2': col_word,
                                    'Association Strength (Word 1 -> Word 2)': df[row_word][col_word]/all_words[all_words.Word == row_word]['Count'].values[0]}, ignore_index=True)

print(assoc_df.sort_values(by='Association Strength (Word 1 -> Word 2)', ascending=False))
