# -*- coding: utf-8 -*-

'''
Object for nouns, verbs, adjectives.
'''

class Word(object):
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

    # def __repr__(self):
    #     return self.word


class GodanVerb(Word):
    def __init__(self, word):
        super(GodanVerb, self).__init__(word)
        self.stem = self._get_stem(word)


    def __str__(self):
        return self.word

    def _get_stem(self, word):
        syl = word.decode('utf-8')[-1]
        base = u'{}'.format(word.decode('utf-8')[:-1])
        if syl == u'つ':
            stem = u'{}ち'.format(base)
        return stem
