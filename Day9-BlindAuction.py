# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
DataBase = {}
Highest = 0
while True:
    name = input("What is your name: ")
    bid = int(input("Enter your bid: "))

    # Store the data in nested format
    DataBase[name] = {"Price": bid}
    if (bid > Highest):
        Highest = bid
        Winner = name
    act = input("Are there other bidders? [Y/N]: ")
    if act.lower() != 'y':
        break

    print("\n" * 20)

print(f"The winner is {Winner} with a bid of ${Highest}")