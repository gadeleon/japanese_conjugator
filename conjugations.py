# -*- coding: utf-8 -*-

'''
A dump of some conjugation functions I've been pondering
'''

def ichidan_pot_pas(word):
    '''
    Takes ichidan verbs and conjugates to the passive/potential form
    '''
    stem = word.decode('utf-8')[:-1].encode('utf-8')
    return '{}{}'.format(stem, 'られる')

def godan_pas_caus_sound(syl):
    '''
    Terrible if/else block to change the sound of a godan verb to the 
    passive/causitve sound.
    '''
    if syl.decode('utf-8') == 'う'.decode('utf-8'):
        return 'わ'
    elif syl.decode('utf-8') == 'く'.decode('utf-8'):
        return 'か'
    elif syl.decode('utf-8') == 'ぐ'.decode('utf-8'):
        return 'が'
    elif syl.decode('utf-8') == 'す'.decode('utf-8'):
        return 'さ'
    elif syl.decode('utf-8') == 'ず'.decode('utf-8'):
        return 'ざ'
    elif syl.decode('utf-8') == 'つ'.decode('utf-8'):
        return 'た'
    elif syl.decode('utf-8') == 'づ'.decode('utf-8'):
        return 'だ'
    elif syl.decode('utf-8') == 'ぬ'.decode('utf-8'):
        return 'な'
    elif syl.decode('utf-8') == 'ふ'.decode('utf-8'):
        return 'は'
    elif syl.decode('utf-8') == 'ぶ'.decode('utf-8'):
        return 'ば'
    elif syl.decode('utf-8') == 'ぷ'.decode('utf-8'):
        return 'ぱ'
    elif syl.decode('utf-8') == 'む'.decode('utf-8'):
        return 'ま'
    elif syl.decode('utf-8') == 'ゆ'.decode('utf-8'):
        return 'や'
    elif syl.decode('utf-8') == 'る'.decode('utf-8'):
        return 'ら'
    else:
        return None

def godan_passive(word):
    '''
    Takes a Godan verb and conjugates to its passive form.
    '''
    base = word.decode('utf-8')[:-1].encode('utf-8')
    snd = godan_pas_caus_sound(word.decode('utf-8')[-1].encode('utf-8'))
    return '{}{}{}'.format(base,snd,'れる')
