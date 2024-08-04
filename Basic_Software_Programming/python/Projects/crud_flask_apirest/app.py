from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)   #app variável
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://teste:teste@localhost/flaskcrud'

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return{"id":self.id, "nome":self.nome, "email":self.email}

#selecionar tudo
@app.route("/user", methods=["GET"]) #"app" é de acordo com a variável na linha 6
def seleciona_usuarios():   #/"user" precisa ser o mesmo do banco
    user_objetos = user.query.all()
    user_json = [user.to_json() for user in user_objetos]
    
    return gera_response(200,"usuarios", user_json)
    



#selecionar individual
@app.route("/user/<id>", methods=["GET"])
def seleciona_usuario(id):
    user_object = user.query.filter_by(id=id).first()
    user_json = user_object.to_json()
    return gera_response(200,"usuario", user_json)

#cadastrar
@app.route("/user", methods=["POST"])
def criar_users():
    body = request.get_json()

    #validar se vieram os parametros ou utilizar um tryexception

    try:
        usuario = user (nome=body["nome"], email=body["email"]) 
        db.session.add(usuario)   #adicionar no bd
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {},"Erro ao cadastrar" )

#atualizar
@app.route("/user/<id>", methods=["PUT"])
def atualiza_user(id):
    user_object = user.query.filter_by(id=id).first() #pegar usuário
    body = request.get_json() #pegar modificações

    try:
        if('nome' in body):
            user_object.nome = body['nome']
        if('email' in body):
            user_object.email = body['email']

        db.session.add(user_object)
        db.session.commit()
        return gera_response(200, "usuario", user_object.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {},"Erro ao atualizar" )

#deletar
@app.route("/user/<id>", methods=["DELETE"])
def deleta_user(id):
    user_object = user.query.filter_by(id=id).first()

    try:
        db.session.delete(user_object)
        db.session.commit()
        return gera_response(200, "usuario", user_object.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {},"Erro ao d eletar" )




def gera_response(status, nome_do_conteudo, conteudo, mensagem = False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run(debug=True)