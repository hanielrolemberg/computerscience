from scipy.optimize import linprog

# Dados do problema
budget = 15000  # Orçamento total disponível
min_investment_A = 2000
min_investment_B = 3000
min_investment_C = 1500

cost_A = 1000  # Custo fixo da Opção A
cost_B = 1500  # Custo fixo da Opção B
cost_C = 500   # Custo fixo da Opção C

return_A = 0.08  # Retorno da Opção A
return_B = 0.12  # Retorno da Opção B
return_C = 0.10  # Retorno da Opção C

# Coeficientes da função objetivo (negativos porque linprog minimiza)
c = [-return_A, -return_B, -return_C]  # Maximizar retorno é equivalente a minimizar -retorno

# Coeficientes das restrições
A = [
    [1, 1, 1]  # Custo total dos investimentos
]
b = [budget - (cost_A + cost_B + cost_C)]  # Orçamento disponível após custos fixos

# Restrições mínimas de investimento
A_min = [
    [-1, 0, 0],  # Investimento mínimo para Opção A
    [0, -1, 0],  # Investimento mínimo para Opção B
    [0, 0, -1]   # Investimento mínimo para Opção C
]
b_min = [
    -min_investment_A,
    -min_investment_B,
    -min_investment_C
]

# Limites para as variáveis de decisão
x_bounds = [(0, None), (0, None), (0, None)]  # Não podemos investir valores negativos

# Resolver o problema
result = linprog(c, A_ub=A + A_min, b_ub=b + b_min, bounds=x_bounds, method='highs')

# Verificar se a otimização foi bem-sucedida
if result.success:
    investment_A = result.x[0]
    investment_B = result.x[1]
    investment_C = result.x[2]
    max_return = -result.fun

    # Resultados detalhados
    print(f"Optimal Investment in Option A: R$ {investment_A:.2f}")
    print(f"Optimal Investment in Option B: R$ {investment_B:.2f}")
    print(f"Optimal Investment in Option C: R$ {investment_C:.2f}")
    print(f"Maximum Expected Return: R$ {max_return:.2f}")

else:
    print("Optimization failed. Check the problem setup and constraints.")
    print("Status:", result.message)
