from calculator_logo import logo

print(logo)


def calc(operation, n1, n2):
    if operation == '+':
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '/':
        return n1 / n2
    else:
        return 'Invalid Operation!'


operations = ['+', '-', '*', '/']
cont = 'y'
n1 = float(input('What is the first number?: '))
for item in operations:
    print(item)

while True:
    if cont == 'y':
        operation = input('Pick an operation: ')
        n2 = float(input('What is the next number?: '))
        result = calc(operation=operation, n1=n1, n2=n2)
        print(result)
        cont = input(
            f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ').lower()
    if cont == 'n':
        n1 = float(input('What is the first number?: '))
        operation = input('Pick an operation: ')
        n2 = float(input('What is the next number?: '))
        result = calc(operation=operation, n1=n1, n2=n2)
        print(result)
        cont = input(
            f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ').lower()
    n1 = result
