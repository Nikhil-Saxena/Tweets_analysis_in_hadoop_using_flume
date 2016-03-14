#!/usr/bin/env python
import sys
import json
import re
import urllib
import urllib2
import zipimport

importer = zipimport.zipimporter('unidecode.mod')
unidecode = importer.load_module('unidecode')
from unidecode import unidecode
from urllib2 import URLError, HTTPError

# Mapper code, it maps the tweets from a location to its sentiment.
# Possibly determining the satisfaction level of persons in a paricular
# region corresponding to given keywords in the tweets
# Streaming140 API is used for sentiment analysis of tweets.
# Location taken from the location field of the json formated tweet.
# sentiment140 doesn't handle unicode thus unidecode is used.

def main():
    URL_SENTIMENT140 = 'http://www.sentiment140.com/api/bulkClassifyJson?appid=saxena.nik2@gmail.com'
    tweets = []
    for line in sys.stdin:
        try:
            tweetData = json.loads(line.decode('utf-8'))
            location = tweetData['user']['location'].strip()
            if location is None or bool(re.search(r'\d',location)):
                location = 'unknown'
            tempDataDict = {'text': unidecode(tweetData['text']), 'location':\
            unidecode(location.upper())}
            tweets.append(tempDataDict)
        except:
            continue
    dataToSend = {'data': tweets}
    try:
        response = urllib2.urlopen(URL_SENTIMENT140, str(dataToSend))
        sentimentJsonResponse = json.loads(response.read())
        parsedDataDict = parseResponse(sentimentJsonResponse)
        for key, value in parsedDataDict.items():
            print "{0}\t{1}".format(key, value)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    except:
        print 'response from server is null or some error has occured'

def parseResponse(sentimentJsonResponse):
    returnData = {}
    sentiment = None
    for j in sentimentJsonResponse['data']:
        if int(j['polarity']) == 0:
            sentiment = 'negative'
        elif int(j['polarity']) == 4:
            sentiment = 'positive'
        elif int(j['polarity']) == 2:
            sentiment = 'neutral'
        if (j['location'], sentiment) in returnData:
            returnData[j['location'],sentiment] += 1
        else:
            returnData[j['location'],sentiment] = 1
    return returnData

if __name__ == '__main__':
    main()
