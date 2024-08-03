from scipy.optimize import linprog

# Dados do problema
budget = 10000  # Orçamento total disponível
cost_A = 1000  # Custo do Produto A
cost_B = 2000  # Custo do Produto B
return_A = 0.10  # Retorno do Produto A
return_B = 0.20  # Retorno do Produto B

# Coeficientes da função objetivo (negativos porque linprog minimiza)
c = [-return_A, -return_B]  # Maximizar retorno é equivalente a minimizar -retorno

# Coeficientes das restrições
A = [[cost_A, cost_B]]  # Matriz de coeficientes da restrição
b = [budget]  # Limiar da restrição

# Limites para as variáveis de decisão
x_bounds = [(0, None), (0, None)]  # Não podemos investir valores negativos

# Resolver o problema
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Verificar se a otimização foi bem-sucedida
if result.success:
    investment_A = result.x[0]
    investment_B = result.x[1]
    max_return = -result.fun

    # Resultados detalhados
    print(f"Optimal Investment in Product A: R$ {investment_A:.2f}")
    print(f"Optimal Investment in Product B: R$ {investment_B:.2f}")
    print(f"Maximum Expected Return: R$ {max_return:.2f}")

else:
    print("Optimization failed. Check the problem setup and constraints.")
    print("Status:", result.message)
