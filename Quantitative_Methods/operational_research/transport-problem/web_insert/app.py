from flask import Flask, render_template, request

app = Flask(__name__)

# Dados de exemplo
plants = ["SP", "Recife"]
destinations = ["Porto Alegre", "Brasília", "Manaus"]
distances = {
    "SP": [25, 30, 70],
    "Recife": [60, 35, 50]
}

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        plant = request.form['plant']
        # Filtrar as distâncias baseadas na planta selecionada
        plant_distances = distances.get(plant, [])
        return render_template('insert.html', plant=plant, destinations=destinations, distances=plant_distances, zip=zip)
    return render_template('insert.html', plants=plants)

if __name__ == '__main__':
    app.run(debug=True)
