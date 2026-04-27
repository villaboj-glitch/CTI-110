# Josue VillaBonilla
# 26 APR 26
# P5LAB
# This program simulates a self-checkout machine. It generates a random
# amount owed, asks the user for payment, and displays the change.

import random

# Function to break change into dollars and coins
def disperse_change(amount):
    total_cents = int(round(amount * 100))

    if total_cents == 0:
        print("No change")
    else:
        dollars = total_cents // 100
        total_cents = total_cents % 100

        quarters = total_cents // 25
        total_cents = total_cents % 25

        dimes = total_cents // 10
        total_cents = total_cents % 10

        nickels = total_cents // 5
        total_cents = total_cents % 5

        pennies = total_cents

        if dollars > 0:
            if dollars == 1:
                print("1 Dollar")
            else:
                print(f"{dollars} Dollars")

        if quarters > 0:
            if quarters == 1:
                print("1 Quarter")
            else:
                print(f"{quarters} Quarters")

        if dimes > 0:
            if dimes == 1:
                print("1 Dime")
            else:
                print(f"{dimes} Dimes")

        if nickels > 0:
            if nickels == 1:
                print("1 Nickel")
            else:
                print(f"{nickels} Nickels")

        if pennies > 0:
            if pennies == 1:
                print("1 Penny")
            else:
                print(f"{pennies} Pennies")


# Main function
def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = cash - amount_owed
    print(f"Change is: ${change:.2f}\n")

    disperse_change(change)


# Call main
main()