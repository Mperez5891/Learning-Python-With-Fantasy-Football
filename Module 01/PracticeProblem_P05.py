# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 5 (Easy)
# Write a program that calculates yards per carry for 3 
# three top running backs. Store the player data in a 
# list of dictionaries, where each dictionary corresponds 
# to a separate player. Iterate over each dictionary 
# using a for loop.

########################################################
# Create a list of dictionaries for 3 running backs.
# Get their rushing attempted and total rushing yards
# for 2019 season
players = [{
   'Name': "Derrick Henry",
   'RushingYards': 1540,
   'RushingAttempted': 303
   },
   {
   'Name': "Ezekiel Elliott",
   'RushingYards': 1357,
   'RushingAttempted': 301
   },
   {
   'Name': "Nick Chubb",
   'RushingYards': 1494,
   'RushingAttempted': 298
   },
]

# Calculate yards per carry
for player in players:
    name = player['Name']
    yardsPerCarry = round(player['RushingYards'] 
                          / player['RushingAttempted'], 3)
    print( name + "'s yards per carry was: " + str(yardsPerCarry))
