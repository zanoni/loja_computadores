from flask import Flask, render_template, request, redirect
import MySQLdb

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['Post'])
def autenticacao():
    if autentica(form.request['usuario'], form.request['senha']):
        return render_template('login.html')
    return 'Login Inválido'

@app.route('/cadastrar-cliente')
def cadastro_cliente():
    return 'Cadastro cliente' #render_template('cadastro-cliente.html')

@app.route('/cadastrar-cliente-salvar', methods=['POST'])
def cadastro_cliente_salvar():
    return redirect('')

@app.route('/comprar')
def comprar():
    return render_template('compra.html')

@app.route('/lista-compras')
def lista_compras():
    return render_template('lista-compras.html')



app.run()