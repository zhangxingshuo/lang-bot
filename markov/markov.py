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
BEGIN = '__BEGIN__'
END = '__END__'

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

class BetterMarkov(object):

    def __init__(self, filename, order=2):
        self.cache = {}
        self.order = order
        self.word_list = self.parse_file(filename)
        self.create_dictionary()

    def parse_file(self, filename):
        file = open(filename)
        raw_text = file.read()
        # replace newlines with spaces
        raw_text = raw_text.replace('\n', ' ')
        # remove backslashes
        raw_text = raw_text.replace('\\', '')
        # add $ to mark beginning and ending of sentences
        newText = raw_text.replace('.', '.'+' $'* self.order)
        newText = '$ ' * self.order + newText
        textList = newText.split(' ')
        return textList

    def create_dictionary(self):

        def all_same(L, e):
            for elem in L:
                if elem != e:
                    return False
            return True

        for i in range(len(self.word_list) - self.order - 1):
            # Dollar signs track what go after periods or start sentences, so we should not include them in the
            # values of the markov dictionary
            if self.word_list[i + self.order] != '$':
                # creates a key for textList consisting of the k objects in textList (in order of which they appear)
                key = tuple(self.word_list[i:i + self.order])
                # if the key is valid (ie only all $ signs, or ends with a letter/number)
                if '$' != key[-1] or all_same(key, '$'):
                    if key in self.cache.keys():
                        self.cache[key] += [self.word_list[i + self.order]]
                    else:
                        self.cache[key] = [self.word_list[i + self.order]]

    def generate_text(self, length=50):
        keys = list(self.cache.keys())
        string_list = []
        curr_word = ['$'] * self.order
        string_list += curr_word

        num_words = 0
        while num_words < length:
            if tuple(curr_word) in keys:
                next_word = random.choice(self.cache[tuple(curr_word)])
                string_list += [next_word]
                curr_word = string_list[-self.order:]
                num_words += 1
            else:
                curr_word.pop()
                curr_word = ['$'] + curr_word
            if '.' in string_list[-1]:
                curr_word = ['$'] * self.order

        string = ''
        for word in string_list:
            if word != '$':
                string += word + ' '
        return string