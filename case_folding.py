#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import string
import re


# In[ ]:


def load_data():
    data = pd.read_csv(open('DatasetbaruID(1).csv', 'rU'),skiprows=1,names=['TweetID','Tweet_Author','Tweet_Reply'], engine='python')
    return data

tweet_df = load_data()
tweet_df.head(3)


# In[ ]:


df = pd.DataFrame(tweet_df[['TweetID', 'Tweet_Author', 'Tweet_Reply']])


# In[ ]:


df = df.applymap(str)


# In[ ]:


pd.set_option('display.max_colwidth', 100)


# In[ ]:


def normalize(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r'-', ' ', tweet)
    tweet = re.sub('[0-9]+', '', tweet)
    tweet = re.sub('\W+',' ', tweet)
    tweet = tweet.lower()
    tweet = ''.join(["" if ord(i) < 32 or ord(i) > 126 else i for i in tweet])
    tweet = re.sub('\s+', ' ', tweet)
    tweet = tweet.strip()
    tweet = re.sub(r'_', ' ', tweet)
    
    return tweet

df = df[['Tweet_Author', 'Tweet_Reply']].applymap(lambda x: normalize(x))

df


# In[ ]:


df.to_csv('TweetBaru_clean_Final2.csv', index = False, header=True)


# In[ ]:




