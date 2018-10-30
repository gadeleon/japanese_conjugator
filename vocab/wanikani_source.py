'''
Serves as place to grab data from wanikani.
'''

import os
import pickle

import requests

AUTH = os.getenv('WKAPI')

BASE = 'https://api.wanikani.com/v2'

VOCAB = '/subjects?types=vocabulary'

HEADERS = {'Authorization':'Bearer {}'.format(AUTH)}

# Try and load previous request to get the etag

try:
    r = pickle.load(open('wanikanicache.pkl', 'rb'))
    HEADERS['If-None-Match'] = r.headers['Etag']

except FileNotFoundError:
    pass

r = requests.get('{}{}'.format(BASE,VOCAB), headers=HEADERS)

# Dump the request to file

pickle.dump(r, open('wanikanicache.pkl', 'wb'))

print('Updated WaniKani vocab cache!')