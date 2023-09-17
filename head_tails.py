import random


print("Welcome to the coin guessing game\nChoose a method to toss the coin:\n1- Using random.random()\n2- Using random.randint()")
user_choose = input("Enter your choice (1 or 2): ")
if user_choose == "1":
    pc_guess = random.random()
    if pc_guess >= 0.5:
        pc_guess = "heads"     
    else:
        pc_guess = "tails"
        

elif user_choose == "2":
    pc_guess = random.randint(0,1)
    if pc_guess == 0 :
        pc_guess = "heads"    
    else:
        pc_guess = "tails"
        
else:
    print("Wrong choice\nTry again")


user_guess = input("Enter Your Guess (heads or tails) : ").lower()
if user_guess == "heads":
    user_guess == "heads"
elif user_guess == "tails":
    user_guess == "tails"
else:
    print("Wrong choice\nTry again")

    
if user_guess == pc_guess:
    print("Congratulation! You win!")
else:
    print("Sorry, You lost!")

print(f"The computer coin toss result was: {pc_guess}")

