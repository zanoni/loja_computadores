from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

app.run()

















