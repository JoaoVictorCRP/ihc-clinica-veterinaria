from flask import Flask, render_template, request, url_for, redirect

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

# Versão Secretária/Veterinário
@app.route('/adm-login', methods =['POST',  'GET'])
def adm():

    if request.method == 'POST':
        user = request.form['username']        
        password = request.form['password']

        print(user, password)
        if user and password: # Obviamente, teríamos uma validação no BD aqui, mas como é um protótipo, isso não é necessário.
            return render_template ('adm-painel.html', user=user)

    return render_template('adm-login.html')

if __name__ == '__main__':
    app.run(debug=True)