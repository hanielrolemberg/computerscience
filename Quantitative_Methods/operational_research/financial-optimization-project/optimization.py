from scipy.optimize import linprog

# Example data
R = 1000  # Amount of money available
R_i = [0.05, 0.07, 0.06]  # Expected returns of investments
V_i = [0.02, 0.03, 0.01]  # Risks of investments (if needed)

# Coefficients for the objective function
c = [-r for r in R_i]  # Maximization of return

# Coefficients for the inequality constraints
A = [[1, 1, 1]]  # Total investment cannot exceed budget
b = [R]

# Boundary constraints for each investment
x_bounds = [(0, None) for _ in R_i]

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

print('Optimal investments:', result.x)
print('Maximum expected return:', -result.fun)
