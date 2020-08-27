
Get Tweets by IDs through Twitter's API.
========================================

This application creates the dataset through fetching tweets by their IDs.

There are some policies to avoid tweets content directly. Thus, there are many datasets with just tweets IDs and their labels. Hence, I've prepared an application to fetch these tweets context by their IDs using Twitter API. Consequently, you need a Twitter API Token <http://apps.twitter.com>. 
https://github.com/agn-7/tweet-getter
In ``./dataset`` directory exist a dataset contains 1.3 million tweets in seven categories label (\ ``anger``\ , ``thankfulness``\ , ``joy``\ , ``sadness``\ , ``fear``\ , ``love``\ , ``surprise``\ ) by their IDs.

Installation
------------

.. code-block::

   pip install -r requirements.txt

Configuration
-------------

Customize the configuration file (\ ``./configuration/configs.py``\ )

Run
---

.. code-block:: python

   python -m tweet_getter.dataset_maker <start-row-optional> <end-row-optional>

----

[\ **NOTE**\ ]:

This package is compatible on *Python 3*

