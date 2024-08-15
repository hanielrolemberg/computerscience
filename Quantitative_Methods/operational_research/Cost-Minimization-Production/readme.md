# Cost Minimization in Bicycle Production

## Problem Description

A bicycle factory is planning its production levels for the next semester. The unit cost of producing a children's bicycle is R$280.00, while the unit cost of producing an adult bicycle is R$620.00.

- **Labor Requirements:**
  - It takes six workers to produce a batch of 8 children's bicycles per day (0.75 bicycles per worker per day).
  - Three workers are required to manufacture 5 adult bicycles per day (0.625 bicycles per worker per day).
  
- **Constraints:**
  - A total of 200 workers are available for bicycle production.
  - The factory has a maximum production capacity of 300 bicycles per day.
  - To meet existing demand, at least 20 batches of children's bicycles (160 bicycles) and 15 batches of adult bicycles (75 bicycles) must be produced.

## Linear Programming Model

### Decision Variables:
- \( x_1 \): Number of children's bicycles to be produced per day.
- \( x_2 \): Number of adult bicycles to be produced per day.

### Objective Function:
Minimize the total production cost:
\[
\text{Min Z} = 280x_1 + 620x_2
\]

### Constraints:
1. **Labor Constraint:**
\[
0.75x_1 + 0.6x_2 \leq 200
\]

2. **Production Capacity:**
\[
x_1 + x_2 \leq 300
\]

3. **Minimum Production Requirements:**
\[
x_1 \geq 160
\]
\[
x_2 \geq 75
\]

### Non-negativity Constraint:
\[
x_1, x_2 \geq 0
\]

## Solution

Using linear programming to solve this problem, the optimal solution is:

- \( x_1 = 160 \) (children's bicycles produced per day)
- \( x_2 = 75 \) (adult bicycles produced per day)

The minimum production cost \( Z \) is **R$ 91,300.00** per day.
