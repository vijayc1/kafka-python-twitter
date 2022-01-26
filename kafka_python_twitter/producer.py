import tweepy
from json import dumps
from kafka import KafkaProducer

"""
Setup a twitter developer account and generate the token
"""

client = tweepy.Client(bearer_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
topic_name = 'SuriyaTweet'

# Replace with your own search query
query = 'suriya -is:retweet'
# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    data = {'tweet' : tweet.text}
    producer.send(topic_name, value=data)