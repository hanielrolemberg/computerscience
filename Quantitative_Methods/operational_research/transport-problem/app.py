import pulp

# Create the problem variable to minimize the cost
prob = pulp.LpProblem("Bicycle_Transportation_Cost_Minimization", pulp.LpMinimize)

# Decision variables
x_SP_PA = pulp.LpVariable('x_SP_PA', lowBound=0, cat='Continuous')  # São Paulo to Porto Alegre
x_SP_BR = pulp.LpVariable('x_SP_BR', lowBound=0, cat='Continuous')  # São Paulo to Brasília
x_SP_MA = pulp.LpVariable('x_SP_MA', lowBound=0, cat='Continuous')  # São Paulo to Manaus
x_RE_PA = pulp.LpVariable('x_RE_PA', lowBound=0, cat='Continuous')  # Recife to Porto Alegre
x_RE_BR = pulp.LpVariable('x_RE_BR', lowBound=0, cat='Continuous')  # Recife to Brasília
x_RE_MA = pulp.LpVariable('x_RE_MA', lowBound=0, cat='Continuous')  # Recife to Manaus

# Objective function (minimize transportation cost)
prob += 25 * x_SP_PA + 30 * x_SP_BR + 70 * x_SP_MA + 60 * x_RE_PA + 35 * x_RE_BR + 50 * x_RE_MA, "Total Transportation Cost"

# Supply constraints
prob += x_SP_PA + x_SP_BR + x_SP_MA <= 600, "Supply_Constraint_SP"
prob += x_RE_PA + x_RE_BR + x_RE_MA <= 700, "Supply_Constraint_RE"

# Demand constraints
prob += x_SP_PA + x_RE_PA == 450, "Demand_Constraint_PA"
prob += x_SP_BR + x_RE_BR == 500, "Demand_Constraint_BR"
prob += x_SP_MA + x_RE_MA == 300, "Demand_Constraint_MA"

# Solve the problem
prob.solve()

# Output the results
print("Status:", pulp.LpStatus[prob.status])

# Decision variables values
print(f"x_SP_PA (São Paulo to Porto Alegre): {x_SP_PA.varValue}")
print(f"x_SP_BR (São Paulo to Brasília): {x_SP_BR.varValue}")
print(f"x_SP_MA (São Paulo to Manaus): {x_SP_MA.varValue}")
print(f"x_RE_PA (Recife to Porto Alegre): {x_RE_PA.varValue}")
print(f"x_RE_BR (Recife to Brasília): {x_RE_BR.varValue}")
print(f"x_RE_MA (Recife to Manaus): {x_RE_MA.varValue}")

# Total minimum cost
print(f"Total Minimum Transportation Cost: ${pulp.value(prob.objective):,.2f}")
