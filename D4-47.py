# https://replit.com/@appbrewery/rock-paper-scissors-start#main.py

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = options[int(input('What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors.\n'))]
computer_choice = options[random.randint(0, len(options)-1)]

print(f'You chose: \n {user_choice}')
print(f'Computer chose: \n {computer_choice}')

if user_choice == computer_choice:
    print('It is a draw!')
elif user_choice == 0:
    if computer_choice == 1:
        print('You lose!')
    else:
        print('You win!')
elif user_choice == 1:
    if computer_choice == 0:
        print('You win!')
    else:
        print('You lose!')
else:
    if computer_choice == 1:
        print('You lose!')
    else:
        print('You win!')
