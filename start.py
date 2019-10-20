from flask import Flask, render_template, request, redirect, session
import MySQLdb
from models.cliente import Cliente
from dao.cliente_dao import ClienteDao 
from dao.produto_dao import ProdutoDao
from models.produto import Produto


app= Flask(__name__)
app.secret_key = 'Lojinha'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticacao():
    cliente_dao = ClienteDao()
    cli = Cliente()
    try:
        cliente = cliente_dao.select_por_email(request.form['usuario'])    
        session['logado'] = cli.autentica(cliente, request.form['senha'])
        return render_template('compra.html')
    except:
        return 'Login Inválido'

@app.route('/cadastrar-cliente')
def cadastro_cliente():
    return render_template('cadastro-cliente.html')


@app.route('/cadastrar-cliente-salvar', methods=['POST'])
def cadastro_cliente_salvar():
    cliente = Cliente()
    dao_cliente = ClienteDao()
    try:
        cliente.cadastra_cliente(cliente, request.form['nome'], request.form['email'], request.form['senha'])#'teste', 'teste@teste.com', 'teste'
        dao_cliente.insert_cliente(cliente)

        return redirect('login.html')
    except:
        return 'Erro no cadastro'
####################################################################### 

@app.route('/comprar')
def compra():

    return render_template('compra.html')

@app.route('/comprar/salvar', methods = ['POST'])
def compra_salvar():

    return redirect('compra.html')

@app.route('/lista-compras')
def lista_compras():
    return render_template('lista-compras.html')



app.run()