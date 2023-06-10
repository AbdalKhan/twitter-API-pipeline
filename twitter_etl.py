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
   return pd.DataFrame(list_of_dictionaries)

def load_to_csv(extracted_df):
   """Save extracted data to CSV file in /tmp folder"""
   
   extracted_df.to_csv('tmp/output.csv', index=False)
   
    
def main():

   '''************PARAMETERS***********'''
   SECRET_KEYS_PATH = 'config.ini'
   search_query = "data engineering"  # Replace with your desired search query
   num_tweets = 100  # Specify the number of tweets to retrieve (maximum of 100)
   search_results = [] # Create a list to store the search results
   '''*********************************'''

   api = api_connect(*get_access_keys(SECRET_KEYS_PATH))

   # Perform the search only against a sampling of recent Tweets published in the past 7 days
   tweets = api.search_tweets(q=search_query, count=num_tweets)

   # Process and print the search results
   for tweet in tweets:
      username = tweet.user.screen_name
      # tweet_text = tweet.text
      created_at = tweet.created_at
      location = tweet.user.location

      search_results.append({
                              "Username": username,
                              "Created_at" : created_at,
                              "Location": location                              
                              })
      
      extracted_df = create_dataframe(search_results)

      load_to_csv(extracted_df)
      
if __name__ == '__main__':
   main()
