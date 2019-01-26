#!/usr/bin/python3
# -*- encoding=utf8 -*-

#
# This code based on the information from this article:
# http://brandonrose.org/clustering
#
# Many thanks to the author of this great article!!!
#

import nltk
import os.path
from telethon.sync import TelegramClient
from configparser import ConfigParser

import numpy as np
import pandas as pd
import re
import codecs
from sklearn import feature_extraction
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib

import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.manifold import MDS


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
    ALL_QUESTIONS = [q for q in ALL_QUESTIONS]
else:
    with TelegramClient(name, api_id, api_hash) as client:
        for message in client.iter_messages(chat):
            if message.text:
                ALL_MESSAGES.append(str(message.text))

    for q in ALL_MESSAGES:
        msg = q.replace('.', '\n').replace('(', '\n').replace(')', '\n')
        msgs = msg.replace('"', '\n').lower().split('\n')

        for m in msgs:
            if len(m) > 5:
                if '?' in str(m):
                    ALL_QUESTIONS.append(m)

    with open(filename, 'w') as f:
        f.write('\n'.join(ALL_QUESTIONS))


for q in ALL_QUESTIONS:
    print(q + "\n====\n")


print('Total messages: {0}'.format(len(ALL_MESSAGES)))
print('Questions found: {0}'.format(len(ALL_QUESTIONS)))


titles = ALL_QUESTIONS
synopses = ALL_QUESTIONS

stop_words = nltk.corpus.stopwords.words('russian')
stemmer = SnowballStemmer('russian')


# Additional stop words:
stop_words += ['бол', 'больш', 'будт', 'быт', 'вед', 'впроч', 'всег', 'всегд',
               'даж', 'друг', 'е', 'ег', 'ем', 'есл', 'ест', 'ещ', 'зач', 'зде',
               'ил', 'иногд', 'когд', 'конечн', 'куд', 'лучш', 'межд', 'мен', 'мног',
               'мо', 'можн', 'нег', 'нельз', 'нибуд', 'никогд', 'нич', 'опя', 'посл',
               'пот', 'почт', 'разв', 'сво', 'себ', 'совс', 'теб', 'тепер', 'тог',
               'тогд', 'тож', 'тольк', 'хорош', 'хот', 'чег', 'чут', 'эт', 'оп', 'а']


def tokenize_only(text):
    # First tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # Filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[А-Яа-яЁё]', token):
            filtered_tokens.append(token)
    return filtered_tokens


def tokenize_and_stem(text):
    filtered_tokens = tokenize_only(text)

    stems = [stemmer.stem(t) for t in filtered_tokens]

    return stems


totalvocab_stemmed = []
totalvocab_tokenized = []
for i in synopses:
    allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list

    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)


vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')


# Define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, max_features=200000,
                                   min_df=0.01, stop_words=stop_words,
                                   use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)  # Fit the vectorizer to synopses

terms = tfidf_vectorizer.get_feature_names()

dist = 1 - cosine_similarity(tfidf_matrix)


num_clusters = 5
int_previous = 100
smallest = 100

"""
for num_clusters in range(4, 5):

    km = KMeans(n_clusters=num_clusters)

    km.fit(tfidf_matrix)

    interia = km.inertia_
    print("k: ", num_clusters, " cost: ", interia, '  ', (int_previous-interia)/interia)

    if (int_previous-interia)/interia > 0.0 and smallest > (int_previous-interia)/interia:
        smallest = (int_previous-interia)/interia

    int_previous = interia

print(smallest)
"""

km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)


# Dump the model:
# joblib.dump(km,  'doc_cluster.pkl')
# km = joblib.load('doc_cluster.pkl')
# clusters = km.labels_.tolist()


predict_me = tfidf_vectorizer.transform(['Какой провайдер лучше?'])
print(km.predict(predict_me))

predicted_class = km.predict(predict_me)


print('Similar questions:')
for i in ALL_QUESTIONS:
    predict_me = tfidf_vectorizer.transform([i])
    if km.predict(predict_me) == predicted_class:
        print(i + '\n=====\n\n')



"""  For grouping and calculations:
films = { 'title': titles, 'synopsis': synopses, 'cluster': clusters }

frame = pd.DataFrame(films, index = [clusters] , columns = ['title', 'cluster'])

print( frame['cluster'].value_counts() )


print("Top terms per cluster:")
print()
# sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1]

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')

    for ind in order_centroids[i, :6]:  # replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0], end=',')
    print()  # add whitespace
    print()  # add whitespace

    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print()  # add whitespace
    print()  # add whitespace
    print()


MDS()

# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]


# create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles))

# group by cluster
groups = df.groupby('label')

for g in groups:
    print(g)
"""

clusters = km.labels_.tolist()


MDS()

# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]


#set up colors per clusters using a dict
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}

#set up cluster names using a dict
cluster_names = {0: 'Family, home, war',
                 1: 'Police, killed, murders',
                 2: 'Father, New York, brothers',
                 3: 'Dance, singing, love',
                 4: 'Killed, soldiers, captain'}


# create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles))

# group by cluster
groups = df.groupby('label')

# set up plot
fig, ax = plt.subplots(figsize=(17, 9))  # set size
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling

# iterate through groups to layer the plot
# note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12,
            label=cluster_names[name], color=cluster_colors[name],
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params( \
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params( \
        axis='y',  # changes apply to the y-axis
        which='both',  # both major and minor ticks are affected
        left='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelleft='off')

ax.legend(numpoints=1)  # show legend with only 1 point

# add label in x,y position with the label as the film title
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)

plt.show()  # show the plot
