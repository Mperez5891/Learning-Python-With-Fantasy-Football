# Author:  Manuel Perez
# Date:    09/12/2020
#
# Problem 7 (Medium)
# rushing_tds = [10, 12, 12, 6, 7, 8, 12, 15, 17]
# Sort this list in descending order using the sorted 
# built-in function. You can find more information 
# about sorted here.

# Grab the last element of the list, and the first 
# element of the list using list indexing.



########################################################
# Create a list
rushingTds = [10, 12, 12, 6, 7, 8, 12, 15, 17]

# Print original list
print("Original: " + str(rushingTds))

# Sort the list
rushingTds.sort(key = None, reverse = True)

# Show the list in reverse order
print("Reversed: " + str(rushingTds))

# Print the the max and min
print("Max: " + str(rushingTds[0]))
print("Min: " + str(rushingTds[-1]))
