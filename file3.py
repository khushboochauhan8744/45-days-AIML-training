# Even or Odd Checker

# int() converts a string into an integer.
# If we try int("abc"), Python gives a ValueError
# because "abc" is not a valid number.

try:
    number = int(input("Enter a number: "))

    if number == 0:
        print("The number is zero.")
    elif number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Invalid input! Please enter a valid number.")