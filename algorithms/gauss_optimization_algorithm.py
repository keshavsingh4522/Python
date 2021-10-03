# The Gaussian method (coordinate descent method) refers to zero-order methods in which only
# the value of the function Q(X) at different points in the space of variables is used 
# to organize the search for the extremum. This reduces the overall computational cost of
# finding the extremum. Also in the Gaussian method, the procedures for finding and moving
# the operating point are simplified as much as possible.

# This is desctiption of the function. x1 and x2 are limitations
# of the cordinates where optimum may be found.
f = lambda x1, x2: 0 if x1 > 1 or x1 < 0 or x2 > 1 or x2 < 0 else a0 + a1 * x1 + a2 * x2 + a3 * x1 * x2 + a4 * x1 * x1 + a5 * x2 * x2

# Below is declaration of the constants that are used in the function
a0 = 0.3
a1 = 0.6
a2 = 2.6
a3 = 0.3
a4 = 0.2
a5 = 1.4

# This parameters identifies how much step size will be decreased each iteration.
N = 2.4

# This is min and max value for each coordinates. This is used to specify
# the range where optimum should be found.
x1_min, x1_max = 0, 1
x2_min, x2_max = 0, 1

# Default values of x1 and x2. These values will be used for calculation of the next coordinates
# by Gauss optimization method
x1, x2 = 0.5, 0.5

# This is default step
step = 0.5

# This value is used to control accuracy of the optimization. In case if error is less than eps,
# optimization will be stopped
eps = 0.1 ** 100

# Initial value of the error
error = 1

# Initial data that is used in caluclation
data = [x1, x2, f(x1, x2)]

# Implementation of the Gauss optimization algorithm
while abs(error) > eps: 
  # Calculation of the function in coordinates that are gotten with shift 
  bottom = f(x1, x2 - step)
  top = f(x1, x2 + step)
  left = f(x1 - step, x2)
  right = f(x1 + step, x2)

  # Calculation of the best option.   
  max_value = max(bottom, top, left, right)
  # Caluclation of the error    
  error = max_value - f(x1, x2)

  # Change of the coordinates to the best option
  if max_value == bottom:
    x2 -= step
  elif max_value == top:
    x2 += step
  elif max_value == left:
    x1 -= step
  elif max_value == right:
    x1 += step

  # Change of the step  
  step /= N

  # Storing of the data for next iteration
  data = [x1, x2, f(x1, x2)]
  
# Output of the results
print("х1:", x1, "x2:", x2)