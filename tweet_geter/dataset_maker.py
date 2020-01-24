import tweepy

__author__ = 'aGn'

API_KEY = "UL3Q8hMA74wRB5RykuCnCJxkm"
API_SECRET = "WJuehel0rp0wPq8T2MdULr3Hxb21DSZfZXI94oqkV6U0zz00Db"
ACCESS_TOKEN = "1970308164-GCFz3fDbgt95gs9VkbtHi0yzhTN9f8FjfbE2Ciw"
ACCESS_TOKEN_SECRET = "jZ1KL5BbHlqIEsM4qSqN2fmvu0vN4cIay2vQxy9mE6xgP"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweet = api.get_status(148973134249332737)  # Test by an ID.
print(tweet.text)
