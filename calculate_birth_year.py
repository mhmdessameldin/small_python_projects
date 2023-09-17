# print ("Current date and time is = %s" % dt)
# print (f"Current date and time is = {dt}")
# print ("Date and time in ISO Format = %s" % dt.isoformat())
# print ("Current year = %s" %dt.year)
# print ("Current month is = %s" %dt.month)
# print ("Current date (day) = %s" %dt.day )
# print(type(birthday))
# print(type(today_year))

# # Import library
import datetime

# # Birthday question
# birthday = input("How old are you? \n")
# birthday = int(birthday) # convert type to integer

# # Calculate today year
# dt = datetime.datetime.now()
# today_year = dt.year
# user_birth_year = today_year - birthday

# # User message
# print(f"You were born in the year {user_birth_year}")

# number = input("Please enter two digits : \n")
# first_num = number[0]
# second_num = number[1]
# print(int(first_num) + int(second_num))

second = int(input("Enter the duratuin in seconds"))

minutes = second % 60
hours = second / 60

print(minutes, "minutes")
print(hours, "hours")
