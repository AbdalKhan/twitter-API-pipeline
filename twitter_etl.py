import tweepy
import configparser

auth = tweepy.OAuth1UserHandler(
   "API / Consumer Key here", "API / Consumer Secret here",
   "Access Token here", "Access Token Secret here"
)
api = tweepy.API(auth)



parser = configparser.ConfigParser()
parser.read('config.ini')

SECRET = parser.get("reddit_config", "secret")
CLIENT_ID = parser.get("reddit_config", "client_id")
