# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 4 (Medium)
# Using if statements, find whether or not Rashaad Penny is in the 
# interquartile range for rushing yards (between 25th and 75th 
# percentile), in the bottom 25th percentile, or in the top 75th 
# percentile.
#
# Rashaad Penny Rushing Yards: 370 yards
# 25th percentile (2019) for all RBs for Rushing Yards: 20 yards
# 75th percentile (2019) for all RBs for Rushing Yards: 465 yards

#######################################################################
# Create a dictionary for Rashaad Penny with his stats for 2019
player = {
    "Name": "Rashaad Penny",
    "Rushing Yards": 370
}

# Assign the 25th and 75th percentile in rushing yards
percentile_25 = 20
percentile_75 = 465

# Find which percentile range Rashaad Penny lands in
rpRushingYards = player["Rushing Yards"]
if rpRushingYards <= percentile_25:
    print( player["Name"] 
           + " is in the bottom 25th percentile of RBs for rushing yards")
elif rpRushingYards > percentile_25 and rpRushingYards < percentile_75:
    print( player["Name"] 
           + " is in the interquartile range of RBs for rushing yards")
else:
    print( player["Name"] 
           + " is in the 75th percentile of RBs for rushing yards")
    
