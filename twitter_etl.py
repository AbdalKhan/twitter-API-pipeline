import tweepy
import configparser
import json

# parse config file to get twitter API secret keys
parser = configparser.ConfigParser()
parser.read('config.ini')

API_KEY = parser.get("twitter_config", "api_key")
API_SECRET_KEY = parser.get("twitter_config", "api_secret_key")
ACCESS_TOKEN = parser.get("twitter_config", "access_token")
ACCESS_TOKEN_SECRET = parser.get("twitter_config", "access_token_secret")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           # 200 is maximum allowed count
                           count=2,
                           include_rts=False,
                           # necessary to keep full text otherwise
                           # only first 140 word shown
                           tweet_mode = 'extended')

for tweet in tweets:
    tweet_dict = tweet._json  # Convert tweet object to dictionary
    formatted_json = json.dumps(tweet_dict, indent=4)
    print(formatted_json)
    print(tweet.id)
    print(tweet_dict['id'])