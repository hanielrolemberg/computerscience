from scipy.optimize import linprog

# Coeficientes da função objetivo
c = [280, 620]  # Min Z = 280x1 + 620x2

# Coeficientes das restrições (lado esquerdo)
A = [
    [0.75, 0.6],  # 0.75x1 + 0.6x2 ≤ 200
    [1, 1],       # x1 + x2 ≤ 300
    [-1, 0],      # -x1 ≤ -160  => x1 ≥ 160
    [0, -1]       # -x2 ≤ -75   => x2 ≥ 75
]

# Lado direito das restrições
b = [200, 300, -160, -75]

# Resolvendo o problema de programação linear
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Exibindo a solução
print("Número ótimo de bicicletas infantis a serem produzidas por dia:", result.x[0])
print("Número ótimo de bicicletas de adultos a serem produzidas por dia:", result.x[1])
print("Custo mínimo de produção por dia: R$", result.fun)
