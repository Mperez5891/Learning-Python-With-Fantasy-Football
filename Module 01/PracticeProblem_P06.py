# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 6 (Very Hard)
# For each player in the program you created above, write 
# a program that finds the player with the max rushing 
# yards. You should still store player data in a list 
# of dictionaries.
#
# You should leverage for and if here. I'll offer an 
# alternative solution in the problem_6.py file as there 
# are multiple ways to go about this problem.


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

# Find the RB with the most rushing yards
maxRushingYards = 0
maxRushingYardsPlayer = ""
for player in players:
    if player['RushingYards'] > maxRushingYards:
        maxRushingYards = player['RushingYards']
        maxRushingYardsPlayer = player['Name']
        
# Print the RB with the most rushing yards
print(maxRushingYardsPlayer + " had the most rushing yards with " 
      + str(maxRushingYards))
