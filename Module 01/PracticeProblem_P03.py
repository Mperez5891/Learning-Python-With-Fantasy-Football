# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 3 (Very Hard)
# Using the list above, find the standard deviation of Michael 
# Thomas's receiving yards. This is how you calculate the standard 
# deviation: For each element in the list, subtract away the mean of 
# the list, and square the difference for each of these intermediary 
# calculations. Set these numbers to the side. Once you are finish 
# iterating this operation, sum up all of the results, and divide by 
# the length of the list (the number of observations). Find out more 
# information about standard deviation here.

# Finally, take the square root of that number (that number is actually 
# the variance). This is your standard deviation.

#######################################################################
# Make a list of Michael Thomas's receiving yards each week
mtReceivingYardsList = [ 123, 89, 54, 95, 182, 89, 131, 112, 152, 114, 
                         101, 48, 134, 128, 136, 37 ]

# Find the average of the list
mtAverage = sum(mtReceivingYardsList) / len(mtReceivingYardsList)

# Calculate the sum of the squared difference
summedSqrStdDev = 0
for yards in mtReceivingYardsList:
    summedSqrStdDev += (yards - mtAverage)**2
    
# Calculate the std dev
variance = summedSqrStdDev / len(mtReceivingYardsList)
mtStdDev = round(variance**(1/2), 3)

print("Michael Thomas's std dev was: "+ str(mtStdDev))
