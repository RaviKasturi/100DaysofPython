# https://app.codingrooms.com/management/assignments/364928/overview
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name = names[random.randint(0, len(names)-1)]

print(f'{name} is going to buy the meal today.')

