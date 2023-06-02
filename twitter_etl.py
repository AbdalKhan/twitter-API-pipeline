import tweepy

auth = tweepy.OAuth1UserHandler(
   "API / Consumer Key here", "API / Consumer Secret here",
   "Access Token here", "Access Token Secret here"
)
api = tweepy.API(auth)

