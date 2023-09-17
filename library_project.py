print("Welcome to your library")
name = input("What is your name? ").upper()
if name:
    print(f"Hello {name}")
else:
    print("Please Enter your name")

Your_library = []
wish_list = []
first_book = input("Enter the name of a book you own : ").lower()
Your_library.append(first_book)
second_book = input("Enter the name of another book you own (or press 'Enter' to skip) : ").lower()
if second_book:
    Your_library.append(second_book)
print(f"Your Library: {Your_library}")


first_wish = input("Enter the name of a book you wish to have in the future: ").lower()
wish_list.append(first_wish)
second_wish =  input("Enter the name of another book you wish (or press 'Enter' to skip) : ").lower()
if second_wish:
    wish_list.append(second_wish)
print(f"Your wishlist: {wish_list}")


wish_acquired = input("Enter the name of a book from your wishlist that you have owned (or press 'Enter' to skip) : ")
if wish_acquired in wish_list:
    Your_library.append(wish_acquired)
    wish_list.remove(wish_acquired)
print(f"Updated library: {Your_library}\nUpdated wishlist: {wish_list}")


donate_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip) :")
if donate_book in Your_library:
    Your_library.remove(donate_book)
print("final library after Donations: ", Your_library)
