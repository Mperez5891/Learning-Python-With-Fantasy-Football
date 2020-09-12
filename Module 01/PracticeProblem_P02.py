# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 2 (Medium)
# Visit this URL and find Michael Thomas's receiving 
# yards for 2019. Input each weeks receiving yards in 
# to an ordered list, and find the average of the list 
# using Python's built in functions len and sum. Both 
# of these functions can be found in the Python docs.

# Print out MT's average receiving yards for 2019 using 
# the print function.

# URL: 
# https://www.pro-football-reference.com/players/T/ThomMi05/gamelog/2019/

#########################################################################
# Make a list of Michael Thomas's receiving yards each week
mTReceivingYardsList = [ 123, 89, 54, 95, 182, 89, 131, 112, 152, 114, 
                         101, 48, 134, 128, 136, 37 ]

# Find the average of the list
average = sum(mTReceivingYardsList) / len(mTReceivingYardsList)

# Print the average of receiving yards per week
print("Michael Thomas's average receiving yards per week was: " 
      + str(average))
