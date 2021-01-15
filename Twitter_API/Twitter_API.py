import tweepy
import json


file = open("keys.txt","r")
dict_keys = {}
elem = []
for line in file:
    elem = line.split("=")
    dict_keys[elem[0]] = elem[1].rstrip('\n')
auth = tweepy.OAuthHandler(dict_keys.get("consumer_key"),dict_keys.get("consumer_secret"))
auth.set_access_token(dict_keys.get("Access_token"),dict_keys.get("Access_token_secret"))

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) # Si llega al limite de cupo, el programa no va a crashear sino que espera a que haya cupo otra vez

file_tweets = open("tweets.txt","a")

for tweet in tweepy.Cursor(api.search,q="Petro",tweet_mode ="extended").items(1):
    #data = json.dumps(tweet._json,indent = 2)
    data = tweet._json["retweeted_status"]
    data = data["full_text"]
    file_tweets.write(data+"|")
file_tweets.close