import pulp

# Create a linear programming problem
lp_problem = pulp.LpProblem("Bicycle_Production_vs_Purchase", pulp.LpMinimize)

# Define decision variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')  # Model 1 bicycles produced internally
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')  # Model 2 bicycles produced internally
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')  # Model 3 bicycles produced internally
c1 = pulp.LpVariable('c1', lowBound=0, cat='Continuous')  # Model 1 bicycles purchased externally
c2 = pulp.LpVariable('c2', lowBound=0, cat='Continuous')  # Model 2 bicycles purchased externally
c3 = pulp.LpVariable('c3', lowBound=0, cat='Continuous')  # Model 3 bicycles purchased externally

# Define the objective function (minimize total cost)
lp_problem += (350 * x1 + 400 * x2 + 430 * x3 +
               460 * c1 + 540 * c2 + 580 * c3), "Total Cost"

# Define the constraints
# Demand constraints
lp_problem += (x1 + c1 == 3000), "Demand_Model_1"
lp_problem += (x2 + c2 == 2000), "Demand_Model_2"
lp_problem += (x3 + c3 == 1000), "Demand_Model_3"

# Resource constraints
lp_problem += (2 * x1 + 1.5 * x2 + 3 * x3 <= 10000), "Assembly_Time"
lp_problem += (1 * x1 + 2 * x2 + 1 * x3 <= 6000), "Painting_Time"

# Solve the problem
lp_problem.solve()

# Print the results
print(f"Status: {pulp.LpStatus[lp_problem.status]}")
print(f"Total Cost: R${pulp.value(lp_problem.objective):,.2f}")
print(f"Model 1 (Internal): {x1.varValue}")
print(f"Model 2 (Internal): {x2.varValue}")
print(f"Model 3 (Internal): {x3.varValue}")
print(f"Model 1 (External): {c1.varValue}")
print(f"Model 2 (External): {c2.varValue}")
print(f"Model 3 (External): {c3.varValue}")

# Example of optimal solution if obtained from solver
optimal_internal = (x1.varValue, x2.varValue, x3.varValue)
optimal_external = (c1.varValue, c2.varValue, c3.varValue)

print(f"Optimal internal production: Model 1: {optimal_internal[0]}, Model 2: {optimal_internal[1]}, Model 3: {optimal_internal[2]}")
print(f"Optimal external purchase: Model 1: {optimal_external[0]}, Model 2: {optimal_external[1]}, Model 3: {optimal_external[2]}")
