# Operational Research Mixing Problem

Factory XYZ produces feed for livestock. The rations are made from a mixture of three different types of grains: Grain 1, Grain 2, and Grain 3. Three nutrients are considered in the final product: Nutrient A, Nutrient B, and Nutrient C.

## Grain Details

- **Grain 1**:
  - Cost: R$35.00 per kg
  - Nutrient Content: 
    - 30 mg of Nutrient A
    - 10 mg of Nutrient B
    - 43 mg of Nutrient C

- **Grain 2**:
  - Cost: R$23.00 per kg
  - Nutrient Content: 
    - 28 mg of Nutrient A
    - 17 mg of Nutrient B
    - 40 mg of Nutrient C

- **Grain 3**:
  - Cost: R$78.00 per kg
  - Nutrient Content: 
    - 70 mg of Nutrient A

## Nutrient Requirements

The cattle feed must contain at least:
- 1,250 mg of Nutrient A
- 380 mg of Nutrient B
- 980 mg of Nutrient C

## Objective

The analyst wants to determine the composition of the feed that minimizes production costs, while meeting the minimum nutrient requirements.

## Total Cost Calculation

The objective function is:

\[ Z = 35x_1 + 23x_2 + 78x_3 \]

Substituting the values:

\[ Z = 35 \cdot 0 + 23 \cdot 44.642857 + 78 \cdot 0 \]

Let's calculate:

\[ Z = 23 \cdot 44.642857 \]
\[ Z \approx 1,027.71 \]

Therefore, the minimum total cost is approximately R$ 1,027.71.

## Constraints Verification

To ensure that the solution meets all constraints, let's verify if the minimum nutrient requirements are satisfied:

**Nutrient A:**

\[ 30 \cdot 0 + 28 \cdot 44.642857 + 70 \cdot 0 = 28 \cdot 44.642857 \approx 1,250 \text{ mg} \]

**Nutrient B:**

\[ 10 \cdot 0 + 17 \cdot 44.642857 = 17 \cdot 44.642857 \approx 758 \text{ mg} \]

**Nutrient C:**

\[ 43 \cdot 0 + 40 \cdot 44.642857 = 40 \cdot 44.642857 \approx 1,783 \text{ mg} \]

The quantities of nutrients A, B, and C in the provided solution are:

- **Nutrient A**: Approximately 1,250 mg (meets the requirement)
- **Nutrient B**: Approximately 758 mg (meets the requirement)
- **Nutrient C**: Approximately 1,783 mg (meets the requirement)

**Note**: If there is a discrepancy, the model or constraints may need adjustment to ensure all are precisely met.

## Final Summary

With the provided solution:

- **Minimum Total Cost**: R$ 1,027.71
- **Grain 1 (kg)**: 0
- **Grain 2 (kg)**: 44.642857
- **Grain 3 (kg)**: 0


