'''
N4 level grammar constructions
'''

def positive_comparison_extent(topical_noun, weak_noun, adjective):
	'''
	Produces the grammar where you compare two nouns. 
	Effictively topical_noun is more comparison than weak_noun
	This is NOT an expression of preference.
	'''
	return '{}は{}より{}'.format(topical_noun, weak_noun, adjective)

