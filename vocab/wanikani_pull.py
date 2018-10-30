'''
Grab a word from wanikani cache
'''

import json
import pickle
import random

cache = pickle.load(open('wanikanicache.pkl', 'rb'))

data = cache.text

src = json.loads(data)

from pprint import pprint

#pprint(src)

# Desired Kanji is in data[N][data['slug']
# Adj/Verb/Noun in data[N][data['parts_of_speech']


def _grab_noun():
    '''
    Randomly picks a noun from wanikani's vocab
    :return: noun
    '''
    word = random.choice(src['data'])
    #pprint(word)
    while 'noun' not in word['data']['parts_of_speech']:
        word = random.choice(src['data'])
        #pprint(word)
    return word['data']['slug']

def _grab_word(partofspeech):
    '''
    Randomly picks a word from wanikani's extensive vocab, If partofspeech matches (ie verb, noun, etc),
    then it returns
    :param partofspeech: ichidan_vorb, na_adjective, i_adjective, etc.
    :return:
    '''
    word = random.choice(src['data'])
    pprint(word)
    while partofspeech not in word['data']['parts_of_speech']:
        word = random.choice(src['data'])
        pprint(word)
    return word['data']['slug']

no = _grab_noun()
print(no)
v = _grab_word('i_adjective')
print(v)
n = _grab_word('noun')
print(n)