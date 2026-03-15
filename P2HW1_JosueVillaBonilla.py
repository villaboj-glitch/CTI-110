# Josue VillaBonilla
# 15 MAR 26
# P2HW1 - Travel Expenses
# This program calculates and displays travel expenses.


print("This program calculates and displays travel expenses")
print()


budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))


remaining_balance = budget - gas - accommodation - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:,.2f}")
print(f"{'Fuel:':20}${gas:,.2f}")
print(f"{'Accommodation:':20}${accommodation:,.2f}")
print(f"{'Food:':20}${food:,.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':20}${remaining_balance:,.2f}")