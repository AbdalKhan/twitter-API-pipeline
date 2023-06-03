import tweepy
import configparser
import pandas as pd


def api_connect(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
   '''This function creates and returns a twitter api connection'''
   auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
   auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

   api = tweepy.API(auth)
   return api

def get_access_keys(path):
   '''This function parses config file in local/specified repository to fetch twitter API secret keys'''
   parser = configparser.ConfigParser()
   parser.read(path)
   API_KEY = parser.get("twitter_config", "api_key")
   API_SECRET_KEY = parser.get("twitter_config", "api_secret_key")
   ACCESS_TOKEN = parser.get("twitter_config", "access_token")
   ACCESS_TOKEN_SECRET = parser.get("twitter_config", "access_token_secret")
   return API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def create_dataframe(list_of_dictionaries):
   '''This function converts the tweet object attributes list into a dataframe'''
   df = pd.DataFrame(list_of_dictionaries)
   print(df.head(5))


def main():

   '''************PARAMETERS***********'''
   SECRET_KEYS_PATH = 'config.ini'
   search_query = "data engineering"  # Replace with your desired search query
   num_tweets = 100  # Specify the number of tweets to retrieve
   search_results = [] # Create a list to store the search results
   '''*********************************'''

   # API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = get_access_keys(SECRET_KEYS_PATH)
   # api = api_connect(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
   # condensed version of above

   api = api_connect(*get_access_keys(SECRET_KEYS_PATH))

   # tweets = api.user_timeline(screen_name='@elonmusk',
   #                            # 200 is maximum allowed count
   #                            count=2,
   #                            include_rts=False,
   #                            # necessary to keep full text otherwise
   #                            # only first 140 word shown
   #                            tweet_mode = 'extended')

   # for tweet in tweets:
   #    tweet_dict = tweet._json  # Convert tweet object to dictionary
   #    formatted_json = json.dumps(tweet_dict, indent=4)
   #    print(formatted_json)

   # Assuming you already have the 'api' object from the Tweepy API connection

   # Perform the search
   tweets = api.search_tweets(q=search_query, count=num_tweets)

   # Process and print the search results
   for tweet in tweets:
      username = tweet.user.screen_name
      tweet_text = tweet.text
      created_at = tweet.created_at
      location = tweet.user.location

      search_results.append({
                              "Username": username,
                              "Tweet_text": tweet_text,
                              "Created_at" : created_at,
                              "Location": location                              
                              })
      
      create_dataframe(search_results)



if __name__ == '__main__':
   main()