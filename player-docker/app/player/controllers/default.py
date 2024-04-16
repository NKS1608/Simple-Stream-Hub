from player import app
from flask import url_for

@app.route('/')
def index():
    return 'Não tem nada pra você por aqui, desculpe.'

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='image/favicon.ico')