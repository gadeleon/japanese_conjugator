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
	verbstage = random.choice(styles.keys())
	verb = random.choice(verbs.verb1[verbstage].keys())
	return verb
