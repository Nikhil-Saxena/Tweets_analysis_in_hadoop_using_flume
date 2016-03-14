#!/usr/bin/env python
import sys

# Reducer code, which expects input from mapper in form
# word_1 1
# word_1 1
# word_2 1
# and so on, reducer will print for each word its wordCount

wordCount = 0
oldWord = None
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    thisWord, count = data
    try:
        count = int(count)
    except:
        continue
    if oldWord and oldWord != thisWord:
        print '{0}\t{1}'.format(oldWord, wordCount)
        wordCount = 0
    oldWord = thisWord
    wordCount += count
if oldWord is not None:
    print '{0}\t{1}'.format(oldWord, wordCount)
