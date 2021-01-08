# Kyle Bautista (AMDG) 12/17/20

from random import randint

num1 = randint(0, 50)

while True:
    num2 = input("Pick a number between 0 and 50, which one am I thinking? ")

    if num2 == "stop":
        print("The number was {0}.".format(num1))
        break

    if num2.isdigit():
        num3 = int(num2)
    else:
        print("Enter a number:")
        continue

    if num3 > num1:
        print("Lower")
    elif num3 < num1:
        print("Higher")
    else:
        print("You guessed {0}. That is correct".format(num3))
        break
