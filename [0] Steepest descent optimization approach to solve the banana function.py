#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:23:43 2024

@author: DrData

In fact, Rosenbrock’s banana function is a very tough test function for optimization algorithms. Its solution requires more elaborate methods, and we will
discuss some of these methods in later chapters.

This code implements the steepest descent method to minimize the Rosenbrock’s banana function `f(x1, x2) = (1 - x1)^2 + 100(x2 - x1^2)^2`. The key steps are:

1. Define the banana function and its gradient.
2. Implement the steepest descent algorithm, which iteratively updates the solution based on the negative gradient direction.
3. Plot the function contours and the optimization trajectory to visualize the minimization process.

The code starts with an initial guess `x0 = [-1.2, 1]` and finds the minimum solution, which is printed to the console. The final function value at the minimum is also displayed.

The resulting plot shows the contours of the banana function, with the minimum solution marked as a red dot and the optimization trajectory plotted as a white line.

"""

import numpy as np
import sympy as sp



def banana_function(x1, x2):
    return (1 - x1)**2 + 100 * (x2 - x1**2)**2


def gradient_banana_function(x1, x2):
    # Define the variables
    x1, x2 = sp.symbols('x1 x2')
    
    # Define the function
    f = (1 - x1)**2 + 100 * (x2 - x1**2)**2
    
    # Calculate the partial derivative with respect to x1
    df_dx1 = sp.diff(f, x1)
    
    # Calculate the partial derivative with respect to x2
    df_dx2 = sp.diff(f, x2)
    
    return df_dx1, df_dx2



x1, x2 = sp.symbols('x1 x2')
df_dx1,df_dx2=gradient_banana_function(x1,x2)

# Solve the system of equations
solution = sp.solve([df_dx1, df_dx2], [sp.Symbol('x1'), sp.Symbol('x2')], dict=True)
#solution
#Out[41]: [{x1: 1, x2: 1}]

# Print the solutions
print("Solutions:")
for sol in solution:
    x1_value = float(solution[0][sp.Symbol('x1')])
    x2_value = float(solution[0][sp.Symbol('x2')])
    print(f"x1 = {sol[sp.Symbol('x1')]}")
    print(f"x2 = {sol[sp.Symbol('x2')]}")


df_dx1_num = float(df_dx1.subs([(sp.Symbol('x1'), x1_value), (sp.Symbol('x2'), x2_value)]))
df_dx2_num = float(df_dx2.subs([(sp.Symbol('x1'), x1_value), (sp.Symbol('x2'), x2_value)]))

grad=[df_dx1_num, df_dx2_num]


# Example usage
x0 = [5, 5]
#lest use 
x1_value=5
x2_value=5
df_dx1_num = float(df_dx1.subs([(sp.Symbol('x1'), x1_value), (sp.Symbol('x2'), x2_value)]))
df_dx2_num = float(df_dx2.subs([(sp.Symbol('x1'), x1_value), (sp.Symbol('x2'), x2_value)]))




# Given values
df_dx1_num = 40008.0
df_dx2_num = -4000.0
x10 = 5
x20 = 5

# Define the variables
step_size, x11, x21 = sp.symbols('step_size x11 x21')

# Define the equations
eq1 = x11 - x10 + step_size * df_dx1_num
eq2 = x21 - x20 + step_size * df_dx2_num
eq3 = (1 - x11)**2 + 100 * (x21 - x11**2)**2

# Solve the system of equations
solutions = sp.solve([eq1, eq2, eq3], [step_size, x11, x21], dict=True)

# Print the solutions
for soln in solutions:
    print(f"step_size = {soln[step_size]}")
    print(f"x11 = {soln[x11]}")
    print(f"x21 = {soln[x21]}")


"""
step_size = 6.76038997140386e-5 - 6.90235756670606e-7*I
x11 = 2.29530318024074 + 0.0276149521528776*I
x21 = 5.27041559885615 - 0.00276094302668243*I
step_size = 6.76038997140386e-5 + 6.90235756670606e-7*I
x11 = 2.29530318024074 - 0.0276149521528776*I
x21 = 5.27041559885615 + 0.00276094302668243*I
step_size = 0.000184845110583882 - 1.8092643433094e-6*I
x11 = -2.39528318423994 + 0.0723850478471224*I
x21 = 5.73938044233553 - 0.00723705737323759*I
step_size = 0.000184845110583882 + 1.8092643433094e-6*I
x11 = -2.39528318423994 - 0.0723850478471224*I
x21 = 5.73938044233553 + 0.00723705737323759*I
"""

# step_size ~ 0.00006761..,6.76038997140386e-5,0.000184845110583882  #similar to the book....


#calculating the modulus of the solutions:
# Previous solutions
step_size_1 = 6.76038997140386e-5 - 6.90235756670606e-7j
x11_1 = 2.29530318024074 + 0.0276149521528776j
x21_1 = 5.27041559885615 - 0.00276094302668243j

step_size_2 = 6.76038997140386e-5 + 6.90235756670606e-7j
x11_2 = 2.29530318024074 - 0.0276149521528776j
x21_2 = 5.27041559885615 + 0.00276094302668243j

step_size_3 = 0.000184845110583882 - 1.8092643433094e-6j
x11_3 = -2.39528318423994 + 0.0723850478471224j
x21_3 = 5.73938044233553 - 0.00723705737323759j

step_size_4 = 0.000184845110583882 + 1.8092643433094e-6j
x11_4 = -2.39528318423994 - 0.0723850478471224j
x21_4 = 5.73938044233553 + 0.00723705737323759j

# Calculate the modulus
step_size_1_modulus = np.abs(step_size_1)
x11_1_modulus = np.abs(x11_1)
x21_1_modulus = np.abs(x21_1)

step_size_2_modulus = np.abs(step_size_2)
x11_2_modulus = np.abs(x11_2)
x21_2_modulus = np.abs(x21_2)

step_size_3_modulus = np.abs(step_size_3)
x11_3_modulus = np.abs(x11_3)
x21_3_modulus = np.abs(x21_3)

step_size_4_modulus = np.abs(step_size_4)
x11_4_modulus = np.abs(x11_4)
x21_4_modulus = np.abs(x21_4)

# Print the results
print("Solution 1:")
print(f"step_size: {step_size_1_modulus}")
print(f"x11: {x11_1_modulus}")
print(f"x21: {x21_1_modulus}")

print("\nSolution 2:")
print(f"step_size: {step_size_2_modulus}")
print(f"x11: {x11_2_modulus}")
print(f"x21: {x21_2_modulus}")

print("\nSolution 3:")
print(f"step_size: {step_size_3_modulus}")
print(f"x11: {x11_3_modulus}")
print(f"x21: {x21_3_modulus}")

print("\nSolution 4:")
print(f"step_size: {step_size_4_modulus}")
print(f"x11: {x11_4_modulus}")
print(f"x21: {x21_4_modulus}")

"""
Solution 1:
step_size: 6.760742327544791e-05
x11: 2.2954692929345977
x21: 5.270416322025484

Solution 2:
step_size: 6.760742327544791e-05
x11: 2.2954692929345977
x21: 5.270416322025484

Solution 3:
step_size: 0.00018485396491347308
x11: 2.3963766665227015
x21: 5.739385005108387

Solution 4:
step_size: 0.00018485396491347308
x11: 2.3963766665227015
x21: 5.739385005108387
"""

#Whichever these values we use, the new iteration x(1)2 = x2 + 4000𝛼0 is always (0) 
#greater that x2 = 5, which moves away from the best solution (1, 1).
# In this case, the simple steepest descent method does not work well.
# We have to use other more elaborate methods such as the conjugate gradient method.


#PLOT

import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

# Generate a grid of x1 and x2 values
x1 = np.linspace(-5, 5, 50)
x2 = np.linspace(-5, 5, 50)
X1, X2 = np.meshgrid(x1, x2)

# Calculate the function values
f = (1 - X1)**2 + 100 * (X2 - X1**2)**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, f, cmap='viridis')

# Set labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')
ax.set_title('Plot of Rosenbrock’s banana function\n f = (1 - x1)^2 + 100 * (x2 - x1^2)^2')

plt.show()
