#Day 2 of 100 Days of Python

# We're going to build a tip calculator.
#
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay:
#
# (150.00 / 5) * 1.12 = 33.6
#
# After formatting the result to 2 decimal places = 33.60


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${((bill * (1 + tip / 100)) / 5):.2f}")

