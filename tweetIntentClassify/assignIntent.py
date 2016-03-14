#!/usr/bin/env/ python
import json
import random

# This program is used to generate classifiedTweets.json, i.e., hand
# classifying tweets for a supervised machine learning training set.
# Twitter returned data from getTweets.py has \n in every second line,
# thus random no. generated is always taken to be multiple of 2.
#
# It runs till classifyNtweets is met. The selection of tweets is
# unbiased. User is expected to enter
# 'r': recommend
# 'p': purchase
# 'n': neutral/none
# 'q': ignore this tweet and move on

classifyNtweets = 25
tweetsFile = open('tweetsForIntentAnalysis','r')
ftw = open('classifiedTweets.json','w')
tweetsList = list(tweetsFile)
tweetsData = {}
count = 0
while count < classifyNtweets:
    index = random.randrange(0,len(tweetsList),2)
    try:
        tweet = json.loads(tweetsList[index])
        print tweet['text'] + '\n'
        intent = input('tweet intent?')
        while input not in ['r', 'p', 'n', 'q']:
            intent = input('invalid input, try again: ')
        tweetsData['text'] = tweet['text']
        tweetsData['intent'] = intent
        tweetsList.pop(index)
        if intent is not 'q':
            json.dump(tweetsData, ftw)
            ftw.write('\n')
            count += 1
    except:
        continue
ftw.close()
tweetsFile.close()
