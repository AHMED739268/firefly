# -*- coding: utf-8 -*-
"""Untitled35.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wOFwOI-rwIGHKq-2OTm57hcYe7fNAglB
"""

import numpy as np

def firefly_algorithm(objective_func, bounds, n_fireflies=50, max_iterations=100, alpha=0.2, beta_0=1.0, gamma=1.0):
    # Initialize fireflies randomly within the search space
    n_dimensions = len(bounds)
    fireflies = np.random.uniform(bounds[:, 0], bounds[:, 1], size=(n_fireflies, n_dimensions))
    brightness = np.zeros(n_fireflies)

    # Main algorithm loop
    for iteration in range(max_iterations):
        for i in range(n_fireflies):
            for j in range(n_fireflies):
                if brightness[j] > brightness[i]:
                    r = np.linalg.norm(fireflies[i] - fireflies[j])  # Euclidean distance
                    beta = beta_0 * np.exp(-gamma * r**2)  # Update attractiveness

                    # Move firefly towards brighter firefly
                    fireflies[i] += beta * (fireflies[j] - fireflies[i]) + alpha * (np.random.uniform() - 0.5)
                    fireflies[i] = np.clip(fireflies[i], bounds[:, 0], bounds[:, 1])

                    # Update brightness of moved firefly
                    brightness[i] = objective_func(fireflies[i])

        # Sort fireflies based on brightness
        sorted_indices = np.argsort(brightness)
        fireflies = fireflies[sorted_indices]
        brightness = brightness[sorted_indices]

        # Print the best firefly's fitness value at each iteration
        best_fitness = brightness[0]
        print(f"Iteration {iteration+1}: Best Fitness = {best_fitness}")

    # Return the best solution found
    best_solution = fireflies[0]
    return best_solution

# Example usage
def objective_func(x):
    # Define your objective function here
    return np.sum(x**2)

bounds = np.array([[-5, 5], [-5, 5]])  # Example bounds for a 2-dimensional problem
best_solution = firefly_algorithm(objective_func, bounds)
print("Best solution:", best_solution)
print("Best fitness:", objective_func(best_solution))

