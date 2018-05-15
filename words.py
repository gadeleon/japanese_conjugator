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
        self.te = self._get_te_form(word)


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

    def _get_te_form(self, word):
        # exception
        if word.decode('utf-8') == u'行く':
            return u'行って'
        elif word.decode('utf-8') == u'いく':
            return u'いって'
        syl = word.decode('utf-8')[-1]
        base = u'{}'.format(word.decode('utf-8')[:-1])
        utte = [u'う', u'つ' ,u'る']
        nde = [u'ぬ', u'ぶ', u'ぬ']
        ite = [u'く']
        ide = [u'ぐ']
        shite = [u'す']
        if syl in utte:
            te = u'って'
        elif syl in nde:
            te = u'んで'
        elif syl in ite:
            te = u'いて'
        elif syl in ide:
            te = u'いで'
        elif syl in shite:
            te = u'して'
        return u'{}{}'.format(base,te)

    def _get_teinei_pos(self, word):
