# Financial Optimization Project

## Overview

This project aims to apply operations research techniques to optimize financial investments for purchasing a car. The goal is to maximize the returns on investments while adhering to available budget constraints and optionally managing associated risks.

## Problem Definition

You have a certain amount of money available for investment and want to maximize the returns from these investments. The problem is formulated as an optimization model where the objective is to determine the optimal allocation of funds across various investment options to achieve the highest possible return.

## Variables

- **Available Resources (R):** Total amount of money available for investment.
- **Investments (I):** Different investment options available, each with its own expected return and risk.
- **Investment Returns (R_i):** Expected return for each investment option.
- **Investment Risks (V_i):** Risk measure associated with each investment option.

## Objective

Maximize the total return on investments, considering financial constraints and potential risk factors.

## Model Formulation

### Decision Variables

- \( x_i \): Amount of money invested in option \( i \).

### Objective Function

Maximize the expected total return:
\[ \text{Maximize } Z = \sum_{i} R_i \cdot x_i \]

### Constraints

1. **Total Budget:** The total investment cannot exceed the available resources:
\[ \sum_{i} x_i \leq R \]

2. **Diversification (optional):** Limit the amount invested in each option to diversify risk:
\[ x_i \leq \text{Limit}_i \]

3. **Risk (optional):** Limit the acceptable level of risk:
\[ \sum_{i} V_i \cdot x_i \leq \text{Maximum Risk} \]

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hanielrolemberg/buying_a_car.git

## Navigate to the project directory:
```bash
cd financial-optimization-project
```
##Install required packages (Python)
```bash
pip install scipy
``` 

Usage
Open the optimization.py file.

Modify the R, R_i, and V_i variables according to your data.

Run the script:
```bash
python optimization.py
```
The script will output the optimal investment allocation and the maximum expected return.

Contributing
Contributions are welcome! Please open an issue or submit a pull request to enhance the project.

License
This project is licensed under the MIT License. See the LICENSE file for details.