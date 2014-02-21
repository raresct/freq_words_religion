#!/usr/bin/python

import numpy as np

from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn

from pytagcloud import create_tag_image, make_tags

import file_wrapper

def can_be_noun(test_word):
    synsets = wn.synsets(test_word)
    if len(synsets) == 0:
        return True
    for s in synsets:
        if s.pos == 'n':
            return True
    return False


def main():
    stop_words = sw.words()
    word_limit = 50
    freqs = []
    with file_wrapper.File('output/part-00000') as f:
        for line in f.backward():
            line = line.strip()
            count, word = line.split('\t', 1)
            count = int(count)
            if word not in stop_words and len(word)>2 and can_be_noun(word):
                freqs.append((word, count))
            if len(freqs)>word_limit:
                break
    sum_freqs = np.sum(x for _,x in freqs)
    freqs = [(w, np.float(f)/sum_freqs) for w,f in freqs]
    tags = make_tags(freqs, maxsize=80)
    fname = 'freq_words_religion.png'
    create_tag_image(tags, fname, size=(900, 600), fontname='Lobster')        

if __name__=="__main__":
    main()

