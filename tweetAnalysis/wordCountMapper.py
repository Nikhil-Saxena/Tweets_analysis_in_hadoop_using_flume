#!/usr/bin/env python
import sys
import json
import re
import zipimport

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
from nltk.stem.snowball import SnowballStemmer

# Mapper code, this will map relevant words to count ONE,
# i.e, ignoring the stop words and stemming similar words
# SnowballStemmer and englishStopwords corpus are taken from nltk library
# and works for english language
#
# TODO: the lang parameter from json formatted tweet can be used to
# remove stop words of that language, as nltk has stop word
# corpus of 14 languages.
# TODO: do better error handling and unclutter the try blocks
# TODO: debug the way to use nltk corpus in hadoop

englishStopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
                    'ourselves', 'you', 'your', 'yours', 'yourself',
                    'yourselves', 'he', 'him', 'his', 'himself', 'she',
                    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they',
                    'them', 'their', 'theirs', 'themselves', 'what', 'which',
                    'who', 'whom', 'this', 'that', 'these', 'those', 'am',
                    'is', 'are', 'was', 'were', 'be', 'been', 'being',
                    'have', 'has', 'had', 'having', 'do', 'does', 'did',
                    'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
                    'because', 'as', 'until', 'while', 'of', 'at', 'by',
                    'for', 'with', 'about', 'against', 'between', 'into',
                    'through', 'during', 'before', 'after', 'above',
                    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
                    'off', 'over', 'under', 'again', 'further', 'then',
                    'once', 'here', 'there', 'when', 'where', 'why', 'how',
                    'all', 'any', 'both', 'each', 'few', 'more', 'most',
                    'other', 'some', 'such', 'no', 'nor', 'not', 'only',
                    'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
                    'can', 'will', 'just', 'don', 'should', 'now']
stemmer = SnowballStemmer('english')
for line in sys.stdin:
    try:
        tweetData = json.loads(line.decode('utf-8'))
        temp_tweetWordList = re.split(r'[\W+\d+]',tweetData['text'])
        tweetWordList = [stemmer.stem(word) for word in temp_tweetWordList]
        for word in tweetWordList:
            if word.lower() in englishStopWords:
                continue
            else:
                print '{0}\t{1}'.format(word.lower(), 1)
    except:
        continue
