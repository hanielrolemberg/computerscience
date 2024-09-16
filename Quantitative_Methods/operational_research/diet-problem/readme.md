# Diet Problem - Linear Programming Example

This is a classic diet problem in linear programming, where the goal is to find the optimal mix of foods that satisfy nutritional requirements at the lowest possible cost.

## Problem Description

A mother is concerned about her children's diet. She wants to ensure they have a balanced diet and consulted a nutritionist who recommended that they consume at least 10mg of Vitamin A, 70mg of Vitamin C, and 250mg of Vitamin D per day.

However, she also wants to minimize costs while providing this balanced diet. She researched the nutritional content of different types of food as follows:

| Vitamin | Milk (liters) | Meat (kg) | Fish (kg) | Salad (100g) |
|---------|---------------|-----------|-----------|--------------|
| A       | 2 mg          | 2 mg      | 10 mg     | 20 mg        |
| C       | 50 mg         | 20 mg     | 10 mg     | 30 mg        |
| D       | 80 mg         | 70 mg     | 10 mg     | 80 mg        |

She also found out the costs for these foods:

- Milk: $2.00 per liter
- Meat: $20.00 per kg
- Fish: $25.00 per kg
- Salad: $3.00 per 100g

### Goal

Help the mother choose the best diet for her children at the lowest possible cost using linear programming.

## Linear Programming Formulation

### Decision Variables

Let:
- `x1`: Amount of milk (in liters)
- `x2`: Amount of meat (in kg)
- `x3`: Amount of fish (in kg)
- `x4`: Amount of salad (in 100g)

### Objective Function

Minimize the total cost:

\[
\text{Minimize } Z = 2x_1 + 20x_2 + 25x_3 + 3x_4
\]

### Constraints

Nutritional requirements:

- **Vitamin A**: 
\[
2x_1 + 2x_2 + 10x_3 + 20x_4 \geq 10
\]

- **Vitamin C**:
\[
50x_1 + 20x_2 + 10x_3 + 30x_4 \geq 70
\]

- **Vitamin D**:
\[
80x_1 + 70x_2 + 10x_3 + 80x_4 \geq 250
\]

### Non-Negativity Constraints

All variables must be non-negative:

\[
x_1 \geq 0, \quad x_2 \geq 0, \quad x_3 \geq 0, \quad x_4 \geq 0
\]

## Solution Using Python and PuLP

Here is how you can solve this problem using Python and the `PuLP` library.

```python
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
```


## Understanding the Results

After solving the diet problem using linear programming, the results you obtained were:

- **Milk (liters): 2.9166667**
- **Meat (kg): 0.0**
- **Fish (kg): 0.0**
- **Salad (100g): 0.20833333**
- **Total Cost ($): 6.45833339**

### Why Is the Total Cost Greater Than $6?

The total cost is the sum of the costs of the foods required to meet the nutritional requirements.

1. **Milk (2.9166667 liters)**:
   - Cost: \(2.9166667 \times 2\) = $5.8333334

2. **Salad (0.20833333 servings of 100g)**:
   - Cost: \(0.20833333 \times 3\) = $0.625

When you sum these values, the total is approximately $6.45833339.

### Explanation of the Cost

The cost is greater than $6 because the minimum diet that satisfies all the nutritional constraints requires more milk and a bit of salad, which naturally increases the cost. The solution provided by the linear programming solver minimizes the cost but cannot be lower than what is necessary to meet all the constraints (the amounts of vitamins A, C, and D).

### Validation of the Constraints

To meet the vitamin requirements:

- **Vitamin A**:
  - Milk contributes \(2 \times 2.9166667 = 5.8333334\) mg
  - Salad contributes \(20 \times 0.20833333 = 4.1666666\) mg
  - Total: 10 mg (exactly what is needed)

- **Vitamin C**:
  - Milk contributes \(50 \times 2.9166667 = 145.833335\) mg
  - Salad contributes \(30 \times 0.20833333 = 6.25\) mg
  - Total: 152.083335 mg (greater than required, but cannot be lower)

- **Vitamin D**:
  - Milk contributes \(80 \times 2.9166667 = 233.333336\) mg
  - Salad contributes \(80 \times 0.20833333 = 16.6666664\) mg
  - Total: 250 mg (exactly what is needed)

### Conclusion

The solver found the optimal and cheapest solution that meets all the nutritional constraints, resulting in a cost of $6.45. This is the minimum possible cost given the problem's requirements.

