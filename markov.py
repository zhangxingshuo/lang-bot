'''
Markov Chain Text Generation
============================
Takes an input corpus of text and generates new text based on a 
seed word.

Additional functionality for higher order Markov chaining.

Usage:
------
    python3 markov.py [<filename>] ...
'''

import random
import re
import sys

from split import split_into_sentences

# Set flags for sentence beginning and end
BEGIN = '<BEGIN>'
END = '<END>'

class Markov(object):

    def __init__(self, filename, order=2):
        '''
        Creates Markov object based on corpus. Default order is 2.
        '''
        self.model = {}
        self.order = order

        # Read in the corpus text
        self.text = open(filename).read()

        # Generate list of lists
        # Outer list is list of sentences in text
        # Inner list is list of words in each sentence
        self.corpus = self.generate_corpus()

        # Generate the Markov dictionary
        self.create_dictionary()

    def sentence_split(self, text):
        '''
        Splits text into sentences
        '''
        return split_into_sentences(text)

    def word_split(self, sentence):
        '''
        Splits sentence into words
        '''
        word_split_pattern = re.compile(r"\s+")
        return re.split(word_split_pattern, sentence)

    def filter_sentence(self, sentence):
        '''
        Sentence filter to eliminate weird punctuation
        '''
        reject_pat = re.compile(r"(^')|('$)|\s'|'\s|[\"(\(\)\[\])]")
        # Decode unicode, mainly to normalize fancy quotation marks
        if sentence.__class__.__name__ == "str":
            decoded = sentence
        else:
            decoded = unidecode(sentence)
        # Sentence shouldn't contain problematic characters
        if re.search(reject_pat, decoded): 
            return False
        return True

    def generate_corpus(self):
        '''
        Generates list of sentences, where each sentence is a list of words
        '''
        sentences = self.sentence_split(self.text)
        filtered_sentences = list(filter(self.filter_sentence, sentences))
        words = list(map(self.word_split, filtered_sentences))
        return words

    def create_dictionary(self):
        '''
        Creates the Markov dictionary
        '''
        for sentence in self.corpus:
            item = ( [BEGIN] * self.order ) + sentence + [END]
            for i in range(len(sentence) + 1):
                state = tuple(item[i:i+self.order])
                follow = item[i+self.order]

                if state not in self.model:
                    self.model[state] = {}
                if follow not in self.model[state]:
                    self.model[state][follow] = 0

                self.model[state][follow] += 1

    def move(self, state):
        '''
        Move to next word
        '''
        choices, weights = zip(*self.model[state].items())
        totals = []
        running_total = 0

        # accumulate weights
        for weight in weights:
            running_total += weight
            totals.append(running_total)

        rnd = random.random() * running_total

        # find and return the index
        for i, total in enumerate(totals):
            if rnd < total:
                return choices[i]

    def generate_text(self, length=50):
        '''
        Generates random text based on dictionary
        '''
        state = (BEGIN,) * self.order
        next_word = self.move(state)
        text = ''
        while next_word != END:
            text += next_word + ' '
            state = tuple(state[1:]) + (next_word,)
            next_word = self.move(state)
        return text[:-1]