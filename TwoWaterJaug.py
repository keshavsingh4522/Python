# Python3 implementation of program to count
# minimum number of steps required to measure
# d litre water using jugs of m liters and n
# liters capacity.
def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)


''' fromCap -- Capacity of jug from which
			water is poured
toCap -- Capacity of jug to which
			water is poured
d	 -- Amount to be measured '''
def Pour(toJugCap, fromJugCap, d):


	# Initialize current amount of water
	# in source and destination jugs
	fromJug = fromJugCap
	toJug = 0

	# Initialize steps required
	step = 1
	while ((fromJug is not d) and (toJug is not d)):

		
		# Find the maximum amount that can be
		# poured
		temp = min(fromJug, toJugCap-toJug)

		# Pour 'temp' liter from 'fromJug' to 'toJug'
		toJug = toJug + temp
		fromJug = fromJug - temp

		step = step + 1
		if ((fromJug == d) or (toJug == d)):
			break

		# If first jug becomes empty, fill it
		if fromJug == 0:
			fromJug = fromJugCap
			step = step + 1

		# If second jug becomes full, empty it
		if toJug == toJugCap:
			toJug = 0
			step = step + 1
			
	return step

# Returns count of minimum steps needed to
# measure d liter
def minSteps(n, m, d):
	if m> n:
		temp = m
		m = n
		n = temp
		
	if (d%(gcd(n,m)) is not 0):
		return -1
	
	# Return minimum two cases:
	# a) Water of n liter jug is poured into
	# m liter jug
	return(min(Pour(n,m,d), Pour(m,n,d)))

# Driver code
if __name__ == '__main__':

	n = 3
	m = 5
	d = 4

	print('Minimum number of steps required is',
							minSteps(n, m, d))
	
# This code is contributed by Sanket Badhe
