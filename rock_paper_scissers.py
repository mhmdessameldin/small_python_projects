import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list = ["rock", "paper", "scissors"]
print("\nWelcome to the Rock, Paper, Scissors game:")

first = input("Press Enter to continue or type (Help) for the rule ").lower()
if first == "help":
  print("""
        *********** Rules **********
        1) You choose and the computer chooses
        2) Rock brocken Scissors -> Rock wins
        3) Scissors cut Paper -> Scissors win
        4) Paper covers Rock -> Paper win
  """)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice not in list:
  print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")

else:

  if user_choice == "rock":
    print("\nYou chose :")
    print(rock)
  elif user_choice == "paper":
    print(f"\nYou chose :\n{paper}")
  else:
    print(f"\nYou chose :\n{scissor}")

    
  computer_choice = random.choice(list)
  if computer_choice == "rock":
    print("\nYou chose :\n", rock)
  elif computer_choice == "paper":
    print("\nYou chose :\n", paper)
  else:
    print("\nYou chose :\n", scissor)


  if user_choice == computer_choice:
    print("It is a tie")
    
  elif (
       (user_choice == "rock" and computer_choice == "scissor")
       or
       (user_choice == "paper" and computer_choice == "rock")
       or
       (user_choice == "scissor" and computer_choice == "paper")
    ):
       print("You win, You beats ", computer_choice)

  else:
       print("You lose, Computer beats ", user_choice)

