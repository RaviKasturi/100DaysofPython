# https://app.codingrooms.com/management/assignments/364926/overview

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name3 = name1.lower()+name2.lower()

x = str(name3.count('t') + name3.count('r') + name3.count('u') + name3.count('e'))
y = str(name3.count('l') + name3.count('o') + name3.count('v') + name3.count('e'))

score = int(x+y)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f'Your score is {score}.')

