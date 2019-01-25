#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is pretty naive and simple spell checker for Russian texts.
#
# The code was taken from this article:
#   https://habr.com/ru/company/singularis/blog/358664/
#   https://gist.github.com/Kwentar/a957d29f7370f896b691c82ff9ebe7d2
#
# Many thanks to the author of this code!
# I've modified it a little bit for my case:
#   1) Education now based on Russian words dictionary instead of some
#      Russian text.
#   2) Increased the size of the model
#   3) Removed unnecessary Keras dependency.
#

import os
import requests
from termcolor import colored

import gensim
import pymorphy2
from tqdm import tqdm


spell_check_model_name = 'ru_spellcheck.model'
necessary_part = {'NOUN', 'ADJF', 'ADJS', 'VERB', 'INFN',
                  'PRTF', 'PRTS', 'GRND'}

# Wrong Russian words to check the model:
wrong_words = ['челавек',  'стулент', 'студечнеский', 'чиловенчость',
               'учавствовать', 'тактка', 'вообщем', 'симпотичный', 'зделать',
               'сматреть', 'алгаритм', 'ложить', 'проверка']
# Correct words:
words_correct = ['человек', 'студент', 'студенческий', 'человечность',
                 'участвовать', 'тактика', 'вообще', 'симпатичный', 'сделать',
                 'смотреть', 'алгоритм', 'положить', 'проверка']

# Download Russian dictionary:
russian_words_link = ('https://raw.githubusercontent.com/danakt/'
                      'russian-words/master/russian.txt')
res = requests.get(russian_words_link)
res.encoding = 'windows-1251'
words_for_eduction = res.text

# Prepare dictionary words for eduction:
# Note: here we use only first 100000 words, but
# for real cases we need to use the whole list of words!
sentences = words_for_eduction.split('\n')[:10000] + words_correct
all_dict = sentences

if not os.path.isfile(spell_check_model_name):

    morph = pymorphy2.MorphAnalyzer()

    for i in tqdm(range(len(sentences))):

        word = sentences[i]
        sentence = []

        p = morph.parse(word)[0]
        if p.tag.POS in necessary_part:
            sentence.append(p.normal_form)

        sentences[i] = sentence
    sentences = [x for x in sentences if x]

    # Training the model (it can take 2+ hours!):
    model = gensim.models.FastText(sentences, size=300,
                                   window=1, min_count=1, sg=1, iter=100,
                                   min_n=1, max_n=6)
    model.init_sims(replace=True)

    # Save model to the disk (it will take 200+ Mb on disk!)
    print('Saving model to the disk...')
    model.save(spell_check_model_name)

    print('Neuron network model is ready!')

else:
    # Load model from file:
    model = gensim.models.FastText.load(spell_check_model_name)
    model.init_sims(replace=True)


spell_checker = model.wv

# Check what options model will suggest to correct each wrong word:
for index, word in enumerate(wrong_words):

    if word in all_dict:
        print('\n ---- \n\n ', colored(word, 'green'))
        print('The word is correct!')
    else:
        print('\n ---- \n\n ', colored(word, 'red'))

        print('Suggested options:')
        for i in spell_checker.most_similar(positive=[word])[:5]:
            print(colored(i[0], 'yellow'), i[1])

print('\n ---- \n\n ')
