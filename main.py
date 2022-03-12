import random
import string

name = input("Enter your name: ")
print('Welcome to Password Generator!', name)


def passrandom():
    # get the length of password from user
    length = int(input("\nEnter password length: "))

    # define data
    letter = string.ascii_letters
    digits = string.digits
    symbol = "!@#$%^&*"

    # Composite define data
    add = letter + digits + symbol

    # Assign the value temp
    temp = random.sample(add, length)

    # Create the password
    password = "".join(temp)

    print(password)


# Call the function
passrandom()
