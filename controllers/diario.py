from flask import render_template, request, redirect, flash
from database import db
from models.diario import Diario
from flask import Blueprint

bp_diario = Blueprint("diario", __name__, template_folder='templates')

@bp_diario.route('/recovery')
def recovery():
    return render_template('diario_recovery.html')
