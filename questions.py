# -*- coding: utf-8 -*-

import random

import conjugations
import vocab.japanese_verbs as verbs

def passive_question():
    styles = {
        'godan':conjugations.godan_passive,
        'ichidan':conjugations.ichidan_pot_pas,
        'irregular':conjugations.irregular_passive
    }
    # Pick which type of verb we'll ask about
    verbstage = random.choice(styles.keys())

    # Grab a verb from the appropriate style
    verb = random.choice(verbs.verb1[verbstage].keys())

    # Conjugated verb is the correct answer
    correct = styles[verbstage](verb)

    # Set up question/answer question
    user_answer = raw_input('Enter the Passive form of {}: '.format(verb))
    
    while user_answer != correct:
        print 'Nope! Try again!'
        user_answer = raw_input('Enter the Passive form of {}: '.format(verb))
    print '正解！'

if __name__ == '__main__':
    # This will likely have arguments like "passive, potential, polite, causitive, mixed bag, and number of questions"
    # For now, we'll keep it at one type at a time
    passive_question()