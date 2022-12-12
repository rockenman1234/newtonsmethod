## Newton's method for finding square roots
## By Alex Jenkins for Dr. Christopher Raridan's Math 1501 Calculus 1 class

def newtonsmethod(func, funcderiv, x, n):

    def f(x):
        f = eval(func)
        # This takes in the user's function and evaluates it
        return f
        # This returns the value of the function

    def df(x):
        df = eval(funcderiv)
        # This takes in the user's function's derivative and evaluates it
        return df

    for itercept in range(1, n):
        i = x - (f(x)/df(x))
        x = i
    print(f"the root was found to at {x} after {n} iterations")


print ("Welcome to Newton's method for finding square roots!")
print ("Made by Alex Jenkins for Dr. Christopher Raridan's Math 1501 Calculus 1 Class")

# Asks user for the function and its derivative
func = input("Please enter the function you would like to find the root of: ")
funcderiv = input("Please enter the derivative of the function: ")

# Asks user for the initial guess and the number of iterations
x = float(input("Please enter the initial guess: "))
n = int(input("Please enter the number of iterations: "))
newtonsmethod(func, funcderiv, x, n)

