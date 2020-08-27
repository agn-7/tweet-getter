import tweepy
import pandas as pd
import sys
import os

from tqdm import tqdm
from configuration.configs import DATA_PREPARATION
from easydict import EasyDict as edict
from time import sleep

__author__ = 'aGn'

params = edict(DATA_PREPARATION)
API_KEY = params.api_key
API_SECRET = params.api_secret
ACCESS_TOKEN = params.access_token
ACCESS_TOKEN_SECRET = params.access_token_secret


def get_tweet(id_):
    """
    Get tweet through its ID using tweepy library.
    :param id_: tweet's ID.
    :return: tweet text.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweet = api.get_status(id_)
    tweet_text = remove_symbol(tweet.text, '#')

    return tweet_text


def remove_symbol(text, *symbols):
    """
    Remove entered symbols from text.
    :param text: Text
    :param symbols: forbidden symbols.
    :return: Text without entered symbols.
    """
    entity_prefixes = symbols
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)


def clean_data(start=None, end=None):
    """
    Read raw data and clean it.
    :param start: Start point of row.
    :param end: End point of row.
    :return: cleaned data.
    """
    df = pd.read_csv('dataset/tweetIds.csv')

    if start is not None:
        if end is not None and end != 'end':
            df = df.iloc[start:end, :]
        else:
            '''Start to the End of file'''
            df = df.iloc[start:, :]

    print("Shape before clean: ", df.shape)
    cleaned_df = df.dropna(how='any', axis=0)
    print("Shape after clean: ", cleaned_df.shape)

    return cleaned_df


def prepare_dataset(*args, **kwargs):
    """
    Preparing dataset through getting tweets per IDs and apply hashtag remover pre-process on it.
    :return:
    """
    chunked_start = kwargs.get('chunked_start', None)
    chunked_end = kwargs.get('chunked_end', None)
    print(f"Start from {chunked_start} to {chunked_end}")

    '''Generating Postfix.'''
    _start, _end = 0, 'end'
    if chunked_start is not None:
        _start = chunked_start
    if chunked_end is not None:
        _end = chunked_end

    data = clean_data(chunked_start, chunked_end)
    progress = data.shape[0]
    progress_bar = tqdm(total=progress)
    missing_tweets = 0

    with open(f'dataset/dataset_{_start}_to_{_end}.txt', mode='a') as file_:
        for i, row in data.iterrows():
            id_ = row.iloc[0]
            emotion_ = row.iloc[1]
            try:
                file_.write(f"{id_} {get_tweet(id_)} {emotion_}")
                file_.write("\n")
                progress_bar.update()
            except KeyboardInterrupt:
                sys.exit(0)
            # except tweepy.error.TweepError as exc:  # TODO :: Not yet tested.
            #     print(exc)
            #     missing_tweets -=- 1
            #     progress_bar.update()
            #     # Do some stuff to count missing tweets and managing progress bar here. # TODO
            except Exception as exp:
                print(exp)
                missing_tweets -=- 1  # TODO

    print(f"We missed {missing_tweets} of tweets.")
    progress_bar.close()


def run():  # TODO :: add argparse
    if len(sys.argv) == 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    else:
        start = int(params.chunked_start)
        end = int(params.chunked_end)

    prepare_dataset(chunked_start=start, chunked_end=end)

    if params.auto_poweroff:
        print('Auto Shut Down ...')
        sleep(10)
        if os.name == 'nt':
            '''Windows'''
            os.system("shutdown /s /t 1")
        elif os.name == 'posix':
            '''*nix'''
            os.system("shutdown now -h")
        else:
            os.system("shutdown now -h")


if __name__ == '__main__':
    run()
