#Tweets analysis using Apache Hadoop and MapReduce
* Decided to split the task into 2 mapper reducer scripts
* used the tweets related to samsung s7, for analysis
* included the SnowBall stemmer to make more sense of the word count
* decided to use the location field of tweet instead of (latitude, longitude), due to rate limit on the Twitter API.
* Sentiment140 was not responding to my unicode query, thus used the unidecode package.
* used zipimport, to make the scripts run on a Hadoop system.
* used Hadoop streaming to run the map reduce scripts on Hadoop in pseudo distributed mode. 

##Files:
* **wordCount*.py**: mapper and reducer scripts, which will return the count for each word in the tweet's text.
Stop words removal and stemming have been applied to get a more realistic count.
* **locationSentiment*.py**: extracts the location from the tweets if location is absent or absurd sets the location to 'Unknown'. Does sentiment analysis for the tweets using Sentiment140 API. Ultimately maps the location to different sentiments observed with their relative counts.
* **sampleResult***: sample results obtained on execution of the scripts.
* ***.mod**: modules to be used by the zipimport, should be placed in the same folder as the scripts.
* **tweetsSalman.txt, samsungS7Tweets.txt, testavro**: different tweets samples for testing purposes.
