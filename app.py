from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
from users import usuarios # Dados de acesso

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

        if (username in usuarios) and password==usuarios[username][0]:
            global privilegio
            privilegio = 'Atendente' if usuarios[username][1] == 'a' else 'Veterinária(o)'
            return redirect(url_for('adm_painel', username=username, privilegio=privilegio))

    return render_template('adm-login.html')

@app.route('/painel-administrativo')
def adm_painel():
    return render_template('adm-painel.html', user=username, privilegio=privilegio)

@app.route('/chat')
def adm_chat():
    return render_template('adm-chat.html', user=username, privilegio=privilegio)

@app.route('/pets')
def adm_petsData():
    pets = pd.read_csv('./static/data/pets.csv')
    pets = pets.to_dict(orient='records') # Converte em lista de dicionários

    return render_template('adm-dataPets.html', user=username, pets=pets, privilegio=privilegio)

@app.route('/clientes')
def adm_clientesData():
    clientes = pd.read_csv('./static/data/clientes.csv')
    clientes = clientes.to_dict(orient='records')

    return render_template('adm-dataClientes.html', user=username, clientes=clientes, privilegio=privilegio)

@app.route('/consultas')
def adm_consultas():
    return render_template('adm-consultas.html', user=username, privilegio=privilegio)

@app.route('/configuracoes')
def adm_configs():
    return render_template('adm-configs.html', user=username, privilegio=privilegio, usuarios=usuarios)

@app.route('/exames')
def adm_exames():
    return render_template('adm-exames.html', user=username, privilegio=privilegio)


if __name__ == '__main__':
    app.run(debug=True)