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
        if syl == u'う':
            stem = u'い'
        elif syl == u'す':
            steam = u'し'
        elif syl == u'く':
            stem = u'き'
        elif syl == u'つ':
            stem = u'{}ち'
        elif syl == u'ぬ':
            stem = u'に'
        elif syl == u'ふ':
            stem == u'ひ'
        elif syl == u'む':
            stem = u'み'
        elif syl == u'る':
            stem = u'り'
        stem = u'{}{}'.format(base, stem)
        return stem
