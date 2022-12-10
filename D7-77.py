# https://replit.com/@appbrewery/Day-7-Hangman-2-Start

import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
display = []
lives = len(stages)

for letter in chosen_word:
    display.append('_')

while lives != 0:
    guess = input('Guess the letter: ')
    if guess not in display:
        if guess in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            print(f'{guess} is not in the word.')
            lives -= 1
            print(stages[lives])
    else:
        print('{guess} is already guessed')
    print(f"Word:  {''.join(display)}")

if "_" not in display:
    print("You win.")
else:
    print('You lose!')

