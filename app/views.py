from app import app
from flask import render_template, url_for,  request, session, redirect, flash, g
import sqlite3


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory=sqlite3.Row 
    return

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/acesso', methods=['POST'])
def acesso():
    nome = request.form.get('email')
    senha = request.form.get('senha')

    print(f"{nome} - {senha}")
    return redirect('/')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro/cadastrando', methods=['POST'])
def cadastrando():
    nome = request.form.get('name')
    email = request.form.get('email')
    senha = request.form.get('password')
    imagem_perfil = nome[0].upper()
    
    print(f"{nome} - {email} - {senha} - {imagem_perfil}")
    return redirect('/')