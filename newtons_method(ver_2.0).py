#Created by Kenneth (Alex) Jenkins
#Date: 12/06/2022
# Version 2.0

# CHANGE CATALOG
"""
NEW IN VERSION 2.0:
  Added a welcome message
  Added change catelog
  Added an interation counter
  Added a check for a negative derivative, with a break if the derivative is 0
  Added a message to tell the user how to input the function
  Added inital guess support
  Switched from using a user defined derivative function to the limit definition of the derivative
  Cleaned up the code and added much needed documentation


TO DO:
  add support for multiple roots
  add support for nonpolynomial functions
    such as sin(x), cos(x), tan(x), etc.
  more code cleanup
"""

print("Welcome to the Newton's Method Calculator! ")
print("This program was created by: Kenneth (Alex) Jenkins, for Dr. Christopher Raridan's Math 1501 at Clayton State University.")
print("Please input your function in the form of \"x**3 - 2*x**2 + 3*x - 4\" without the quotes.")

func = input("Enter your function: ")
# Define a user-defined function
def f(x):
    # Evaluate the function using the user inputted function
    f = eval(func)
    # Return the value of the function
    return f

# Calculate the derivative of the user inputted function
def derivative(f, x, h=1e-10):
    # Calculate the derivative using the limit definition of the derivative
  return (f(x + h) - f(x)) / h


# Define the Newton's method function
def newton(f, omega, maximum_iteratons=100, tolerance=1e-10):
  #tolerance is the maximum allowed error of the root
  count = 0
  x = omega
  # omega is the initial guess

  # Check if the derivative is 0
  if derivative(f, x) == 0:
    print("WARNING! The derivative of the function is 0 at the inital guess!")
    print("Try again with a different inital guess")
    return None
    # If the derivative is 0, return None
    # else, continue

  # Iterate until we reach the maximum number of iterations or the tolerance
  for i in range(maximum_iteratons):
    zeta = x - f(x) / derivative(f, x)
    # Calculate the next value of x using Newton's method
    count = count + 1
    # Increment the iteration counter

    # Check if we have reached the tolerance
    if abs(zeta - x) < tolerance:
        # If we have reached the tolerance, return the value of x
      print("Took {count} iteration(s) to complete".format(count=count))
        # Print the number of iterations it took to complete
      return zeta

      # Update the value of x
    x = zeta

  # If we have reached the maximum number of iterations, return the last value of x
  return x


# Get the initial guess from the user
omega = float(input("Enter an initial guess for the root: "))

# Calculate the root of the function
root = newton(f, omega)
print("A root of function is: ", root)  # Prints a root of the function