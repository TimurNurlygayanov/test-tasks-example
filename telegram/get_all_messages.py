#!/usr/bin/python3
# -*- encoding=utf8 -*-

import re
import nltk
from telethon.sync import TelegramClient


ALL_MESSAGES = []
ALL_QUESTIONS = []

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

# ALL_QUESTIONS = [q for q in ALL_MESSAGES if '?' in q]

for q in ALL_QUESTIONS:
    print(q + "\n====\n")


print('Total messages: {0}'.format(len(ALL_MESSAGES)))
print('Questions found: {0}'.format(len(ALL_QUESTIONS)))


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

"""
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(ALL_QUESTIONS[:10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

res = text_clf.predict(['текст номер три'])
print(ALL_QUESTIONS[:10])
print(res)
"""

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
