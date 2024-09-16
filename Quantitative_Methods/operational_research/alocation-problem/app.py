import pulp

# Define the problem
prob = pulp.LpProblem("Minimize_Cleaning_Time", pulp.LpMinimize)

# Define decision variables
x11 = pulp.LpVariable('x11', cat='Binary')
x12 = pulp.LpVariable('x12', cat='Binary')
x13 = pulp.LpVariable('x13', cat='Binary')
x14 = pulp.LpVariable('x14', cat='Binary')

x21 = pulp.LpVariable('x21', cat='Binary')
x22 = pulp.LpVariable('x22', cat='Binary')
x23 = pulp.LpVariable('x23', cat='Binary')
x24 = pulp.LpVariable('x24', cat='Binary')

x31 = pulp.LpVariable('x31', cat='Binary')
x32 = pulp.LpVariable('x32', cat='Binary')
x33 = pulp.LpVariable('x33', cat='Binary')
x34 = pulp.LpVariable('x34', cat='Binary')

x41 = pulp.LpVariable('x41', cat='Binary')
x42 = pulp.LpVariable('x42', cat='Binary')
x43 = pulp.LpVariable('x43', cat='Binary')
x44 = pulp.LpVariable('x44', cat='Binary')

# Objective function
prob += (2 * x11 + 5 * x12 + 7 * x13 + 3 * x14 +
         3 * x21 + 6 * x22 + 8 * x23 + 4 * x24 +
         4 * x31 + 4 * x32 + 6 * x33 + 5 * x34 +
         2 * x41 + 5 * x42 + 7 * x43 + 2 * x44)

# Constraints
prob += x11 + x21 + x31 + x41 == 1  # Make Bed
prob += x12 + x22 + x32 + x42 == 1  # Clean Bathroom
prob += x13 + x23 + x33 + x43 == 1  # Sweep Room
prob += x14 + x24 + x34 + x44 == 1  # Dusting

# Solve the problem
prob.solve()

# Display the results
print("Optimal Solution:")
for v in prob.variables():
    if v.varValue == 1:
        print(f"{v.name} = {v.varValue}")

print(f"Minimum Time: {pulp.value(prob.objective)} minutes")
