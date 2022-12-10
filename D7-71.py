# https://replit.com/@appbrewery/Day-7-Hangman-2-Start

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display.append('_')

guess = input('Guess the letter: ')

for letter in chosen_word:
    if letter == guess:
        display[chosen_word.index(letter)] = letter

print(display)

