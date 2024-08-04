from crud_flask_apirest.app import app, db  # Substitua 'app' e 'db' pelos nomes corretos se forem diferentes

with app.app_context():
    db.create_all()