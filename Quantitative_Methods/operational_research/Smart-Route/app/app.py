from flask import Flask, request, render_template
import pulp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/optimize-route', methods=['POST'])
def optimize_route():
    num_nodes = int(request.form['num-nodes'])
    distances = []
    
    for i in range(num_nodes):
        row = list(map(float, request.form[f'distances-{i}'].split()))
        distances.append(row)
    
    # Create the optimization problem
    prob = pulp.LpProblem("Logistics_Routing_Problem", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("x", (range(num_nodes), range(num_nodes)), cat='Binary')
    
    prob += pulp.lpSum(distances[i][j] * x[i][j] for i in range(num_nodes) for j in range(num_nodes) if i != j)
    
    for i in range(num_nodes):
        prob += pulp.lpSum(x[i][j] for j in range(num_nodes) if i != j) == 1
        prob += pulp.lpSum(x[j][i] for j in range(num_nodes) if i != j) == 1
    
    prob.solve()
    
    result = []
    for i in range(num_nodes):
        for j in range(num_nodes):
            if x[i][j].varValue == 1:
                result.append((i, j, distances[i][j]))
    
    total_cost = pulp.value(prob.objective)
    
    return render_template('result.html', route=result, total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
