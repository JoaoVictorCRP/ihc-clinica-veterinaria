from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agendar-consulta')
def form_consulta():
    return render_template('form-consulta.html')

if __name__ == '__main__':
    app.run(debug=True)