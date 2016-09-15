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

def generate_text(filenames):
    '''
    Using python markovify package
    '''
    text_models = []

    for filename in filenames:

        with open(filename) as f:
            text = f.read()

        text_models.append(markovify.Text(text))

    total_model = markovify.combine(text_models)

    return total_model.make_short_sentence(140)

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
    filenames = sys.argv[1:]
    print(generate_text(filenames))