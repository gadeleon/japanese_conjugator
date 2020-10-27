"""
Quiz on inflection changes for verbs and adjectives.
"""

import random


from pprint import pprint
from datetime import datetime

import words
from vocab import wanikani_pull as source

s = datetime.now()
print(f'Seed: {s!r}')
random.seed(s)

# Possible Qs
form = ['teinei', 'nai', 'te', 'casual', 'passive', 'potential', 'causitive' ]
tense = ['present', 'past']
positivity = ['positive', 'negative']

def godan_quiz(f=''):
	v = source._get_word('godan verb')
	print(v)
	word = words.GodanVerb(v) 
	# Pick a part of speech if not specified
	if not f:
		# Hardcode for now, 
		#f = random.choice(list(vars(word)))
		f = random.choice(['causitive_passive','potential'])
	q = f'{f}, '
	n = vars(word)[f]
	ready = False
	while not ready:
		try:
			if n.keys():
				f = random.choice(list(n))
				q += f'{f}, '
				n = n[f]
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
		elif answer == 'cheat':
			print(excepted)
		elif answer in excepted:
			correct = True
			return correct


if __name__ == '__main__':
	godan_quiz()