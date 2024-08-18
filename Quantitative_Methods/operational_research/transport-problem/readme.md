# Transportation Problem

A bicycle manufacturing company operates two plants, one located in São Paulo and another in Recife. The company distributes bicycles to three dealers located in Porto Alegre, Brasília, and Manaus.

### **Plants**

| Plant     | Supply (units) |
|-----------|----------------|
| São Paulo | 600            |
| Recife    | 700            |

### **Markets**

| Market       | Demand (units) |
|--------------|----------------|
| Porto Alegre | 450            |
| Brasília     | 500            |
| Manaus       | 300            |

### **Shipping Costs Per Unit**

| From/To  | Porto Alegre | Brasília | Manaus |
|----------|--------------|----------|--------|
| São Paulo | $25          | $30      | $70    |
| Recife    | $60          | $35      | $50    |

These are the transportation costs for the problem's network.

## Linear Programming Problem Formulation

### **Decision Variables:**

- \( x_{SP,PA} \): Number of bicycles shipped from São Paulo to Porto Alegre.
- \( x_{SP,BR} \): Number of bicycles shipped from São Paulo to Brasília.
- \( x_{SP,MA} \): Number of bicycles shipped from São Paulo to Manaus.
- \( x_{RE,PA} \): Number of bicycles shipped from Recife to Porto Alegre.
- \( x_{RE,BR} \): Number of bicycles shipped from Recife to Brasília.
- \( x_{RE,MA} \): Number of bicycles shipped from Recife to Manaus.

### **Objective Function:**

Minimize the total transportation cost:

\[
Z = 25x_{SP,PA} + 30x_{SP,BR} + 70x_{SP,MA} + 60x_{RE,PA} + 35x_{RE,BR} + 50x_{RE,MA}
\]

### **Supply Constraints:**

- The São Paulo plant can supply up to 600 bicycles:
  \[
  x_{SP,PA} + x_{SP,BR} + x_{SP,MA} \leq 600
  \]
- The Recife plant can supply up to 700 bicycles:
  \[
  x_{RE,PA} + x_{RE,BR} + x_{RE,MA} \leq 700
  \]

### **Demand Constraints:**

- Porto Alegre requires 450 bicycles:
  \[
  x_{SP,PA} + x_{RE,PA} = 450
  \]
- Brasília requires 500 bicycles:
  \[
  x_{SP,BR} + x_{RE,BR} = 500
  \]
- Manaus requires 300 bicycles:
  \[
  x_{SP,MA} + x_{RE,MA} = 300
  \]

### **Non-Negativity Condition:**

All decision variables must be greater than or equal to zero:
\[
x_{SP,PA}, x_{SP,BR}, x_{SP,MA}, x_{RE,PA}, x_{RE,BR}, x_{RE,MA} \geq 0
\]

## **Solution:**

To solve this transportation problem, we can use a linear programming solver to minimize the objective function while satisfying all constraints. The optimal solution is as follows:

- \( x_{SP,PA} = 450 \) (Ship 450 bicycles from São Paulo to Porto Alegre)
- \( x_{SP,BR} = 150 \) (Ship 150 bicycles from São Paulo to Brasília)
- \( x_{RE,BR} = 350 \) (Ship 350 bicycles from Recife to Brasília)
- \( x_{RE,MA} = 300 \) (Ship 300 bicycles from Recife to Manaus)
- \( x_{SP,MA} = 0 \) (No bicycles are shipped from São Paulo to Manaus)
- \( x_{RE,PA} = 0 \) (No bicycles are shipped from Recife to Porto Alegre)

### **Total Minimum Cost:**

Substituting these values into the objective function:

\[
Z = 25(450) + 30(150) + 70(0) + 60(0) + 35(350) + 50(300)
\]

\[
Z = 11,250 + 4,500 + 0 + 0 + 12,250 + 15,000 = 43,000
\]

Thus, the minimum transportation cost is **$43,000**.

This solution satisfies all the supply and demand constraints while minimizing the transportation cost for the company.
