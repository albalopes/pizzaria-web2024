from flask import Flask, render_template, flash, redirect, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

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

        return redirect(url_for('cadastro_usuario'))
