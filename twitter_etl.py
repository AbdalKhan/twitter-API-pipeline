import tweepy
import configparser
import json


def api_connect(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
   auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
   auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

   api = tweepy.API(auth)
   return api

def get_access_keys(path):
   # parse config file to get twitter API secret keys
   parser = configparser.ConfigParser()
   parser.read(path)
   API_KEY = parser.get("twitter_config", "api_key")
   API_SECRET_KEY = parser.get("twitter_config", "api_secret_key")
   ACCESS_TOKEN = parser.get("twitter_config", "access_token")
   ACCESS_TOKEN_SECRET = parser.get("twitter_config", "access_token_secret")
   return API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET



def main():
   # parse config file to get twitter API secret keys
   
   '''************PARAMETERS***********'''
   SECRET_KEYS_PATH = 'config.ini'
   '''*********************************'''
   
   # API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = get_access_keys(SECRET_KEYS_PATH)
   # api = api_connect(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
   # condensed version of above

   api = api_connect(*get_access_keys('config.ini'))

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



if __name__ == '__main__':
   main()