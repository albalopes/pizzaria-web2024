from flask import Flask, render_template, flash, redirect, request, url_for
from utils import db, lm
import os
from flask_migrate import Migrate
from models import *
from controllers.diario import bp_diario
from controllers.usuario import bp_usuario


app = Flask(__name__)
app.register_blueprint(bp_diario, url_prefix='/diario')
app.register_blueprint(bp_usuario, url_prefix='/usuario')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{username}:{password}@{host}/{mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lm.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/cardapio")
def cardapio():
    return render_template('cardapio.html')

@app.route('/avaliacoes')
def avaliacoes():
    dados = [{'cliente': 'Alba', 'nota': 3},
             {'cliente': 'Maria', 'nota': 5},
             {'cliente': 'João', 'nota': 2}
            ]
    return render_template('avaliacoes.html', dados=dados)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form["email"]
    senha = request.form["senha"]
    if (email=="admin@email.com" and senha=="123"):
        return 'Bem vindo admin'
    else:
        flash('E-mail ou senha inválidos', 'danger')
        flash('Tente novamente', 'warning')

        return redirect(url_for('login'))
        #return redirect('/login2')

@app.route('/cadastro_usuarios', methods=['GET', 'POST'])
def cadastro_usuarios():
    if request.method=='GET':
        return render_template('cadastro_usuarios.html')
    else:
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        csenha = request.form['csenha']

        if nome == '' or email == '' or senha == '' or senha != csenha:
            if nome == '':
                flash('Campo nome não pode ser vazio', 'danger')
            if email == '':
                flash('Campo email não pode ser vazio', 'danger')
            if senha == '':
                flash('Campo senha não pode ser vazio', 'danger')
            if senha != csenha:
                flash('As senhas não conferem', 'danger')
        else:
            flash('Dados cadastrados com sucesso!', 'success')

        return redirect(url_for('cadastro_usuarios'))


@app.route('/add_diario')
def add_diario():
    d = Diario('LIC0X83', 'Desenvolvimento Web')
    db.session.add(d)
    db.session.commit()
    return 'Dados inseridos com sucesso!'

@app.route('/select_diario')
def select_diario():
    #dados = Diario.query.all() # SELECT * from diario
    #for d in dados:
    #    print(d.id, d.titulo, d.disciplina)

    d = Diario.query.get(2) # SELECT * from diario WHERE id = 2
    print(d.id, d.titulo, d.disciplina)

    return 'Dados obtidos com sucesso'

@app.route('/update_diario')
def update_diario():
    d = Diario.query.get(2)
    d.titulo = 'LICX866'
    d.disciplina = "Segurança da Informação"
    db.session.add(d)
    db.session.commit()
    return 'Dados atualizados com sucesso'

@app.route('/delete_diario')
def delete_diario():
    d = Diario.query.get(2)
    db.session.delete(d)
    db.session.commit()
    return 'Dados excluídos com sucesso'