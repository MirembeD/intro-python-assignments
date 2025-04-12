#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address: mnd5365@psu.edu
# Class: CMPSC 101
# Project # 2
# Due Date: Friday, February 7, 2025 (1:25 p.m.)
# Brief Project Description: This program calculates the 
# balance of a bank account after compound interest is applied
# for a specified number of years.
#----------------------------------------------------------

# Explain the program to the user
print("This program calculates the ending principal in a bank account after compounding the interest.")

# Ask the user for input values
principal = float(input("Enter the starting principal: "))  # Initial deposit
annual_rate = float(input("Enter the annual interest rate: "))  # Interest rate in percentage
compounds_per_year = int(input("How many times per year is the interest compounded? "))  # Compounding frequency
years = int(input("For how many years will the account earn interest? "))  # Number of years

# Convert the annual interest rate from percentage to a decimal
annual_rate = annual_rate / 100

# Use the compound interest formula to calculate the final amount
final_amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)

# Display the result, rounded to two decimal places
print("At the end of", years, "years, you will have $", round(final_amount, 2))
