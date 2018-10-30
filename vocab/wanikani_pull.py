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

no = _grab_noun()
print(no)