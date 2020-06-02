# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:25:06 2020

@author: Dell
"""


import nltk
    
from nltk.tokenize import word_tokenize


text = """Harry Potter is the most miserable, lonely boy you can imagine.
He's shunned by his relatives, the Dursley's, that have raised him since he was an infant.
He's forced to live in the cupboard under the stairs, forced to wear his cousin Dudley's hand-me-down clothes, and forced to go to his neighbour's house when the rest of the family is doing something fun.
Yes, he's just about as miserable as you can get."""


def to_lower(text):
    return ' '.join([w.lower() for w in word_tokenize(text)])
print (to_lower(text))


"""Remove Numbers"""
text = "There was 200 people standing right next to me at 2pm."
output = ''.join(c for c in text if not c.isdigit())
print(output)



"""Remove punctutation"""
from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)
text = "Hello! how are you doing?"
print(strip_punctuation(text))

"""Lemmatize"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#is based on The Porter Stemming Algorithm
stopword = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()
text = 'the functions of this fan is great'
word_tokens = nltk.word_tokenize(text)
lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
print (lemmatized_word)


"""Stemming"""
from nltk.stem import SnowballStemmer
#is based on The Porter Stemming Algorithm
stopword = stopwords.words('english')
snowball_stemmer = SnowballStemmer('english')
text = 'This is a Demo Text for NLP using NLTK. Full form of NLTK is Natural Language Toolkit'
word_tokens = nltk.word_tokenize(text)
stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
print (stemmed_word)



"""Word Tokenize"""

text = 'This is a Demo Text for NLP using NLTK. Full form of NLTK is Natural Language Toolkit'
word_tokens = nltk.word_tokenize(text)
print (word_tokens)


"""Sentence Tokenize"""

text = 'This is a Demo Text for NLP using NLTK. Full form of NLTK is Natural Language Toolkit'
sent_token = nltk.sent_tokenize(text)
print (sent_token)


"""Stop Words Removal"""
stopword = stopwords.words('english')
text = 'This is a Demo Text for NLP using NLTK. Full form of NLTK is Natural Language Toolkit'
word_tokens = nltk.word_tokenize(text)
removing_stopwords = [word for word in word_tokens if word not in stopword]
print (removing_stopwords)

"""Spell check"""
from autocorrect import spell
text = "This is a wrld of hope"
spells = [spell(w) for w in (nltk.word_tokenize(text))]
print (spells)


