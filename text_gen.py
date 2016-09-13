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
    with open(filename) as f:
        text = f.read()

    text_model = markovify.Text(text)

    return text_model.make_short_sentence(140)

def markov_generate_text(filename):
    '''
    My method of markov chain text generation
    '''
    markov = Markov(filename)
    raw_text = markov.generate_text().split()

    text = ''
    index = 0

    while len(text + raw_text[index] + ' ') <= 140:
        text += raw_text[index] + ' '
        index += 1

    return text

if __name__ == '__main__':
    filename = sys.argv[1]
    print(generate_text(filename))