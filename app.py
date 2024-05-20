from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre-nos')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)