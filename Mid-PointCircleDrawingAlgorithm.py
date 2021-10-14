# program for implementing
# Mid-Point Circle Drawing Algorithm

def midPointCircleDraw(x_centre, y_centre, r):
	x = r
	y = 0
	
	# Printing the initial point the
	# axes after translation
	print("(", x + x_centre, ", ",
			y + y_centre, ")",
			sep = "", end = "")
	
	# When radius is zero only a single
	# point be printed
	if (r > 0) :
	
		print("(", x + x_centre, ", ",
				-y + y_centre, ")",
				sep = "", end = "")
		print("(", y + x_centre, ", ",
				x + y_centre, ")",
				sep = "", end = "")
		print("(", -y + x_centre, ", ",
					x + y_centre, ")", sep = "")
	
	# Initialising the value of P
	P = 1 - r

	while x > y:
	
		y += 1
		
		# Mid-point inside or on the perimeter
		if P <= 0:
			P = P + 2 * y + 1
			
		# Mid-point outside the perimeter
		else:		
			x -= 1
			P = P + 2 * y - 2 * x + 1
		
		# All the perimeter points have
		# already been printed
		if (x < y):
			break
		
		# Printing the generated point its reflection
		# in the other octants after translation
		print("(", x + x_centre, ", ", y + y_centre,
							")", sep = "", end = "")
		print("(", -x + x_centre, ", ", y + y_centre,
							")", sep = "", end = "")
		print("(", x + x_centre, ", ", -y + y_centre,
							")", sep = "", end = "")
		print("(", -x + x_centre, ", ", -y + y_centre,
										")", sep = "")
		
		# If the generated point on the line x = y then
		# the perimeter points have already been printed
		if x != y:
		
			print("(", y + x_centre, ", ", x + y_centre,
								")", sep = "", end = "")
			print("(", -y + x_centre, ", ", x + y_centre,
								")", sep = "", end = "")
			print("(", y + x_centre, ", ", -x + y_centre,
								")", sep = "", end = "")
			print("(", -y + x_centre, ", ", -x + y_centre,
											")", sep = "")
							
# Driver Code
if __name__ == '__main__':
	
	# To draw a circle of radius 3
	# centred at (0, 0)
	midPointCircleDraw(0, 0, 3)

