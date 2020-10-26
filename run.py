'''
So I don't have to do this in a python shell.
'''

import random 

from pprint import pprint 
from datetime import datetime


import words

from vocab import wanikani_pull as source

from grammar import n4grammar
from grammar.n4grammar import positive_comparison_extent as comp

random.seed(datetime.now())


topic = source._get_word('noun')

weak = source._get_word('noun')

adjec = source._get_word('i_adjective')
diff = words.IAdjective(adjec)

#out = comp(topic, weak, diff.teinei['positive'][random.choice(list(diff.teinei['positive'].keys()))])

#out = n4grammar.superlative(topic, '何', diff.teinei['positive'][random.choice(list(diff.teinei['positive'].keys()))])

print(out)

