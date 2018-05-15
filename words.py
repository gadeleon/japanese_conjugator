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
        self.past_te = self._get_past_te_form(word)
        self.cas_pos = self._get_cas_pos(word)
        self.past_cas_pos = self._get_past_cas_pos(word)
        self.cas_neg = self._get_cas_neg(word)
        self.past_cas_neg = self._get_past_cas_neg(word)
        self.teinei_pos = self._get_teinei_pos(word)
        self.past_teinei_pos = self._get_past_teinei_pos(word)
        self.teinei_neg = self._get_teinei_neg(word)
        self.past_teinei_neg = self._get_past_teinei_neg(word)
        self.caus_cas_pos = self._get_caus_cas_pos(word)
        self.past_caus_cas_pos = self._get_past_caus_cas_pos(word)
        self.caus_cas_neg = self._get_caus_cas_neg(word)
        self.past_caus_cas_neg = self._get_past_caus_cas_neg(word)
        self.caus_teinei_pos = self._get_caus_teinei_pos(word)
        self.past_caus_teinei_pos = self._get_past_caus_teinei_pos(word)
        self.caus_teinei_neg = self._get_caus_teinei_neg(word)
        self.past_caus_teinei_neg = self._get_past_caus_teinei_neg(word)
        self.pas_cas_pos = self._get_pas_cas_pos(word)
        self.past_pas_cas_pos = self._get_past_pas_cas_pos(word)
        self.pas_cas_neg = self._get_pas_cas_neg(word)
        self.past_pas_cas_neg = self._get_past_pas_cas_neg(word)




    def __str__(self):
        return self.word

    def _get_stem(self, word):
        # Get the I stage changes for a godan verb
        syl = word.decode('utf-8')[-1]
        base = u'{}'.format(word.decode('utf-8')[:-1])
        if syl == u'う':
            stem = u'い'
        elif syl == u'く':
            stem = u'き'
        elif syl == u'ぐ':
            stem = u'ぎ'
        elif syl == u'す':
            stem = u'し'
        elif syl == u'ず':
            stem = u'じ'
        elif syl == u'つ':
            stem = u'ち'
        elif syl == u'づ':
            stem = u'ぢ'
        elif syl == u'ぬ':
            stem = u'に'
        elif syl == u'ふ':
            stem = u'ひ'
        elif syl == u'む':
            stem = u'み'
        elif syl == u'る':
            stem = u'り'
        stem = u'{}{}'.format(base, stem)
        return stem

    def _get_a_dan(self, word):
        # Get the A stage changes for a Godan Verb
        syl = word.decode('utf-8')[-1]
        base = word.decode('utf-8')[:-1]
        if syl == u'う':
            dan = u'わ'
        elif syl == u'く':
            dan = u'か'
        elif syl == u'ぐ':
            dan = u'が'
        elif syl == u'す':
            dan = u'さ'
        elif syl == u'ず':
            dan = u'ざ'
        elif syl == u'つ':
            dan = u'た'
        elif syl == u'づ':
            dan = u'だ'
        elif syl == u'ぬ':
            dan = u'な'
        elif syl == u'ふ':
            dan = u'は'
        elif syl == u'ぶ':
            dan = u'ば'
        elif syl == u'む':
            dan = u'ま'
        elif syl == u'る':
            dan = u'ら'
        return u'{}{}'.format(base,dan)

    def _get_nai_form(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'ない')

    def _get_past_nai_form(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'なかった')

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
        return u'{}{}'.format(base, te)

    def _get_past_te_form(self, word):
        te = self.te
        if te[-1] == u'て':
            past = u'た'
        elif te[-1] == u'で':
            past = u'だ'
        return u'{}{}'.format(te[:-1], past)

    def _get_cas_pos(self, word):
        return word

    def _get_past_cas_pos(self, word):
        return self.past_te

    def _get_cas_neg(self, word):
        return self._get_nai_form(word)

    def _get_past_cas_neg(self, word):
        return self._get_past_nai_form(word)

    def _get_teinei_pos(self, word):
        return u'{}{}'.format(self.stem, u'ます')

    def _get_past_teinei_pos(self, word):
        return u'{}{}'.format(self.stem, u'ました')

    def _get_teinei_neg(self, word):
        return u'{}{}'.format(self.stem, u'ません')

    def _get_past_teinei_neg(self, word):
        return u'{}{}'.format(self.stem, u'ませんでした')

    def _get_caus_cas_pos(self, word):
        # Make an Ichidan Te-Form maker
        return u'{}{}'.format(self._get_a_dan(word), u'せる')

    def _get_past_caus_cas_pos(self, word):
        # Make an Ichidan Te form-maker
        return u'{}{}'.format(self._get_a_dan(word), u'せた')

    def _get_caus_cas_neg(self, word):
        base = self._get_caus_cas_pos(word).encode('utf-8')
        return self._get_nai_form(base)

    def _get_past_caus_cas_neg(self, word):
        base = self._get_caus_cas_pos(word).encode('utf-8')
        return self._get_past_nai_form(base)

    def _get_caus_teinei_pos(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'せます')

    def _get_past_caus_teinei_pos(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'せました')

    def _get_caus_teinei_neg(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'ません')

    def _get_past_caus_teinei_neg(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'ませんでした')

    def _get_pas_cas_pos(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'れる')

    def _get_past_pas_cas_pos(self, word):
        return u'{}{}'.format(self._get_a_dan(word), u'れた')

    def _get_pas_cas_neg(self, word):
        base = self._get_pas_cas_pos(word).encode('utf-8')
        return self._get_nai_form(base)

    def _get_past_pas_cas_neg(self, word):
        base = self._get_pas_cas_pos(word).encode('utf-8')
        return self._get_past_nai_form(base)





