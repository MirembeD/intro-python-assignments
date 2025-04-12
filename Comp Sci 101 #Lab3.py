#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address: mnd5365@psu.edu
# Class: CMPSC 101
# Lab #: 3
#----------------------------------------------------------

# Ask the user for the month, day, and year (in two-digit format)
month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day of the month: "))
year = int(input("Enter the year in two-digit format: "))

# Display the entered date in the required format
print(f"The date is {month} /{day} /{year}.")

# Check if the month multiplied by the day equals the year
if month * day == year:
    print("This is a magic date.")
else:
    print("This is not a magic date.")


