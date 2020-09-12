# Author:  Manuel Perez
# Date:    09/11/2020
#
# Problem 1 (Easy)
# Tyler Lockett had the following stat line for 2019.
# 69 receptions, 82 targets, 1057 receiving yards, 8 
# receiving touchdowns.
# Using Python, print Lockett's catch rate and fantasy 
# points scored for 2019.

########################################################
# Create a dictionary for Tyler Lockett with his stats
# for 2019
player = {
    "Name": "Tyler Lockett",
    "Receptions": 69,
    "Targets": 82,
    "Receiving yards": 1057,
    "Receiving Touchdowns": 8
}

# Calculate Lockett's catch rate
catches = player["Receptions"]
targets = player["Targets"]
lockettsCatchRate = round(catches / targets, 3);

# Calculate Lockett's fantasy points scored
yards = player["Receiving yards"]
tds = player["Receiving Touchdowns"]
lockettsFantasyPoints = catches + (yards * 0.1) + (tds * 6)

# Print Lockett's catch rate and fantasy points scored 
# for 2019
print(player["Name"] + "'s catch rate was: " 
      + str(lockettsCatchRate))
print(player["Name"] + "'s fantasy points was: " 
      + str(lockettsFantasyPoints))
