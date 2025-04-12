#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address:mnd5365@psu.edu
# Class: CMPSC 101
# Lab #: 4
#----------------------------------------------------------

# Program to determine today's day and the future day

# Prompt the user for today's day (0 for Sunday, 1 for Monday, ..., 6 for Saturday)
today = int(input("Enter today's day (Sunday is 0, Monday is 1 ..., and Saturday is 6): "))

# Determine the name of today's day using basic if/elif statements
if today == 0:
    today_name = "Sunday"
elif today == 1:
    today_name = "Monday"
elif today == 2:
    today_name = "Tuesday"
elif today == 3:
    today_name = "Wednesday"
elif today == 4:
    today_name = "Thursday"
elif today == 5:
    today_name = "Friday"
elif today == 6:
    today_name = "Saturday"

print("Today is " + today_name + ".")

# Prompt the user for the number of days elapsed since today
days_elapsed = int(input("Enter the number of days elapsed since today: "))

# Calculate the future day's number using the modulo operator
future_day_number = (today + days_elapsed) % 7

# Determine the future day name with similar if/elif statements
if future_day_number == 0:
    future_day_name = "Sunday"
elif future_day_number == 1:
    future_day_name = "Monday"
elif future_day_number == 2:
    future_day_name = "Tuesday"
elif future_day_number == 3:
    future_day_name = "Wednesday"
elif future_day_number == 4:
    future_day_name = "Thursday"
elif future_day_number == 5:
    future_day_name = "Friday"
elif future_day_number == 6:
    future_day_name = "Saturday"

print("The future day is " + future_day_name + ".")
