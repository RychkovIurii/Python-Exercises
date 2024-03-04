def guess_input():
    tries = 0
    number = int(input("Enter number: "))
    while True:
        guess = int(input("Enter a guess: "))
        tries += 1
        if (guess == number):
            break
        elif (guess < number):
            print("it is more")
        else:
            print("it is less")
    print("Number of tries needed:")
    print(tries)

guess_input()