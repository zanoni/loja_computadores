from flask import Flask, render_template, request, redirect, session
import MySQLdb
from models.cliente import Cliente
from dao.cliente_dao import ClienteDao 
from dao.produto_dao import ProdutoDao
from models.produto import Produto
from dao.compra_dao import CompraDao


app= Flask(__name__)
app.secret_key = 'LojinhaPC'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar')#, methods=['POST']
def autenticacao():
    cliente_dao = ClienteDao()
    cli = Cliente()
    try:
        cliente = cliente_dao.select_por_email('lais@teste.com')    #request.form['usuario']
        session['logado'] = cli.autentica(cliente, '1234')  #cliente, request.form['senha']
        print(session['logado'])
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
        cliente.cadastra_cliente(cliente, request.form['nome'], request.form['email'], request.form['senha'])
        dao_cliente.insert_cliente(cliente)

        return redirect('login.html')
    except:
        return 'Erro no cadastro'
####################################################################### 

@app.route('/comprar')
def comprar():
    dao_produto = ProdutoDao()
    produtos = dao_produto.select_produtos(1)
    return render_template('compra.html', produtos = produtos)

@app.route('/comprar/salvar', methods=['POST'])
def compra_salvar():
    dao_compra = CompraDao()
    #receber a lista com os produtos selecionados no front (id dos produtos)
    compra = dao_compra.insert_compra(200.00, 2) # Criar e Chamar o método que calcula o valor total e pegar o id do cliente na sessao usando select_por_email(self, email)
    #criar os itens da compra e adicionar um a um no banco de dados
    return redirect('compra.html')

@app.route('/lista-compras')
def lista_compras():
    #realizar um group by dos produtos pelo id da compra buscando pelo id do cliente
    return render_template('lista-compras.html')



app.run()