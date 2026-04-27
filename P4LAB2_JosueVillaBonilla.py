# Josue VillaBonilla
# 9 APR 2026
# P4LAB2
# This program displays a multiplication table and asks the user if they want to run again.

run_again = "yes"

while run_again == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        for x in range(1, 13):
            print(number, "*", x, "=", number * x)

    else:
        print("This program does not handle negative numbers")

    run_again = input("Would you like to run the program again? ")

print("Exiting program...")