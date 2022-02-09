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

choices = [rock, paper, scissors]
choices_length = len(choices)
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(choices[user_choice])

comp_choice=random.randint(0 , choices_length-1)
print(f"Compute chose:{choices[comp_choice]}")

if user_choice == comp_choice:
    print("Its a tie\n")
elif user_choice == 0 and comp_choice == 2:
    print("You won")
elif user_choice == 1 and comp_choice == 0:
    print("You won")
elif user_choice == 2 and comp_choice == 1:
    print("You won")
else:
    print("You loose")
