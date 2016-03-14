#**Tweets_analysis_in_hadoop_using_flume**

#####Part 1 : Setting up Apache Hadoop and Apache Flume to ingest tweets in real time.
            - Installed hadoop and flume 
            - made changes to various configuration files of hadoop
            - registered an app on twiter to use its API
            - made source and sink configuration changes in Flume 
            - the changed files with their locations are included
            
#####Part 2: Analyse the tweets
     Implemented mapper and reducer scripts for:
     1. word count, stemming, stopword removal
            The word count makes more sense if we remove the stopwords and stem the similar ones. Driven by this logic I clubbed word count, stemming, stopword removal into a single mapper.
            
     2. location extraction and sentiment analysis using the Sentiment140 API
            I wanted to make use of the location to derive some intuition or understanding about the tweets. The mapper file include will extract the (location, text) from the tweets and send it to Sentiment140 API for sentiment analysis. This made it possible to associate sentiments to a location regarding the product/ event which form keywords in the tweets. The output from the reducer is: (location, sentiment) countOfTweets.
            
Problems to solve: 
            - The script will work fine given json text as input, they have been tested on the linux system, Apache Hadoop in pseudo-distributed mode. But they fail on avro formatted input (the format which Apache Flume uses to store data in HDFS).
I figured out the solution which is provided by hadoop itself, i.e., to append "-inputformat org.apache.avro.mapred.AvroAsTextInputFormat" hadoop streaming statement and incude the various jar file. This would convert avro to json as required and feed the same to the mapper. But it didn't workout.
            - I was forced to enter the stopword list into the mapper, after numerous attempts of including the NLTK corpus into the hadoop system had failed.

#####Part 3: Tweet Intent classification
     I decided to go with the Naive Bayes Classifier and coded a program which will:
            - clean the tweets
            - train the classifier 
            - make classification
