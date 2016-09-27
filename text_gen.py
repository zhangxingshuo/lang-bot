'''
Markov Text Generation
======================
Consumes a corpus of text and generates random text.

Usage:
------
    python3 text_gen.py [<path to file>]
'''

import markovify
import sys

from markov import Markov

def generate_text(filename):
    '''
    Using python markovify package
    '''
    with open(filename) as f:
        text = f.read()

    text_model = markovify.Text(text)

    return text_model.make_short_sentence(140)

def markov_generate_text(filename):
    '''
    My method of markov chain text generation
    '''
    markov = Markov(filename)
    result = None
    while result is None:
        result = markov.generate_text()
    return result

if __name__ == '__main__':
    filename = sys.argv[1]
    print(markov_generate_text(filename))