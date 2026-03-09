# Josue VillaBonilla
# 8 MAR 26
# Assignment Name: Dictionary MPG Program
# This program creates a dictionary of vehicles and their MPG values.
# It displays the keys, asks the user to choose a vehicle, and calculates
# how many gallons of gas are needed for a given number of miles.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()


print(keys)

car = input("Enter a vehicle to see its mpg: ")

mpg = vehicles[car]
print(f"\nThe {car} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {car}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {car} {miles:.1f} miles.")