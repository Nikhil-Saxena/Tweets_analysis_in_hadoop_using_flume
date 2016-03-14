#!/usr/bin/env python
import sys
import json
import re

# Reducer code, it reduces the counts of various sentiment for each location
# it expects the input of form:
# ('location_0', 'sentiment') 2
# ('location_0', 'sentiment') 1
# ('location_1', 'sentiment') 12
# and so on, where sentiment may be 'positive', 'negative', 'neutral'
#
# TODO: count 'Banglore', 'banglore, india', 'banglore, karnataka',
# 'Bengaluru', 'Bengaluru, india', 'Bengaluru, karnataka'.
# The first test case looks trivial, include only the city/ country name,
# but (city, country) name is required to recognise a place correctly.
# so it depends on the use case. Workout the second case.

totalCount = 0
oldLocationSentiment = None
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    locationSentiment, count = data
    try:
        count = int(count)
    except:
        continue
    if oldLocationSentiment and oldLocationSentiment != locationSentiment:
        print '{0}\t{1}'.format(oldLocationSentiment, totalCount)
        totalCount = 0
    oldLocationSentiment = locationSentiment
    totalCount += count
if oldLocationSentiment is not None:
    print '{0}\t{1}'.format(oldLocationSentiment, totalCount)
