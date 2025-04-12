#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address: mnd5365@psu.edu
# Class: CMPSC 101
# Lab #: 5
#----------------------------------------------------------

print("The Miles Per Gallon application")
print("------------------------------------------")
choice = "y"
while choice.lower() == "y":
    # Get user inputs and convert them to floats
    miles = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons of gas used: "))
    cost_per_gallon = float(input("Enter cost per gallon: "))
    
    # Calculate miles per gallon and total gas cost
    mpg = miles / gallons
    total_cost = gallons * cost_per_gallon
    
    # Display results rounded to two decimal places
    print("Miles Per Gallon:", round(mpg, 2))
    print("Total Gas Cost:", round(total_cost, 2))
    
    # Ask if the user wants to enter another trip
    choice = input("Get entries for another trip (y/n)? ")

print("Bye")
