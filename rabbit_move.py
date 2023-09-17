print("Welcome to place the rabbit")
play_1 = ["🎄", "🎄", "🎄"]
play_2 = ["🎄", "🎄", "🎄"]
play_3 = ["🎄", "🎄", "🎄"]

print(play_1)
print(play_2)
print(play_3)

Questions = input("Where should the rabbit go? 🐇\nPlease choose a row and a column ")
if Questions[0] == "1":
  column = int(Questions[1])-1
  play_1.remove("🎄")
  play_1.insert(column, "🐇")

  print(play_1)
  print(play_2)
  print(play_3)

elif Questions[0] == "2":
  column = int(Questions[1])-1
  play_2.remove("🎄")
  play_2.insert(column, "🐇")

  print(play_1)
  print(play_2)
  print(play_3)

elif Questions[0] == "3":
  column = int(Questions[1])-1
  play_3.remove("🎄")
  play_3.insert(column, "🐇")

  print(play_1)
  print(play_2)
  print(play_3)