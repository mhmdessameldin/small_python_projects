# welcome symbol
print("""
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗    ██╗███████╗██╗      █████╗ ███╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝    ██║██╔════╝██║     ██╔══██╗████╗  ██║██╔══██╗
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗      ██║███████╗██║     ███████║██╔██╗ ██║██║  ██║
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝      ██║╚════██║██║     ██╔══██║██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗    ██║███████║███████╗██║  ██║██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
                                                                                                                   
""")
# welcome message
print("Welcom to my island!\nThere are two doors in front of you.🟥 a red door and 🟦 a blue door")
# First Question to users
f_q = input("which door do you want to open?\n").lower()
if f_q == "red":
    print("Great! now you entered a room\nYou found three boxes: 🎁 white, 🎁 black, 🎁 green")
    box = input("which box you open?\n").lower()
    if box == "white":
        print("Oops! you opened a box filled with snackes 🐍🐍🐍")
    elif box == "black":
        print("Oops! you opened a box filled with spiders 🕷️ 🕷️ 🕷️")
    elif box == "green":
        print("congratulation! you found the treasure! 💰💰💰")
    else:
        print("Invalid choice! ⚠️ ⚠️ ⚠️")
elif f_q == "blue":
    print("Oops! You choose the crocodile door.🐊🐊🐊\nGame over!")
else:
    print("Invalid choice! ⚠️⚠️⚠️")