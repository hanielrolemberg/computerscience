## Operational research (OR)

Operational research (OR) is the science of better decision making. 

Mathematical modeling techniques and efficient computational algorithms. This enables effective decision-making and the development of more productive systems.

The different types of models lead us to adopt different OR techniques, such as Linear Programming, Non-Linear Programming, Queuing Theory, Simulation, Computational Intelligence and Theory
of the Games.

- **Model Classification**:

Static or Dynamic
Linear or Nonlinear
Integer or Non-Integer
Deterministic or Stochastic
In this content, we will focus exclusively on deterministic models.

# Composition:
### Composition:
- **Objective Function**: Defines the goal to be maximized or minimized.
- **Decision Variables**: The variables that will be adjusted to achieve the objective.
- **Constraints**: The limitations or requirements that must be met.

**Example**:
- **Objective Function**: Maximize revenue
- **Decision Variables**: Variables to be decided (e.g., quantities of products to produce)
- **Constraints**: Available resources (e.g., budget, materials, time)




**Phases of an Operations Research Study**

Problem Formulation

Clearly define the problem to be solved, including objectives and constraints.
System Observation

Gather and analyze data about the system to understand its behavior and constraints.
Formulation of the Mathematical Model

Develop a mathematical representation of the problem, including objective function, decision variables, and constraints.
Mathematical Model Verification and Use for Prediction

Verify the accuracy of the mathematical model and use it to make predictions about the system's behavior.
Selection of the Best Alternative

Evaluate different solutions and select the best alternative based on the model's predictions and other relevant criteria.
Presentation of Results and Conclusion

Present the findings and conclusions in a clear and comprehensive manner.
Implementation and Analysis of Recommendations

Implement the recommended solution and analyze its effectiveness in solving the problem.



## Main techniques of operations research:
Linear Programming
Integer Programming
Nonlinear Programming
Dynamic Programming
Network Flows
Queuing Theory
Simulation
Decision Analysis
Game Theory
Markov Processes


Let's focus on the first one.

# Linear Programming



### Steps to Find the Optimal Maximum and Minimum Point  Using Linear Programming in Operations Research

1. **Formulate the Problem**:
   - Clearly define the decision variables.
   - Specify the objective function to be maximized or minimized.
   - List all the constraints of the problem.

2. **Transform the Constraints into Inequalities**:
   - Write the constraints as linear inequalities in the form \(a_1x_1 + b_1x_2 \leq d_1\), \(a_2x_1 + b_2x_2 \geq d_2\), etc.
   - Include the non-negativity constraints \(x_1 \geq 0\) and \(x_2 \geq 0\).

3. **Plot the Constraints on the Cartesian Plane**:
   - Each constraint is represented by a line on the \(x_1\)-\(x_2\) graph.
   - Determine the feasible region as the intersection of all areas defined by the inequalities.

4. **Identify the Feasible Region**:
   - The feasible region is the area where all constraints are simultaneously satisfied. This area is generally a convex polygon.

5. **Find the Vertices of the Feasible Region**:
   - The vertices of the feasible region are the intersection points of the constraint lines.
   - Solve the systems of equations formed by the intersections to find the vertices.

6. **Evaluate the Objective Function at the Vertices**:
   - Calculate the value of the objective function \(Z = c_1x_1 + c_2x_2\) at each vertex of the feasible region.

7. **Determine the Optimal Solution**:
   - The optimal maximum solution is the vertex where the objective function has the highest value.
   - The optimal minimum solution is the vertex where the objective function has the lowest value.

### Example Summary:

Let's consider the previous example with the objective function \(Z = 3x_1 + 2x_2\):

**Problem**:  
Maximize \(Z = 3x_1 + 2x_2\)  
Subject to:
\[
x_1 + x_2 \leq 4
\]
\[
x_1 \leq 2
\]
\[
x_2 \leq 3
\]
\[
x_1, x_2 \geq 0
\]

1. **Plot the constraints** on the \(x_1\)-\(x_2\) graph.
2. **Identify the feasible region** (intersection of the areas below the constraint lines and in the first quadrant).
3. **Find the vertices of the feasible region**: (0,0), (0,3), (2,2), (2,0).
4. **Evaluate the objective function at the vertices**:
   - At (0,0): \(Z = 0\)
   - At (0,3): \(Z = 6\)
   - At (2,2): \(Z = 10\)
   - At (2,0): \(Z = 6\)

5. **Determine the optimal solution**:
   - **Maximum**: \(Z = 10\) at point (2,2).
   - **Minimum**: \(Z = 0\) at point (0,0).


Python code:

```python
import matplotlib.pyplot as plt
import numpy as np

# Definindo as linhas das restrições
x = np.linspace(0, 5, 400)
y1 = 4 - x  # Linha para x1 + x2 <= 4
y2 = np.full_like(x, 3)  # Linha para x2 <= 3
y3 = np.full_like(x, 2)  # Linha para x1 <= 2

plt.figure(figsize=(8, 6))

# Plotando as linhas das restrições
plt.plot(x, y1, label=r'$x_1 + x_2 \leq 4$')
plt.plot(x, y2, label=r'$x_2 \leq 3$')
plt.plot(np.full_like(x, 2), x, label=r'$x_1 \leq 2$')

# Preenchendo a região viável
plt.fill_between(x, np.minimum(y1, 3), where=(x <= 2), color='gray', alpha=0.5)

# Marcando os pontos de interesse (vértices)
vertices = [(0, 0), (0, 3), (2, 2), (2, 0)]
for vert in vertices:
    plt.plot(*vert, 'ro')

# Configurações do gráfico
plt.xlim((0, 5))
plt.ylim((0, 5))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()
plt.grid(True)
plt.title('Gráfico de Programação Linear')

# Exibindo o gráfico
plt.show()
```

![Linear Programming Graph](https://github.com/hanielrolemberg/computerscience/blob/master/Quantitative_Methods/operational_research/linearprogramming.png)

