#Intent Classification and Analysis
- Decided to go with the naive bayes classifier approach as it known for higher accuracy in text classification.
- Learn about naive bayes, its inner working, implementation, improvements.
- Used the NLTK library's implementation of naive bayes.
- Majority of my task revolved around cleaning the tweets, formatting it, getting classified data, improving classification accuracy.

##Files:
Providing a brief intro to files, proper commenting has been done in the files for further information.
- assignIntent.py: program to hand classify random n tweets from a tweets file
- getTweets.py: this file is contained in the misc folder. Uses tweepy library to fetch tweets having the stated words.
*Usage: $ python misc/getTweets.py >> fetchedTweets*
Useful for fetching JSON formatted tweets, for testing purposes.
- intentAnalysis.py: The main program used to do the analysis.
  - Clean the tweets:
      - remove stopwords, stem similar words, web and email addresses
      - seperate test and training data in an unbiased way, while ensuring a good mix of all types of tweets to classify. 
  - train NBClassifier:
      - choose a feature set which will represents the training tweets, balancing in performance and space
      - using the feature set applied to training data, trained the naive bayes classifier
  - make classification:
      - use the trained NBClassifier to do classification on test data.
      - compute classification accuracy. *(Note: Classification accuracy will vary on each run due to random initialization)*
      - test on the given test statements:
        - Buying intent: “Where can I buy a new pair of shoes?”
        - Recommendation intent: “What is a good first-date restaurant in Delhi?”
