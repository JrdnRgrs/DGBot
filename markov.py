import markovify
import random
import os


# Creates the post and logs to a file
with open(os.path.dirname(__file__) + '/dglyrics.txt') as f:
    text = f.read()

text_model = markovify.NewlineText(text)

for i in range(5):
    print(text_model.make_sentence())
