import sys

from setuptools import setup, find_packages
from tweet_getter import __version__


if sys.version_info[0] < 3:
    with open('README.rst') as f:
        long_description = f.read()
else:
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='tweet_getter',
    version=__version__,
    description="Get Tweets by IDs through Twitter's API",
    long_description=long_description,
    url='https://github.com/agn-7/tweet-getter',
    author='agn-7',
    author_email='benyaminjmf@gmail.com',
    license='MIT',
    packages=find_packages(),
    keywords=[
        'tweets',
        'twitter',
        'twitter-api',
        'tweepy',
        'python',
        'python-3',
        'dataset',
        'sentiment-analysis',
        'emotion-detection',
        'nlp',
        'natural-language-processing'
    ],
    download_url='https://github.com/agn-7/tweet-getter/archive/1.0.0rc2.zip',
    install_requires=[
        'tweepy',
        'pandas',
        'tqdm',
        'easydict'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
