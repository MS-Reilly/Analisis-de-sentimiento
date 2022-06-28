import tweepy
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from classifier import SentimentClassifier
import time

username= "@esquivelgerardo"

consumer_key = "Ulvb5aFX4M4tKds71GaHRFVoZ"
consumer_secret = "ociChyAJ0LMmogd0UVDgk2gAQgiSZhHb6AAEUBbBbbUIapk05f"
access_token = "1620052802-DRJsk91JjTLY5Qd4cg7MqKkJRMyB1c2zQeihU10"
#
#
access_token_secret = "KuPadmuDDa9XfZcHNXpiDDvk8nWEMhLWBWF82CtBpgUNN"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

tweets = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name=username,tweet_mode="extended").items(3000):
    tweets.append(tweet)

df = pd.DataFrame(data=[tweet.full_text for tweet in tweets],columns=["tweets"])
df['date']=np.array([tweet.created_at for tweet in tweets])

clf = SentimentClassifier()
sentimiento = []


for tweet in df["tweets"]:
    sentimiento.append(clf.predict(tweet))

df["sentimiento"]=np.array(sentimiento)
df = df.loc[::-1]
df.to_csv(username+".csv",index=False)
