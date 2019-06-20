'''
So I don't have to do this in a python shell.
'''

import random 

from pprint import pprint 

import words

from vocab import wanikani_pull as source

from grammar.n4grammar import positive_comparison_extent as comp

topic = source._get_word('noun')

weak = source._get_word('noun')

adjec = source._get_word('i_adjective')
diff = words.IAdjective(adjec)

out = comp(topic, weak, diff.teinei['positive'])

print(out)

