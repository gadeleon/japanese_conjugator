'''
Grab a word from wanikani cache
'''

import json
import pickle
import random

from pprint import pprint
from datetime import datetime

random.seed(datetime.now())


cache = pickle.load(open('wanikanicache.pkl', 'rb'))

data = cache.text

src = json.loads(data)


# Desired Kanji is in data[N][data['slug']
# Adj/Verb/Noun in data[N][data['parts_of_speech']



def _get_word(partofspeech):
    '''
    Randomly picks a word from wanikani's extensive vocab, If partofspeech matches (ie verb, noun, etc),
    then it returns
    :param partofspeech: ichidan_verb, na_adjective, i_adjective, etc.
    :return:
    '''
    word = random.choice(src['data'])
    #pprint(word)
    while partofspeech not in word['data']['parts_of_speech']:
        word = random.choice(src['data'])
        #pprint(word)
    return word['data']['slug']

