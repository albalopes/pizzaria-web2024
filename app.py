from flask import Flask, render_template

app = Flask(__name__)

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
