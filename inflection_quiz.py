"""
Quiz on inflection changes for verbs and adjectives.
"""

import random


from pprint import pprint
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
	print(v)
	word = words.GodanVerb(v) 
	print(word)
	pprint(vars(word))
	#f = random.choice(list(vars(word)))
	f = 'causitive_passive'
	print(f)
	q = f'{f}, '
	n = vars(word)[f]
	ready = False
	while not ready:
		try:
			if n.keys():
				print('\n',n)
				f = random.choice(list(n))
				q += f'{f}, '
				n = n[f]
				print(n)

			else:
				ready = True
		except AttributeError:
			excepted = n
			ready = True



	#print(f'Form: {random.choice(form)}, Tense: {random.choice(tense)}, {random.choice(positivity)}')
	print(f'\n{q[:-1]}')
	correct = False
	while not correct:
		answer = input(f'{word}: ')
		if answer == excepted:
			correct = True
			return correct


if __name__ == '__main__':
	godan_quiz()