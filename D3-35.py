# https://app.codingrooms.com/management/assignments/364925/overview

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if extra_cheese == "Y":
    bill += 1

if add_pepperoni == "Y":
    if size == "S":
        bill += 17
    elif size == "M":
        bill += 23
    elif size == "L":
        bill += 28
    else:
        print('Incorrect pizza size!')
elif add_pepperoni == "N":
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print('Incorrect pizza size!')
else:
    print('Incorrect pepperoni selection!')

print(f'Your final bill is ${bill}.')


