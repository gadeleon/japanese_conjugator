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

class IAdjective(Word):
    def __init__(self, word):
        super(IAdjective, self).__init__(word)
        self.stem = self._get_stem(word)
        self.adverb = self._get_adverb(word)
        self.te = self._get_te_hash(word)
        self.casual = self._get_casual_hash(word)
        self.teinei = self._get_teinei_hash(word)



    def _get_stem(self, word):
        if word[-2:] == 'いい':
            word = 'よい'
        return word[:-1]

    def _get_adverb(self, word):
        return '{}く'.format(self._get_stem(word))

    def _get_nai_form(self, word):
        return '{}ない'.format(self._get_adverb(word))

    def _get_te_hash(self, word):
        out = {}
        out['positive'] = '{}て'.format(self._get_adverb(word)),
        out['negative'] = '{}て'.format(self._get_adverb(self._get_nai_form(self._get_adverb(word))))
        return out


    def _get_casual_hash(self, word):
        out = {}
        out['positive'] = word
        out['negative'] = self._get_nai_form(word)
        out['past_pos'] = '{}かった'.format(self._get_stem(word))
        out['past_neg'] = '{}かった'.format(self._get_stem(self._get_nai_form(word)))

        return out

    def _get_teinei_hash(self, word):
        out = {}
        out['positive'] = {
                            'present':'{}です'.format(word),
                            'past':'{}かったです'.format(self._get_stem(word))
                            }
        out['negative'] = '{}です'.format(self._get_nai_form(word))
        out['past_pos'] = '{}かったです'.format(self._get_stem(word))
        out['past_neg'] = '{}かったです'.format(self._get_stem(self._get_nai_form(word)))
        return out


class NaAdjective(Word):
    def __init__(self, word):
        super(NaAdjective, self).__init__(word)
        self.stem = self._get_stem(word)
        self.adverb = self._get_adverb(word)
        self.te = self._get_te_hash(word)
        self.predicate = self._get_predicate_hash(word)
        self.casual = self._get_cas_ending_hash(word)
        self.teinei = self._get_teinei_ending_hash(word)


    def _get_stem(self, word):
        return word

    def _get_adverb(self, word):
        return '{}に'.format(word)

    def _get_te_hash(self, word):
        out = {}
        out['positive'] = '{}で'.format(word)
        out['negative'] = '{}ではなくて'.format(word)
        out['col_neg'] = '{}じゃなくて'.format(word)
        return out

    def _get_predicate_hash(self, word):
        '''
        Na-Adjectives, when used before the noun they modify
        take on this form. Note that な is a conjugation of the
        verb だ. When you make it negative, the predicate
        behaves like an い adjective.
        :param word: word to conjugate
        :return: dict of values
        '''
        out = {}
        out['positive'] = '{}な'.format(word)
        out['negative'] = '{}ではない'.format(word)
        out['col_neg'] = '{}じゃない'.format(word)
        return out

    def _get_cas_ending_hash(self, word):
        '''
        Since Na adjectives use auxiliary verbs when they're not paired
        next to a noun, you use them differently (like a noun) when
        putting them at the end of the sentence.
        :param word: word to conjugate
        :return: dict of values
        '''
        out = {}
        out['positive'] = '{}だ'.format(word)
        out['negative'] = '{}ではない'.format(word)
        out['col_neg'] = '{}じゃない'.format(word)
        out['past_pos'] = '{}だった'.format(word)
        out['past_neg'] = '{}ではなかった'.format(word)
        out['past_col_neg'] = '{}じゃなかった'.format(word)
        return out

    def _get_teinei_ending_hash(self, word):
        out = {}
        out['positive'] = '{}です'.format(word)
        out['negative'] = '{}ではありません'.format(word)
        out['col_neg'] = '{}じゃありません'.format(word)
        out['past_pos'] = '{}でした'.format(word)
        out['past_neg'] = '{}ではありませんでした'.format(word)
        out['past_col_neg'] = '{}じゃありませんでした'.format(word)
        return out

