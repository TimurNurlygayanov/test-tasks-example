#!/usr/bin/python3
# -*- encoding=utf8 -*-

import nltk
import os.path
from telethon.sync import TelegramClient
from configparser import ConfigParser


config = ConfigParser()
config.read('/Users/timurnurlygayanov/.config.ini')


def get_conf_param(parameter, default_value):
    result = config.get('DEFAULT', parameter)
    return result or default_value


# Read all parameters from config file:
name = get_conf_param('name', '')
api_id = get_conf_param('api_id', '')
api_hash = get_conf_param('api_hash', '')
chat = get_conf_param('chat', '')


ALL_MESSAGES = []
ALL_QUESTIONS = []

filename = 'questions.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        ALL_QUESTIONS = f.readlines()
    ALL_QUESTIONS = [q[:-2] for q in ALL_QUESTIONS]
else:
    with TelegramClient(name, api_id, api_hash) as client:
        for message in client.iter_messages(chat):
            if message.text:
                ALL_MESSAGES.append(str(message.text))

    for q in ALL_MESSAGES:
        msg = q.replace('.', '\n').replace('(', '\n').replace(')', '\n')
        msgs = msg.replace('"', '\n').lower().split('\n')

        for m in msgs:
            if '?' in str(m) and len(m) > 5:
                ALL_QUESTIONS.append(m)

    with open(filename, 'w') as f:
        f.write('\n'.join(ALL_QUESTIONS))


for q in ALL_QUESTIONS:
    print(q + "\n====\n")


print('Total messages: {0}'.format(len(ALL_MESSAGES)))
print('Questions found: {0}'.format(len(ALL_QUESTIONS)))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


stop_words = nltk.corpus.stopwords.words('russian')

vectorizer = TfidfVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(ALL_QUESTIONS)

model = KMeans(n_clusters=2, init='k-means++', max_iter=100, n_init=1)
model.fit(X)


print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()


print(terms)


for i in range(2):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()
