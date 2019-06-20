'''
N4 level grammar constructions
'''

def positive_comparison_extent(strong_noun, weak_noun, comparison):
	'''
	Produces the grammar where you compare two nouns. 
	Effictively stroung_noun is more comparison than weak_noun
	This is NOT an expression of preference.
	Generally the strong noun is the topic of the sentence.
	'''
	return '{}は{}{}'.format(strong_noun, weak_noun, comparison)