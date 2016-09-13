import markovify

with open('tale_two_cities.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

print(text_model.make_short_sentence(140))