'''
N4 level grammar constructions
'''

def positive_comparison_extent(topic, weak_noun, comparison):
	'''
	Produces the grammar where you compare two nouns. 
	Effictively topical_noun is more comparison than weak_noun
	This is NOT an expression of preference.
	'''
	return '{}は{}より{}'.format(topic, weak_noun, comparison)

def superlative(topic, interogative, comparison):
	'''
	Create a superlative sentence.
	'''
	return '{}は{}より{}'.format(topic, interogative, comparison)