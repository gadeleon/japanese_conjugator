# -*- coding: utf-8 -*-

'''
Object for nouns, verbs, adjectives.
'''

class Word(object):
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word

