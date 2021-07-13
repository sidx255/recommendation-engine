import nltk
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import tokenize
from operator import itemgetter
import math
import pandas as pd
from nltk.util import ngrams

import matplotlib.pyplot as plt


def check_sent(word, sentences):
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))


text = """
Writing is an important skill. We should motivate writing as a pre requisite.
"""
text = text.lower();

# tokenzixed text
tokenized_text = sent_tokenize(text)
number_of_sentences = len(tokenized_text)
# print(tokenized_text)

# tokenized words
tokenized_word = word_tokenize(text)
# print(tokenized_word)

# COUNT NUMBER OF WORDS
word_list = text.split()
number_of_words = len(word_list)
print("TOTAL NUMBER OF WORDS: ", number_of_words)

# LONGEST WORD
longest = list(text.split(" "))
longest = sorted(longest, key=len)
print("THE LONGEST WORD: " + longest[-1])

# FIND MOST FREQUENT WORD
fdist = FreqDist(tokenized_word)
print("MOST COMMON WORD: ", fdist.most_common(2))
fdist.plot(30, cumulative=False)
plt.show()

# KEYWORD EXTRACTION
stop_words = set(stopwords.words('english'))
tf_score = {}
for each_word in word_list:
    each_word = each_word.replace('.', '')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

tf_score.update((x, y/int(number_of_words)) for x, y in tf_score.items())

idf_score = {}
for each_word in word_list:
    each_word = each_word.replace('.', '')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, tokenized_text)
        else:
            idf_score[each_word] = 1

idf_score.update((x, math.log(int(number_of_sentences)/y))
                 for x, y in idf_score.items())
tf_idf_score = {key: tf_score[key] *
                idf_score.get(key, 0) for key in tf_score.keys()}
# print(tf_idf_score)


def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(),
                         key=itemgetter(1), reverse=True)[:n])
    return result


print("KEYWORDS EXTRACTED: ", get_top_n(tf_idf_score, 5))

# BIGRAM EXTRACTION
bigram = ngrams(word_list, 2)
print("BIGRAMS ARE: ")
for grams in bigram:
    print(grams)

print("\n")
# TRIGRAM EXTRACTION
trigram = ngrams(word_list, 3)
print("TRIGRAMS ARE: ")
for grams in trigram:
    print(grams)

wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='blue',
                      collocations=False, stopwords=STOPWORDS).generate(text)
# text is the input to the generate() method
# draw the figure
# Set figure size
plt.figure(figsize=(40, 30))
# Display image
plt.imshow(wordcloud)
# No axis
plt.axis("off")
plt.show()
