
import tweepy
import emoji
import csv
import re

api = tweepy.Client(bearer_token = "AAAAAAAAAAAAAAAAAAAAAPUVfwEAAAAAmEJAxgY4WzTeX4xTwq%2FI4fW9jAU%3Dkb62OBJmHNzkkj6yBQZfugg6h62R7IWTYTzMfXrv4uhjYCDOKg")


def search_tweets(query, max_results):
    tweets = api.search_recent_tweets(query = query + " -RT", max_results = max_results)
    return tweets

tweet = search_tweets('Liverpool', 10)

results = []
sentences = []
words = []
data = []
for eachTweet in tweet.data:
  eachTweet.text = re.sub(',+', '', eachTweet.text)
  eachTweet.text = re.sub('-+', '', eachTweet.text)
  eachTweet.text = re.sub('@+','',eachTweet.text)
  eachTweet.text = re.sub('#[^\s]+', '',eachTweet.text)
  eachTweet.text = re.sub('http[^\s]+','URL',eachTweet.text)
  results.append(eachTweet.text.lower())

for result in results:
    word = result.split(' ')
    words.append(word)
    sentence = result.split('.')
    sentences.append(sentence)

for word in words:
    chars = []
    for letter in word:
        letter = emoji.demojize(letter)
        letter = re.sub('_+', " ", letter)
        chars.append(letter)
    data.append(chars)

for sentence in sentences:
    chars = []
    for letter in sentence:
       letter = emoji.demojize(letter)
       letter = re.sub('_+', " ", letter)
       chars.append(letter)
    data.append(chars)   

with open('tweets.csv', 'w', encoding ='UTF8', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

