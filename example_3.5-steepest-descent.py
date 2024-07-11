#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:13:09 2024

@author: DrData
"""
import numpy as np
import sympy as sp

# Define the symbolic variables
x1, x2 = sp.symbols('x1 x2')

# Define the function f
f = 10*x1**2 + 5*x1*x2 + 10*(x2 - 3)**2

# Compute the gradient of f
df_dx1 = sp.diff(f, x1)
df_dx2 = sp.diff(f, x2)

# Define the steepest descent method
def steepest_descent(x0, tol=1e-6, max_iter=10000):
    x = np.array(x0)
    iteration = 0
    while True:
        # Compute the gradient at the current point
        grad = np.array([float(df_dx1.subs({x1: x[0], x2: x[1]})),
                        float(df_dx2.subs({x1: x[0], x2: x[1]}))])
        
        # Compute the step size using the backtracking line search
        alpha = 1.0
        while True:
            x_new = x - alpha * grad
            if x_new[0] >= -10 and x_new[0] <= 10 and x_new[1] >= -15 and x_new[1] <= 15:
                if f.subs({x1: x[0], x2: x[1]}) - f.subs({x1: x_new[0], x2: x_new[1]}) >= 0.5 * alpha * np.dot(grad, grad):
                    break
            alpha *= 0.5
        
        # Update the current point
        x = x_new
        
        # Check the stopping criterion
        if np.linalg.norm(grad) < tol:
            break
        
        iteration += 1
        if iteration >= max_iter:
            break
    
    return x

# Run the steepest descent method with the initial point (10, 15)
x0 = np.array([10, 15])
x_opt = steepest_descent(x0)

print(f"The optimal solution is: {x_opt}")
print(f"The minimum value of the function is: {float(f.subs({x1: x_opt[0], x2: x_opt[1]}))}")
