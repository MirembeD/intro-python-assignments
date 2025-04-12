#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address: mnd5365@psu.edu
# Class: CMPSC 101
# Project #3
# Due Date: 21 February 2025 (1:30pm)
# Brief Project Description: This program calculates the shipping cost 
#and total cost of an item based on its price.
#----------------------------------------------------------


# Print the header for the program
print("==============================================================")
print("Shipping Calculator")
print("==============================================================")

# Ask the user to enter the cost of the item ordered
cost = float(input("Enter the cost of the item ordered: "))

# Check if the entered cost is negative
if cost < 0:
    print("You must enter a positive number. Please try again.")
else:
    # Determine shipping cost based on the cost of the item
    if cost >= 75:
        shipping = 0.00
    elif cost >= 50:
        shipping = 9.95
    elif cost >= 30:
        shipping = 7.95
    else:
        shipping = 5.95

    # Calculate the total cost (item cost + shipping cost)
    total = cost + shipping

    # Display the shipping cost and total cost, rounded to two decimal places
    print("Shipping cost: ${:.2f}".format(shipping))
    print("Total cost: ${:.2f}".format(total))
