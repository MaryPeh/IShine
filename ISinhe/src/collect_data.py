import tweepy
import pandas as pd

api_key = "SUA_API_KEY"
api_secret = "SUA_API_SECRET"
access_token = "SEU_ACCESS_TOKEN"
access_secret = "SEU_ACCESS_SECRET"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

query = "depressão OR ansiedade OR felicidade -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="pt").items(500)

data = [{"tweet": tweet.text, "data": tweet.created_at} for tweet in tweets]
df = pd.DataFrame(data)
df.to_csv("../data/tweets_saude_mental.csv", index=False)
print("Coleta de dados concluída!")
