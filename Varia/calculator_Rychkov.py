def exponent(a, b):
    result = a ** b
    return result


def ask_operation():
    message = '''
Please type in the math operation you would like to complete and press Enter:
+ : addition
- : subtraction
/ : division
* : multiplication
^ or ** : exponentiation
	Choose: '''

# Create list  with correct operations
    correct_operations = ['+', '-', '/', '*', '^', '**']

# Ask user for the first operation
    operation = input(message)

# Exc if user enter not existing operator
    while operation not in correct_operations:
        print('This operation is not available. Try again.')
        operation = input(message)

    return operation


def digit_check():
    try:
        i = float(input('Enter the number:\n'))
        return i
    except ValueError:
        print('It is not a number! Please, enter the number\n')
        return digit_check()


def run_calculator():
    # Ask data
    a = digit_check()
    b = digit_check()



    # Ask the type of operation
    operation = ask_operation()

    # Count numbers
    result = calculate(a, b, operation)

    # Output the result
    print(f'Result: {result}')

def calculate(a, b, operation):
    result = None

    if operation == '+':
        result = sum(a, b)
    elif operation == '-':
        result = a - b
    elif operation == '/':
        try:
            result = a / b
        except ZeroDivisionError:
            result = "As we know, division by zero is not possible"
    elif operation == '*':
        result = a * b

    # Exponentiation
    elif operation == '^' or operation == '**':
        result = exponent(a, b)

    else:
        print('Something wrong! We need a catnap\n')

    return result

run_calculator()
