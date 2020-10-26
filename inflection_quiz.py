"""
Quiz on inflection changes for verbs and adjectives.
"""

import random


from datetime import datetime

import words
from vocab import wanikani_pull as source


random.seed(datetime.now())

# Possible Qs
form = ['teinei', 'nai', 'te', 'casual', 'passive', 'potential', 'causitive' ]
tense = ['present', 'past']
positivity = ['positive', 'negative']

def godan_quiz():
	v = source._get_word('godan verb')
	word = words.GodanVerb(v) 
	print(vars(word))
	print(word)
	print(f'Form: {random.choice(form)}, Tense: {random.choice(tense)}, {random.choice(positivity)}')

	answer = input('Input Answer: ')
	return True


if __name__ == '__main__':
	godan_quiz()