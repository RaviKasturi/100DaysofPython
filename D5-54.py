# https://app.codingrooms.com/management/assignments/364936/overview

start_num = int(input('Enter the starting number: '))
end_num = int(input('Enter the ending number: '))

i = 0
sum = 0

if start_num % 2 == 0:
    i = start_num
else:
    i = start_num + 1

while i <= end_num:
    sum += i
    i += 2

print(f'The sum of all even numbers between {start_num} and {end_num} is {sum}.')
