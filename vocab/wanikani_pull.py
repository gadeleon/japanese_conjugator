'''
Grab a word from wanikani cache
'''

import json
import pickle

cache = pickle.load(open('wanikanicache.pkl', 'rb'))

data = cache.text

print(data)