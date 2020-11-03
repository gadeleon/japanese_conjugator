'''
Module for Ichidan Verbs
'''

import words

class IchidanVerb(words.Word):
    def __init__(self, word):
        super(IchidanVerb, self).__init__(word)
        self.stem = self._get_stem(word)
        self.te = self._get_te(word)
        self.past_te = self._get_past_te(word)
        self.teinei = self._get_teinei_hash(word)

    def _get_stem(self, word):
    	return word[:-1]

    def _get_nai(self, word):
        return f'{self.stem}ない'

    def _get_te(self, word):
    	return '{}{}'.format(self._get_stem(word), 'て')

    def _get_past_te(self, word):
    	return '{}{}'.format(self._get_stem(word), 'た')

    def _get_teinei_pos(self, word):
    	return '{}{}'.format(self._get_stem(word), 'ます')

    def _get_past_teinei_pos(self, word):
    	return '{}{}'.format(self._get_stem(word), 'ました')

    def _get_teinei_neg(self, word):
    	return '{}{}'.format(self._get_stem(word), 'ません')

    def _get_past_teinei_neg(self, word):
    	return '{}{}'.format(self._get_stem(word), 'ませんでした')

    def _get_teinei_hash(self, word):
    	out = {
    		'postive': self._get_teinei_pos(word),
    		'negative': self._get_teinei_neg(word),
    		'past_pos': self._get_past_teinei_pos(word),
    		'past_neg': self._get_past_teinei_neg(word)

    	}

    	return out
