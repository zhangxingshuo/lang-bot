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

class Markov(object):

    def __init__(self, filenames, order=2):
        '''
        Creates Markov object based on corpus. Default order is 2.
        '''
        self.cache = {}
        self.word_list = []
        for filename in filenames:
            print("Reading %s..." % filename)
            self.word_list.extend(self.parse_file(filename))
        self.order = order
        self.create_dictionary()

    def parse_file(self, filename):
        '''
        Takes in a file and returns a list of sanitized words
        '''
        file = open(filename)

        words = []
        for line in file.readlines():
            words.extend(line.split())

        # sanitize words by removing non-alphanumerics and converting to lowercase
        sanitized_words = [re.sub(r'\W+', '', word.lower()) for word in words if len(word) > 0]
        return sanitized_words

    def group_words(self):
        '''
        Groups words based on the order of Markov chain
        '''
        if len(self.word_list) < self.order:
            return
        for i in range(len(self.word_list) - (self.order-1)):
            yield self.word_list[i:i + (self.order+1)]

    def create_dictionary(self):
        '''
        Creates dictionary of grouped words and next words
        '''
        for words in self.group_words():
            key = tuple(words[:-1])
            value = words[-1]
            if key not in self.cache:
                self.cache[key] = [value]
            else:
                self.cache[key].append(value) 

    def generate_text(self, length=50):
        '''
        Generates random text based on dictionary
        '''
        seed = random.randint(0, len(self.word_list) - self.order)
        seed_words = self.word_list[seed:seed + (self.order+1)]
        words = seed_words
        gen_words = []
        for i in range(length):
            gen_words.append(words[0])
            words = words[1:]
            words.append(random.choice(self.cache[tuple(words)]))
        return ' '.join(gen_words)   

if __name__ == '__main__':
    filenames = sys.argv[1:]
    markov = Markov(filenames)
    print(markov.generate_text())