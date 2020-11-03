'''
Module for Ichidan Verbs
'''

import words

class IchidanVerb(words.Word):
    def __init__(self, word, from_godan=False):
        super(IchidanVerb, self).__init__(word)
        self.stem = self._get_stem(word)
        self.nai = self._get_nai(word)
        self.past_nai = self._get_past_nai(word)
        self.te = self._get_te(word)
        self.past_te = self._get_past_te(word)
        self.teinei = self._get_teinei_hash(word)
        self.casual = self._get_cas_hash(word)
        # Don't want to make gibberish if generating 
        # causitive, passive, etc from godan verbs
        if not from_godan:
            self.causitive = self._get_causitive(word)
            self.causitive_hash = self._get_inflection_hash(self.causitive)


    def _get_stem(self, word):
    	return word[:-1]

    def _get_nai(self, word):
        return f'{self._get_stem(word)}ない'

    def _get_past_nai(self, word):
        return f'{self._get_stem(word)}なかった'

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

    def _get_cas_pos(self, word):
        return word

    def _get_cas_neg(self, word):
        return self._get_nai(word)

    def _get_past_cas_pos(self, word):
        return self._get_past_te(word)

    def _get_past_cas_neg(self, word):
        return f'{self._get_stem(word)}なかった'

    def _get_teinei_hash(self, word):
        out = {}
        out['present'] = {
            'positive' : self._get_teinei_pos(word),
            'negative' : self._get_teinei_neg(word)
        }
        out['past'] = {
            'positive' : self._get_past_teinei_pos(word),
            'negative' : self._get_past_teinei_neg(word)
        }
        return out

    def _get_cas_hash(self, word):
        out = {}
        out['present'] = {
            'positive' : self._get_cas_pos(word),
            'negative' : self._get_cas_neg(word)
        }
        out['past'] = {
            'positive' : self._get_past_cas_pos(word),
            'negative' : self._get_past_cas_neg(word)
        }
        return out

    def _get_causitive(self, word):
        return f'{self._get_stem(word)}させる'

    def _get_inflection_hash(self, word):
        out = {}
        out['casual'] = self._get_cas_hash(word)
        out['teinei'] = self._get_teinei_hash(word)
        return out



