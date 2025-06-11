#Day 4 of 100 Days of Python

# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice: list[str] = [rock, paper, scissors]

PlayerChoice = choice[int(input("Enter your choice [1] Rock [2] Paper [3] Scissors: ")) - 1]
print(f"Your Choice: \n {PlayerChoice} \n\n")

ComputerChoice =  choice[random.randint(0,len(choice) - 1)]
print(f"Computer's Choice: {ComputerChoice}")

if PlayerChoice == ComputerChoice:
    print("DRAW! Try Again!")
elif PlayerChoice == choice[0]:
    if ComputerChoice == choice[2]:
        print("Congratulations! Player Wins!")
    else:
        print("You Failed! Computer Wins!")
elif PlayerChoice == choice[1]:
    if ComputerChoice == choice[0]:
        print("Congratulations! Player Wins!")
    else:
        print("You Failed! Computer Wins!")
elif PlayerChoice == choice[2]:
    if ComputerChoice == choice[1]:
        print("Congratulations! Player Wins!")
    else:
        print("You Failed! Computer Wins!")
