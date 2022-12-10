# https://replit.com/@appbrewery/Day-7-Hangman-2-Start

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display.append('_')

while display.count('_') != 0:
    guess = input('Guess the letter: ')
    position = 0
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
        position += 1
    print(display)

