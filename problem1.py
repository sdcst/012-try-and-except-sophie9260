#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')

a = input("Enter a number for the value of A for a quadratic equation in the format: ax^2 + bx + c = 0: => ")

b = input("Enter a number for the value B => ")

c = input("Enter a number for the value C => ")

try:
  a = float(a)
  b = float(b)
  c = float(c)
  try:
    sr = ((b**2) - (4*a*c))**0.5
    tp = -(b) + sr
    x = tp/(2*a)
    x = round(x,2)
  
    sr = ((b**2) - (4*a*c))**0.5
    tp = -(b) - sr
    xx = tp/(2*a)
    xx = round(xx,2)

    print(f"The roots are {x} and {xx}")
  
  except:
    print("There are no real roots to the equation.")

except:
  print("Those are not valid values for a, b, c.")

