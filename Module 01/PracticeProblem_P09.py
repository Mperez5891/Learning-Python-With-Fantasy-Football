# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 9 (Easy)
# Explore Python's built in functions. Find the max and min of this 
# list of numbers using Python's built-in functions. Also find the 
# difference between the min and max, known as the range. As an 
# added bonus, try to find the min and max without using any 
# built-in functions.
# 
# list_obj = [1, 2, 3, 56, 12, 23, 34, 12, 89, 90, 345, 67, 56, 34]

####################################################################
# Given list
listObj = [1, 2, 3, 56, 12, 23, 34, 12, 89, 90, 345, 67, 56, 34]
print("Original List: " + str(listObj))

# Find max and min
maxNum = max(listObj)
minNum = min(listObj)
print("Max: " + str(maxNum))
print("Min: " + str(minNum))

# Find the range
range = maxNum - minNum
print("Range: " + str(range))
