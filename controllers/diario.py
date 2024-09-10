from flask import render_template, request, redirect, flash, url_for
from utils import db
from models.diario import Diario
from flask import Blueprint
from flask_login import login_required

bp_diario = Blueprint("diario", __name__, template_folder='templates')

@bp_diario.route('/recovery')
@login_required
def recovery():
    dados = Diario.query.all()
    return render_template('diario_recovery.html', dados=dados)

@bp_diario.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method=="GET":
        return render_template('diario_create.html')

    if request.method=="POST":
        titulo = request.form['titulo']
        disciplina = request.form['disciplina']
        d = Diario(titulo, disciplina)
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('diario.recovery'))

@bp_diario.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    d = Diario.query.get(id)
    
    if request.method=="GET":
        return render_template('diario_update.html', d=d)

    if request.method=="POST":
        d.titulo = request.form['titulo']
        d.disciplina = request.form['disciplina']
        db.session.add(d)
        db.session.commit()
        return redirect(url_for('diario.recovery'))


@bp_diario.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    d = Diario.query.get(id)

    if request.method=="GET":
        return render_template('diario_delete.html', d=d)

    if request.method=="POST":
        db.session.delete(d)
        db.session.commit()
        return redirect(url_for('diario.recovery'))
        