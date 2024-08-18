## Hotel Room Cleaning Optimization Problem

### Problem Description

A supervisor in charge of a hotel cleaning team needs to organize teams of housekeepers to clean rooms during guest turnover. Guests checking out must vacate their rooms by 12:00 PM, while new guests can check in starting at 2:00 PM. The cleaning teams have limited time to organize and clean all the rooms. Therefore, the supervisor must allocate tasks among the housekeepers to complete the work as quickly as possible.

The supervisor needs to form a team to take care of the rooms on the third floor of the hotel. The tasks to be completed are: making the beds, cleaning the bathroom, sweeping the room, and dusting. The time each housekeeper takes to complete these tasks in a single room is as follows:

| Housekeeper | Task             | Make Bed | Clean Bathroom | Sweep Room | Dusting |
|-------------|------------------|----------|----------------|------------|---------|
| **Lara**    |                  | 2 min    | 5 min          | 7 min      | 3 min   |
| **Ana**     |                  | 3 min    | 6 min          | 8 min      | 4 min   |
| **Julia**   |                  | 4 min    | 4 min          | 6 min      | 5 min   |
| **Talita**  |                  | 2 min    | 5 min          | 7 min      | 2 min   |

### Problem Formulation

To minimize the total cleaning time, we define the problem as a linear programming problem.

#### **Decision Variables**

Let \( x_{ij} \) be a binary variable indicating whether housekeeper \( i \) performs task \( j \):

- \( x_{1j} \): Lara performs task \( j \)
- \( x_{2j} \): Ana performs task \( j \)
- \( x_{3j} \): Julia performs task \( j \)
- \( x_{4j} \): Talita performs task \( j \)

Where \( j \) represents the tasks:
1. Make Bed
2. Clean Bathroom
3. Sweep Room
4. Dusting

#### **Objective Function**

The objective is to minimize the total time spent on cleaning:

\[
\text{Minimize } Z = 2x_{11} + 5x_{12} + 7x_{13} + 3x_{14} + 3x_{21} + 6x_{22} + 8x_{23} + 4x_{24} + 4x_{31} + 4x_{32} + 6x_{33} + 5x_{34} + 2x_{41} + 5x_{42} + 7x_{43} + 2x_{44}
\]

#### **Constraints**

Each task must be performed by exactly one housekeeper:

\[
x_{11} + x_{21} + x_{31} + x_{41} = 1
\]
\[
x_{12} + x_{22} + x_{32} + x_{42} = 1
\]
\[
x_{13} + x_{23} + x_{33} + x_{43} = 1
\]
\[
x_{14} + x_{24} + x_{34} + x_{44} = 1
\]

Also, \( x_{ij} \) are binary variables:

\[
x_{ij} \in \{0, 1\} \quad \text{for all } i, j
\]

### Solution in Python

Here is a Python solution using the `PuLP` library to solve the linear programming problem:

```python
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
