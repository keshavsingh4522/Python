# Python implementation
# to print circle pattern

import math

# function to print circle pattern
def printPattern(radius):
	
	# dist represents distance to the center
	# for horizontal movement
	for i in range((2 * radius)+1):

		# for vertical movement
		for j in range((2 * radius)+1):
			
			dist = math.sqrt((i - radius) * (i - radius) +
				(j - radius) * (j - radius))

			# dist should be in the
			# range (radius - 0.5)
			# and (radius + 0.5) to print stars(*)
			if (dist > radius - 0.5 and dist < radius + 0.5):
				print("*",end="")
			else:
				print(" ",end="")	
	

		print()

# Driver code

radius = 6
printPattern(radius)


