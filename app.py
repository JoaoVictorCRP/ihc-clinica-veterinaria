from flask import Flask, render_template, request, url_for, redirect
import pandas as pd

app = Flask(__name__)
app.config['DEBUG'] = True

# Versão cliente
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre-nos')
def sobre():
    return render_template('sobre.html')

@app.route('/pagamento')
def info_pagamento():
    return render_template('pagamento.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')

# Versão Administrativa
@app.route('/adm-login', methods =['POST',  'GET'])
def adm():

    if request.method == 'POST':
        global username
        username = request.form['username']        
        password = request.form['password']

        if username and password: # Obviamente, teríamos uma validação no BD aqui, mas como é um protótipo, isso não é necessário.
            return redirect(url_for('adm_painel', username=username))

    return render_template('adm-login.html')

@app.route('/painel-administrativo')
def adm_painel():
    username = request.args.get('username')
    return render_template('adm-painel.html', user=username)

@app.route('/chat')
def adm_chat():
    return render_template('adm-chat.html', user=username)

@app.route('/pets')
def adm_petsData():
    pets = pd.read_csv('./static/data/pets.csv') # Lendo csv de dados
    pets = pets.to_dict(orient='records') # convertendo em lista de dicionários

    return render_template('adm-petsData.html', user=username, pets=pets)

@app.route('/clientes')
def adm_clientesData():
    clientes = pd.read_csv('./static/data/clientes.csv')
    clientes = clientes.to_dict(orient='records')

    return render_template('adm-clientesData.html', user=username, clientes=clientes)


if __name__ == '__main__':
    app.run(debug=True)