import tweepy
import pandas as pd

from tqdm import tqdm

__author__ = 'aGn'

API_KEY = "UL3Q8hMA74wRB5RykuCnCJxkm"
API_SECRET = "WJuehel0rp0wPq8T2MdULr3Hxb21DSZfZXI94oqkV6U0zz00Db"
ACCESS_TOKEN = "1970308164-GCFz3fDbgt95gs9VkbtHi0yzhTN9f8FjfbE2Ciw"
ACCESS_TOKEN_SECRET = "jZ1KL5BbHlqIEsM4qSqN2fmvu0vN4cIay2vQxy9mE6xgP"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def get_tweet(id_):
    tweet = api.get_status(id_)
    return tweet.text


def clean_data():
    df = pd.read_csv('dataset/tweetIds.csv')
    print("Shape before clean: ", df.shape)

    cleaned_df = df.dropna(how='any', axis=0)
    print("Shape after clean: ", cleaned_df.shape)

    return cleaned_df


def create_dataset():
    data = clean_data()
    progress = data.shape[0]
    pbar = tqdm(total=progress)

    with open('dataset/dataset.txt', mode='a') as file_:
        for i, row in data.iterrows():
            id_ = row.iloc[0]
            emotion_ = row.iloc[1]
            try:
                file_.write(f"{id_} {get_tweet(id_)} {emotion_}")
                file_.write("\n")
                pbar.update()
            except Exception as exp:
                print(exp)

    pbar.close()


create_dataset()  # TODO
