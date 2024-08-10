# Logistics Route Optimization

## Overview

This project focuses on optimizing truck routes for logistics using linear programming. The goal is to find the most efficient route that minimizes the total transportation cost based on the distances between various locations.

## Problem Context

### Description

In logistics, efficiently routing trucks is crucial for minimizing operational costs and improving customer service. The specific problem addressed here is finding the most cost-effective route for a set of delivery locations.

- **Input:**
  - **Number of Locations:** Total number of locations that need to be visited.
  - **Distance Matrix:** A matrix representing the distances between each pair of locations.

- **Objective:**
  - **Minimize Total Cost:** Determine the route that minimizes the total transportation cost, calculated based on the distances between locations.

- **Constraints:**
  - Each location must be visited exactly once.
  - The route must start and end at the same location (if applicable).

### Importance

- **Cost Reduction:** Efficient routes can significantly lower fuel and travel costs.
- **Improved Customer Service:** Efficient routes ensure timely deliveries.
- **Operational Efficiency:** Enhances overall operational performance.

## Decision

### Chosen Approach

To solve the route optimization problem, we use **Linear Programming**. This approach is effective for optimization problems where the objective is to minimize or maximize a linear function subject to linear constraints.

- **Linear Programming Model:**
  - **Decision Variables:** 
    - `x[i][j]`: Binary variables indicating whether there is a direct route from location `i` to location `j`.
  - **Objective Function:**
    - Minimize the total transportation cost, which is the sum of distances multiplied by the decision variables `x[i][j]`.
  - **Constraints:**
    - Ensure that each location is visited exactly once.
    - Ensure that the route is complete without leaving any locations disconnected.

- **Solution Method:**
  - We use the **PuLP** solver to handle the linear programming problem. PuLP is a Python library that facilitates defining and solving linear programming problems.

### Implementation

1. **User Input:**
   - The user provides the number of locations and the distance matrix.
2. **Optimization:**
   - The system applies the linear programming model to find the optimized route.
3. **Output:**
   - The optimal route and the associated total cost are presented to the user.

### Advantages

- **Accuracy:** Linear programming provides exact solutions.
- **Computational Efficiency:** PuLP handles problems of reasonable size efficiently.
- **Flexibility:** The model can be adapted for various logistic optimization scenarios.

## Example

### Scenario

A logistics company needs to optimize truck routes for delivering products to 4 locations. The distance matrix is provided as follows:

- **Number of Locations:** 4
- **Distances:**
  - Row 1: `0 10 15 20`
  - Row 2: `10 0 35 25`
  - Row 3: `15 35 0 30`
  - Row 4: `20 25 30 0`

### Expected Output

- **Optimized Route:** The route that minimizes the total transportation cost.
- **Total Cost:** The cost associated with the optimized route.

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
Install Dependencies:

bash
Copy code
pip install pulp flask
Run the Application:

```bash

python app.py
Access the Application:
``` 

Open your browser and navigate to http://127.0.0.1:5000/ to use the application.

## Contributing
Contributions to improve the application are welcome! Please fork the repository and submit a pull request with your changes.

##License##
This project is licensed under the MIT License. See the LICENSE file for details.

