# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 8 (Hard)
# Calculate the passer rating for a given player using 
# the following formula:

# Passer Rating = (((comp/att) - 0.3) * 5 + ((yards/att) - 3) 
# * 0.25 + (td/att) * 20 + 2.375 - ((int/att) * 25)) / 6) * 100


########################################################
# Create a list of obj/dictionaries
players = [{
   'name': 'Josh Allen',
   'completions': 271,
   'attempts': 461,
   'yards': 3089,
   'touchdowns': 20,
   'interceptions': 9
   },
   {
   'name': 'Lamar Jackson',
   'completions': 265,
   'attempts': 401,
   'yards': 3127,
   'touchdowns': 36,
   'interceptions': 6
   },
   {
   'name': 'Tom Brady',
   'completions': 373,
   'attempts': 613,
   'yards': 4057,
   'touchdowns': 24,
   'interceptions': 8
   },
]

# Calculate passer ratings and print
for player in players:
    comp = player['completions']
    att = player['attempts']
    yards = player['yards']
    td = player['touchdowns']
    inter = player['interceptions']
    passerRating = ((((comp/att) - 0.3) * 5 + ((yards/att) - 3) * 0.25 
                 + (td/att) * 20 + 2.375 - ((inter/att) * 25)) / 6) * 100
    passerRating = round(passerRating, 1)
    print(player['name'] + " passing rating is: " + str(passerRating))
