import pulp

# Create a linear programming problem
lp_problem = pulp.LpProblem("Minimize_Cost", pulp.LpMinimize)

# Define decision variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')  # kg of grain 1
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')  # kg of grain 2
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')  # kg of grain 3

# Define the objective function (minimize total cost)
lp_problem += (35 * x1 + 23 * x2 + 78 * x3), "Total Cost"

# Define the constraints
lp_problem += (30 * x1 + 28 * x2 + 70 * x3 >= 1250), "Nutrient_A"
lp_problem += (10 * x1 + 17 * x2 >= 380), "Nutrient_B"
lp_problem += (43 * x1 + 40 * x2 >= 980), "Nutrient_C"

# Solve the problem
lp_problem.solve()

# Print the results
status = pulp.LpStatus[lp_problem.status]
total_cost = pulp.value(lp_problem.objective)
grain1_qty = x1.varValue
grain2_qty = x2.varValue
grain3_qty = x3.varValue

print(f"Status: {status}")
print(f"Total Cost: R${total_cost:,.2f}")
print(f"Grain 1 (kg): {grain1_qty}")
print(f"Grain 2 (kg): {grain2_qty}")
print(f"Grain 3 (kg): {grain3_qty}")
