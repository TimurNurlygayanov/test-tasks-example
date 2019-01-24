#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is pretty naive and simple spell checker for Russian texts.
#
# The code was taken from this article:
#   https://habr.com/ru/company/singularis/blog/358664/
#   https://gist.github.com/Kwentar/a957d29f7370f896b691c82ff9ebe7d2
#
# Many thanks to the author of this code!
# I've modified it a little bit ofr my case.
#

import os
import gensim
from keras.preprocessing.text import text_to_word_sequence
import pymorphy2
from tqdm import tqdm


morph = pymorphy2.MorphAnalyzer()
spell_check_model_name = 'ru_spellcheck.model'
necessary_part = {"NOUN", "ADJF", "ADJS", "VERB", "INFN", "PRTF", "PRTS", "GRND"}

if not os.path.isfile(spell_check_model_name):
    all_sentences = []
    for filename in os.listdir('./education_texts'):
        if filename.endswith('.txt'):
            with open('./education_texts/{0}'.format(filename), 'r',
                      errors='ignore') as f:
                print('Parsing {0} ...'.format(filename))

                text = f.read().split('\n')
                sentences = []

                # Normalization
                for line in text:
                    sentences.append(text_to_word_sequence(line))

                for i in tqdm(range(len(sentences))):
                    sentence = []
                    for el in sentences[i]:
                        p = morph.parse(el)[0]
                        if p.tag.POS in necessary_part:
                            sentence.append(p.normal_form)
                    sentences[i] = sentence
                sentences = [x for x in sentences if x]

                all_sentences += sentences

    print(len(all_sentences))

    # --------------------------
    # Training
    model = gensim.models.FastText(all_sentences, size=300, window=3, min_count=2, sg=1, iter=35)
    model.init_sims(replace=True)

    model.save(spell_check_model_name)

else:

    # Just load model from file:
    model = gensim.models.FastText.load(spell_check_model_name)
    model.init_sims(replace=True)

    words = ['челавек',  'стулент', 'студечнеский', 'чиловенчость',
             'учавствовать', 'тактка', 'вообщем', 'симпотичный', 'зделать',  'сматреть', 'алгаритм', 'ложить']
    words_correct = ['человек', 'студент', 'студенческий', 'человечность',
                     'участвовать', 'тактика', 'вообще', 'симпатичный', 'сделать',
                     'смотреть', 'алгоритм', 'положить']

    for index, word in enumerate(words):
        if word in model:
            print(word)

            for i in model.most_similar(positive=[word], topn=20):
                print(i[0], i[1])
            print('---------------')
            print(model.similarity(word, words_correct[index]))
            print('______________\n')
