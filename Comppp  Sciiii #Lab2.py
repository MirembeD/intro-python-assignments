#----------------------------------------------------------
# Name: Mirembe Ddumba
# E-mail Address: mnd5365@psu.edu
# Class: CMPSC 101
# Lab #: 2
#----------------------------------------------------------

# Constants
MOVIE_NAME = "La La Land"  # Fixed movie name
TICKET_PRICE = 6.00  
THEATER_SHARE = 0.20  

# Get user input
tickets_sold = int(input("Enter the number of tickets sold: "))

# Calculations
gross_profit = tickets_sold * TICKET_PRICE  
net_profit = gross_profit * THEATER_SHARE  
amount_to_distributor = gross_profit - net_profit  

# Revenue Report
print("\nRevenue Report")
print("=" * 26)
print(f'Movie Name: "{MOVIE_NAME}"')
print(f"Tickets Sold: {tickets_sold}")
print(f"Gross Box Office Profit: $ {gross_profit:.2f}")
print(f"Net Box Office Profit: $ {net_profit:.2f}")
print(f"Amount Paid to Distributor: $ {amount_to_distributor:.2f}")
