# https://replit.com/@appbrewery/Day-7-Hangman-1-Start#main.py

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input('Guess the letter: ')

if guess in chosen_word:
    print('Yes')
else:
    print('No')