class GodanVerb(Word):
    def __init__(self, word):
        super(GodanVerb, self).__init__(word)
        self.stem = self._get_stem(word)
        self.te = self._get_te_form(word)
        self.past_te = self._get_past_te_form(word)
        self.casual = self._get_cas_hash(word)
        self.teinei = self._get_teinei_hash(word)
        self.causitive = self._get_causitive_hash(word)
        self.passive = self._get_passive_hash(word)
        self.causitive_passive = self._get_causpas_hash(word)
        self.potential = self._get_potential_hash(word)
        self.volitional = self._get_volitional_hash(word)


    def _get_stem(self, word):
        # Get the I stage changes for a godan verb
        syl = word[-1]
        base = '{}'.format(word   [:-1])
        if syl == 'う':
            stem = 'い'
        elif syl == 'く':
            stem = 'き'
        elif syl == 'ぐ':
            stem = 'ぎ'
        elif syl == 'す':
            stem = 'し'
        elif syl == 'ず':
            stem = 'じ'
        elif syl == 'つ':
            stem = 'ち'
        elif syl == 'づ':
            stem = 'ぢ'
        elif syl == 'ぬ':
            stem = 'に'
        elif syl == 'ふ':
            stem = 'ひ'
        elif syl == 'ぶ':
            stem = 'び'
        elif syl == 'む':
            stem = 'み'
        elif syl == 'る':
            stem = 'り'
        stem = '{}{}'.format(base, stem)
        return stem

    def _get_a_dan(self, word):
        # Get the A stage changes for a Godan Verb
        syl = word[-1]
        base = word[:-1]
        if syl == 'う':
            dan = 'わ'
        elif syl == 'く':
            dan = 'か'
        elif syl == 'ぐ':
            dan = 'が'
        elif syl == 'す':
            dan = 'さ'
        elif syl == 'ず':
            dan = 'ざ'
        elif syl == 'つ':
            dan = 'た'
        elif syl == 'づ':
            dan = 'だ'
        elif syl == 'ぬ':
            dan = 'な'
        elif syl == 'ふ':
            dan = 'は'
        elif syl == 'ぶ':
            dan = 'ば'
        elif syl == 'む':
            dan = 'ま'
        elif syl == 'る':
            dan = 'ら'
        return '{}{}'.format(base,dan)

    def _get_e_dan(self, word):
        # Get the E stage changes for a Godan Verb
        syl = word[-1]
        base = word[:-1]
        if syl == 'う':
            dan = 'え'
        elif syl == 'く':
            dan = 'け'
        elif syl == 'ぐ':
            dan = 'げ'
        elif syl == 'す':
            dan = 'せ'
        elif syl == 'ず':
            dan = 'ぜ'
        elif syl == 'つ':
            dan = 'て'
        elif syl == 'づ':
            dan = 'で'
        elif syl == 'ぬ':
            dan = 'ね'
        elif syl == 'ふ':
            dan = 'へ'
        elif syl == 'ぶ':
            dan = 'べ'
        elif syl == 'む':
            dan = 'め'
        elif syl == 'る':
            dan = 'れ'
        return '{}{}'.format(base, dan)

    def _get_o_dan(self, word):
        # Get the O stage changes for a Godan Verb
        syl = word[-1]
        base = word[:-1]
        if syl == 'う':
            dan = 'お'
        elif syl == 'く':
            dan = 'こ'
        elif syl == 'ぐ':
            dan = 'ご'
        elif syl == 'す':
            dan = 'そ'
        elif syl == 'ず':
            dan = 'ぞ'
        elif syl == 'つ':
            dan = 'と'
        elif syl == 'づ':
            dan = 'ど'
        elif syl == 'ぬ':
            dan = 'の'
        elif syl == 'ふ':
            dan = 'ほ'
        elif syl == 'ぶ':
            dan = 'ぼ'
        elif syl == 'む':
            dan = 'も'
        elif syl == 'る':
            dan = 'ろ'
        return '{}{}'.format(base, dan)

    def _get_nai_form(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'ない')

    def _get_past_nai_form(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'なかった')

    def _get_te_form(self, word):
        # exception
        if word == '行く':
            return '行って'
        elif word == 'いく':
            return 'いって'
        syl = word[-1]
        base = '{}'.format(word[:-1])
        utte = ['う', 'つ','る']
        nde = ['む', 'ぶ', 'ぬ']
        ite = ['く']
        ide = ['ぐ']
        shite = ['す']
        if syl in utte:
            te = 'って'
        elif syl in nde:
            te = 'んで'
        elif syl in ite:
            te = 'いて'
        elif syl in ide:
            te = 'いで'
        elif syl in shite:
            te = 'して'
        return '{}{}'.format(base, te)

    def _get_past_te_form(self, word):
        te = self.te
        if te[-1] == 'て':
            past = 'た'
        elif te[-1] == 'で':
            past = 'だ'
        return '{}{}'.format(te[:-1], past)

    def _get_cas_pos(self, word):
        return word

    def _get_past_cas_pos(self, word):
        return self.past_te

    def _get_cas_neg(self, word):
        return self._get_nai_form(word)

    def _get_past_cas_neg(self, word):
        return self._get_past_nai_form(word)

    def _get_cas_hash(self, word):
        out = {
            'positive': self._get_cas_pos(word),
            'negative': self._get_cas_neg(word),
            'past_pos': self._get_past_cas_pos(word),
            'past_neg': self._get_past_cas_neg(word)
            }
        return out

    def _get_teinei_pos(self, word):
        return '{}{}'.format(self.stem, 'ます')

    def _get_past_teinei_pos(self, word):
        return '{}{}'.format(self.stem, 'ました')

    def _get_teinei_neg(self, word):
        return '{}{}'.format(self.stem, 'ません')

    def _get_past_teinei_neg(self, word):
        return '{}{}'.format(self.stem, 'ませんでした')

    def _get_teinei_hash(self, word):
        out = {
            'positive': self._get_teinei_pos(word),
            'negative': self._get_teinei_neg(word),
            'past_pos': self._get_past_teinei_pos(word),
            'past_neg': self._get_past_teinei_neg(word)
            }
        return out

    def _get_caus_cas_pos(self, word):
        # Make an Ichidan Te-Form maker
        return '{}{}'.format(self._get_a_dan(word), 'せる')

    def _get_past_caus_cas_pos(self, word):
        # Make an Ichidan Te form-maker
        return '{}{}'.format(self._get_a_dan(word), 'せた')

    def _get_caus_cas_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'せない')

    def _get_past_caus_cas_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'せなかった')

    def _get_caus_teinei_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'せます')

    def _get_past_caus_teinei_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'せました')

    def _get_caus_teinei_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'ません')

    def _get_past_caus_teinei_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'ませんでした')

    def _get_causitive_hash(self, word):
        out = {}
        out['teinei'] = {
            'positive': self._get_caus_teinei_pos(word),
            'negative': self._get_caus_teinei_pos(word),
            'past_pos': self._get_past_caus_teinei_pos(word),
            'past_neg': self._get_past_caus_teinei_neg(word)
        }
        out['casual'] = {
            'positive': self._get_caus_cas_pos(word),
            'negative': self._get_caus_cas_neg(word),
            'past_pos': self._get_past_caus_cas_pos(word),
            'past_neg': self._get_past_caus_cas_neg(word)
        }
        return out

    def _get_pas_cas_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れる')

    def _get_past_pas_cas_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れた')

    def _get_pas_cas_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れない')

    def _get_past_pas_cas_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れなかった')

    def _get_pas_teinei_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れます')

    def _get_past_pas_teinei_pos(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れました')

    def _get_pas_teinei_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れません')

    def _get_past_pas_teinei_neg(self, word):
        return '{}{}'.format(self._get_a_dan(word), 'れませんでした')

    def _get_passive_hash(self, word):
        out = {}
        out['teinei'] = {
            'positive': self._get_pas_teinei_pos(word),
            'negative': self._get_pas_teinei_neg(word),
            'past_pos': self._get_past_pas_teinei_pos(word),
            'past_neg': self._get_past_pas_teinei_neg(word)
        }
        out['casual'] = {
            'positive': self._get_pas_cas_pos(word),
            'negative': self._get_pas_cas_neg(word),
            'past_pos': self._get_past_pas_cas_pos(word),
            'past_neg': self._get_past_pas_cas_neg(word)
        }
        return out

    def _get_pot_cas_pos(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'る')

    def _get_past_pot_cas_pos(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'た')

    def _get_pot_cas_neg(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'ない')

    def _get_past_pot_cas_neg(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'なかった')

    def _get_pot_teinei_pos(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'ます')

    def _get_past_pot_teinei_pos(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'ました')

    def _get_pot_teinei_neg(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'ません')

    def _get_past_pot_teinei_neg(self, word):
        return '{}{}'.format(self._get_e_dan(word), 'ませんでした')


    def _get_potential_hash(self, word):
        out = {}
        # out['teinei'] = {
        #     'positive': self._get_pot_teinei_pos(word),
        #     'negative': self._get_pot_teinei_neg(word),
        #     'past_pos': self._get_past_pot_teinei_pos(word),
        #     'past_neg': self._get_past_pot_teinei_neg(word)

        # }
        # out['casual'] = {
        #     'positive': self._get_pot_cas_pos(word),
        #     'negative': self._get_pot_cas_neg(word),
        #     'past_pos': self._get_past_pot_cas_pos(word),
        #     'past_neg': self._get_past_pot_cas_neg(word)

        # }
        out['casual'] = {
            'present' : {
                'positive' : self._get_pot_cas_pos(word),
                'negative' : self._get_pot_cas_neg(word)
            },
            'past' : {
                'positive' : self._get_past_pot_cas_pos(word),
                'negative' : self._get_past_pot_cas_neg(word)
            }
        }
        out['teinei'] = {
            'present' : {
                'positive' : self._get_pot_teinei_pos(word),
                'negative' : self._get_pot_teinei_neg(word)
            },
            'past' : {
                'positive' : self._get_past_pot_teinei_pos(word),
                'negative' : self._get_past_pot_teinei_neg(word)
            }
        }
        return out

    def _get_causpas_cas_pos(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられる')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'される'),
                '{}{}'.format(self._get_a_dan(word), 'せられる')
                ]
            

    def _get_past_causpas_cas_pos(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられた')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'された'),
                '{}{}'.format(self._get_a_dan(word), 'せられた')
                ]

    def _get_causpas_cas_neg(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられない')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されない'),
                '{}{}'.format(self._get_a_dan(word), 'せられない')
                ]

    def _get_past_causpas_cas_neg(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられなかった')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されなかった'),
                '{}{}'.format(self._get_a_dan(word), 'せられなかった')
                ]

    def _get_causpas_teinei_pos(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられます')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されます'),
                '{}{}'.format(self._get_a_dan(word), 'せられます')
                ]

    def _get_past_causpas_teinei_pos(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられました')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されました'),
                '{}{}'.format(self._get_a_dan(word), 'せられました')
                ]

    def _get_causpas_teinei_neg(self, word):
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられません')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されません'),
                '{}{}'.format(self._get_a_dan(word), 'せられません')
                ]

    def _get_past_causpas_teinei_neg(self, word):
        # す　verbs are execptions and conjugated like ichidan verbs
        if word[-1] == 'す':
            return '{}{}'.format(self._get_a_dan(word), 'せられませんでした')
        else:
            return [
                '{}{}'.format(self._get_a_dan(word), 'されませんでした'),
                '{}{}'.format(self._get_a_dan(word), 'せられませんでした')
                ]

    def _get_causpas_hash(self, word):
        out = {}
        # out['teinei'] = {
        #     'positive': self._get_causpas_teinei_pos(word),
        #     'negative': self._get_causpas_teinei_neg(word),
        #     'past_pos': self._get_past_causpas_teinei_pos(word),
        #     'past_neg': self._get_past_causpas_teinei_neg(word)
        # }

        # out['casual'] = {
        #     'positive': self._get_causpas_cas_pos(word),
        #     'negative': self._get_causpas_cas_neg(word),
        #     'past_pos': self._get_past_causpas_cas_pos(word),
        #     'past_neg': self._get_past_causpas_cas_neg(word)
        # }
        out['casual'] = {
            'present' : {
                'positive' : self._get_causpas_cas_pos(word),
                'negative' : self._get_causpas_cas_neg(word)
            },
            'past' : {
                'positive' : self._get_past_causpas_cas_pos(word),
                'negative' : self._get_past_causpas_cas_neg(word)
            }

        }
        out['teinei'] = {
            'present' : {
                'positive' : self._get_causpas_teinei_pos(word),
                'negative' : self._get_causpas_teinei_neg(word)

            },
            'past' : {
                'positive' : self._get_past_causpas_teinei_pos(word),
                'negative' : self._get_past_causpas_teinei_neg(word)
            }
        }
        return out

    def _get_vol_cas_pos(self, word):
        return '{}{}'.format(self._get_o_dan(word), 'う')

    def _get_vol_cas_neg(self, word):
        return '{}{}'.format(word, 'まい')

    def _get_vol_teinei_pos(self, word):
        tei = self._get_teinei_pos(word)
        return '{}{}'.format(tei[:-1], 'しょう')

    def _get_vol_teinei_neg(self, word):
        return '{}{}'.format(self._get_teinei_pos(word), 'まい')

    def _get_volitional_hash(self,word):
        out = {}
        out['teinei'] = {
            'positive': self._get_vol_teinei_pos(word),
            'negative': self._get_vol_teinei_neg(word)
        }
        out['casual'] = {
            'positive': self._get_vol_cas_pos(word),
            'negative': self._get_vol_cas_neg(word)
        }

        return out







