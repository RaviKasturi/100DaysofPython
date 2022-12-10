# https://app.codingrooms.com/management/assignments/364946/overview

def prime_checker(number):
    divisor = 2
    prime = True
    while prime and divisor <= number/2:
        remainder = number % divisor
        if remainder == 0:
            prime = False
            print(f'{number} is not a prime number. It is divisible by {divisor}.')
        elif divisor + 1 > number/2:
            print(f'{number} is a prime number.')
        divisor += 1


n = int(input("Check this number: "))
prime_checker(number=n)