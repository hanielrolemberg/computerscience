# Linear Programming Model for Bicycle Production vs. Purchase

## Problem Description

A bicycle factory has received an order of R$750,000.00, which includes:
- 3,000 bicycles of Model 1
- 2,000 bicycles of Model 2
- 1,000 bicycles of Model 3

### Production Details

- **Model 1:**
  - Assembly time: 2 hours
  - Painting time: 1 hour
  - Production cost: R$350.00

- **Model 2:**
  - Assembly time: 1.5 hours
  - Painting time: 2 hours
  - Production cost: R$400.00

- **Model 3:**
  - Assembly time: 3 hours
  - Painting time: 1 hour
  - Production cost: R$430.00

The factory has the following resources available:
- 10,000 hours for assembly
- 6,000 hours for painting

### Outsourcing Costs

- **Model 1:** R$460.00
- **Model 2:** R$540.00
- **Model 3:** R$580.00

## Decision Variables

Define the following decision variables:
- `x1`: Number of Model 1 bicycles to be produced internally
- `x2`: Number of Model 2 bicycles to be produced internally
- `x3`: Number of Model 3 bicycles to be produced internally
- `c1`: Number of Model 1 bicycles to be purchased externally
- `c2`: Number of Model 2 bicycles to be purchased externally
- `c3`: Number of Model 3 bicycles to be purchased externally

## Objective Function

Minimize the total cost:
\[ Z = 350x_1 + 400x_2 + 430x_3 + 460c_1 + 540c_2 + 580c_3 \]

## Constraints

### Demand Constraints
- \( x_1 + c_1 = 3,000 \) (Model 1)
- \( x_2 + c_2 = 2,000 \) (Model 2)
- \( x_3 + c_3 = 1,000 \) (Model 3)

### Resource Constraints
- Assembly time: \( 2x_1 + 1.5x_2 + 3x_3 \leq 10,000 \) hours
- Painting time: \( x_1 + 2x_2 + x_3 \leq 6,000 \) hours

### Non-Negativity Constraints
- \( x_1, x_2, x_3, c_1, c_2, c_3 \geq 0 \)

## Solution Approach

1. **Calculate the cost if producing all internally:**
   - Total assembly time required: \( 2(3,000) + 1.5(2,000) + 3(1,000) = 12,000 \) hours
   - Total painting time required: \( 1(3,000) + 2(2,000) + 1(1,000) = 8,000 \) hours

   Since the factory only has 10,000 hours for assembly and 6,000 hours for painting, it cannot produce all bicycles internally due to the painting constraint.

2. **Optimize the production and purchase decision:**
   - Use a linear programming solver to find the optimal combination of internal production and external purchase that minimizes the total cost.

## Conclusion

Use a linear programming solver to determine the optimal quantities for internal production and external purchase. Compare the minimized total cost with the cost of producing all bicycles internally (if it were possible) to make an informed decision on whether to produce or purchase the bicycles.
