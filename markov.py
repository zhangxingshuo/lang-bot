'''
Markov Chain Text Generation
============================
Takes an input corpus of text and generates new text based on a 
seed word.

Additional functionality for higher order Markov chaining.
'''

import random
import re

class Markov(object):

    def __init__(self, filename, order=2):
        self.cache = {}
        self.word_list = self.parse_file(filename)
        self.order = order
        self.create_dictionary()

    def parse_file(self, filename):
        file = open(filename)
        words = []
        for line in file.readlines():
            words.extend(line.split())
        sanitized_words = [re.sub(r'\W+', '', word.lower()) for word in words if len(word) > 0]
        return sanitized_words

    def group_words(self):
        if len(self.word_list) < self.order:
            return
        for i in range(len(self.word_list) - (self.order-1)):
            yield self.word_list[i:i + (self.order+1)]

    def create_dictionary(self):
        for words in self.group_words():
            key = tuple(words[:-1])
            value = words[-1]
            if key not in self.cache:
                self.cache[key] = [value]
            else:
                self.cache[key].append(value) 

    def generate_text(self, length=50):
        seed = random.randint(0, len(self.word_list) - self.order)
        seed_words = self.word_list[seed:seed + (self.order+1)]
        words = seed_words
        gen_words = []
        for i in range(length):
            gen_words.append(words[0])
            words = words[1:]
            words.append(random.choice(self.cache[tuple(words)]))
        return ' '.join(gen_words)    