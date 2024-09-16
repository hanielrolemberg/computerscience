import pulp

# Create the Linear Programming problem
prob = pulp.LpProblem("Diet_Problem", pulp.LpMinimize)

# Define the decision variables
x1 = pulp.LpVariable('Milk', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Meat', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('Fish', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('Salad', lowBound=0, cat='Continuous')

# Define the objective function (minimize cost)
prob += 2 * x1 + 20 * x2 + 25 * x3 + 3 * x4, "Total Cost"

# Define the constraints
prob += 2 * x1 + 2 * x2 + 10 * x3 + 20 * x4 >= 10, "Vitamin A"
prob += 50 * x1 + 20 * x2 + 10 * x3 + 30 * x4 >= 70, "Vitamin C"
prob += 80 * x1 + 70 * x2 + 10 * x3 + 80 * x4 >= 250, "Vitamin D"

# Solve the problem
prob.solve()

# Output the results
print("Status:", pulp.LpStatus[prob.status])
print("Milk (liters):", x1.varValue)
print("Meat (kg):", x2.varValue)
print("Fish (kg):", x3.varValue)
print("Salad (100g):", x4.varValue)
print("Total Cost ($):", pulp.value(prob.objective))
