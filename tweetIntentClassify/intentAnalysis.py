#!/usr/bin/env python
import json
import random
import re
import zipimport

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
from nltk.stem.snowball import SnowballStemmer

# Intent classification and analysis is done on classifiedTweets.json file.
# classifiedTweets.json contains a set of pre-classified tweets.
# A naive bayes classifier is trained to classify tweets into intent of
# purchase, recommendation and neutral/ none.

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
stemmer = SnowballStemmer("english")
recommendTweets = []
purchaseTweets = []
neutralTweets = []
trainingTweets = []
testTweets = []
trainingTweetsWords = []
wordFeatures = []

# Function to initialize various declared lists, purchase and recommend lists
# are used so as to get a good mix in the training and test set.
# The classifiedTweets.json has an intent parameter associated with each tweet.
# r: recommended, p: purchase, n: neutral/ none
# Stemming is done to improve classification accuracy.
def initializeLists():
    tweetsData = open('classifiedTweets.json','r')
    tweetsList = list(tweetsData)
    for line in tweetsList:
        tweet = json.loads(line)
        tweet['text'] = applyStemmerToTweet(tweet['text'])
        if tweet['intent'] == 'r':
            recommendTweets.append((tweet['text'],tweet['intent']))
        elif tweet['intent'] == 'p':
            purchaseTweets.append((tweet['text'],tweet['intent']))
        elif tweet['intent'] == 'n':
            neutralTweets.append((tweet['text'],tweet['intent']))
    tweetsData.close()
    print 'lenght of recommendTweets: ' + str(len(recommendTweets))
    print 'lenght of purchaseTweets: ' + str(len(purchaseTweets))
    print 'lenght of neutralTweets: ' + str(len(neutralTweets))

# Function to split training and test sets, it ensures a balanced and
# unbiased distribution of each type of tweet. 
# This will increase classification accuracy.
def seperateTestTraining(noOfTweetsOfAType):
    count = 0
    while count <= noOfTweetsOfAType:
        index = random.randrange(len(recommendTweets))
        trainingTweets.append(recommendTweets[index])
        recommendTweets.pop(index)
        count += 1
    count = 0
    while count <= noOfTweetsOfAType:
        index = random.randrange(len(purchaseTweets))
        trainingTweets.append(purchaseTweets[index])
        purchaseTweets.pop(index)
        count += 1
    count = 0
    while count <= noOfTweetsOfAType:
        index = random.randrange(len(neutralTweets))
        trainingTweets.append(neutralTweets[index])
        neutralTweets.pop(index)
        count += 1
    testTweets.extend(recommendTweets + purchaseTweets + neutralTweets)

# Classifier function to make a feature list (wordFeatures list) of size =
# noOfFeatures from the most frequent occuring words in trainingTweetsWords.
def classifier(noOfFeatures):
    allWords = []
    for (words,sentiment) in trainingTweetsWords:
        allWords.extend(words)
    wordList = nltk.FreqDist(allWords)
    wordList = sorted(wordList.iteritems(), key=lambda(k,v):(v,k), reverse=True)
    wordList = [word for (word, freq) in wordList]
    for word in wordList:
        if word in englishStopWords:
            wordList.remove(word)
        elif re.search(r'http[\w:]+', word):
            wordList.remove(word)
        elif re.search(r'[\w:?]*@\w*', word):
            wordList.remove(word)
        elif re.search(r'\\u[\w:@.]*', word):
            wordList.remove(word)
    print 'lenght of wordList: ' + str(len(wordList))
    print 'lenght of wordFeatures: ' + str(noOfFeatures)
    return wordList[:noOfFeatures]

# Function to extract (words, intent) from a list of classified tweets
# eg: [(['recommend', 'me', ...], 'r'), (['hello', 'buy', ...], 'p'), ...]
def extractWords(appendTo,fromTweets):
    for (words, intent) in fromTweets:
        wordsFiltered = [word.lower() for word in words.split()]
        appendTo.append((wordsFiltered, intent))

# Function to extract the features(which are used in the Naive Bayes Classifier)
# from the tweetWords list. Casting to set is done to remove duplicate words.
# wordFeatures is the feature list of words that are used for classification.
def extractFeatures(tweetWords):
    tweetWords = set(tweetWords)
    features = {}
    for word in wordFeatures:
        features['contains(%s)' %word] = (word in tweetWords)
    return features

def applyStemmerToTweet(tweet):
    return ' '.join([stemmer.stem(word) for word in tweet.split()])

def main():
    noOfTweetsOfAType = 15
    noOfFeatures = 167
    initializeLists()
    seperateTestTraining(noOfTweetsOfAType)
    # trainingTweetsWords, wordFeatures are initialized here
    extractWords(trainingTweetsWords, trainingTweets)
    wordFeatures.extend(classifier(noOfFeatures))
    trainingSet = nltk.classify.apply_features(extractFeatures,
                                               trainingTweetsWords)
    NBClassifier = nltk.NaiveBayesClassifier.train(trainingSet)
    # Checking classification accuracy
    count = 0
    for (tweetText, intent) in testTweets:
        prediction = NBClassifier.classify(extractFeatures(tweetText.split()))
        if prediction == intent:
            count += 1
    printMsg = '---Accuracy with %d tweets of each type = '
    print printMsg %noOfTweetsOfAType + str(count/float(len(testTweets)))
    print '---Accuracy varies with each run due to random initialization'    
    samplePurchaseTweet = 'Where can I buy a new pair of shoes?'
    sampleRecommendTweet = 'What is a good first-date restaurant in Delhi?'
    print 'Tweet: ' + samplePurchaseTweet + '\nPrediction:'
    print NBClassifier.classify(extractFeatures(samplePurchaseTweet.split()))
    print 'Tweet: ' + sampleRecommendTweet + '\nPrediction:'
    print NBClassifier.classify(extractFeatures(sampleRecommendTweet.split()))


if __name__ == '__main__':
    main()
