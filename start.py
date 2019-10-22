from flask import Flask, render_template, request, redirect, session
import MySQLdb
import json
from models.cliente import Cliente
from dao.cliente_dao import ClienteDao 
from dao.produto_dao import ProdutoDao
from models.produto import Produto
from dao.compra_dao import CompraDao
from models.itens_compra import ItensCompra
from models.compra import Compra
from dao.item_compra_dao import ItemCompraDao




app= Flask(__name__)
app.secret_key = 'LojinhaPC'


@app.route('/')
def cadastro():
    return render_template('cadastro-cliente.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/autenticar', methods=['POST'])
def autenticacao():
    cliente_dao = ClienteDao()
    cli = Cliente()
    try:
        cliente = cliente_dao.select_por_email('lais@teste.com')    #request.form['usuario']
        session['logado'] = cli.autentica(cliente, '1234')  #cliente, request.form['senha']
        
        return redirect('/home')
    except:
        return 'Login Inválido'


@app.route('/cadastrar-cliente-salvar', methods=['POST'])
def cadastro_cliente_salvar():
    cliente = Cliente()
    dao_cliente = ClienteDao()
    try:
        cliente.cadastra_cliente(cliente, request.form['nome'], request.form['email'], request.form['senha'])
        dao_cliente.insert_cliente(cliente)

        return redirect('/login')
    except:
        return 'Erro no cadastro'
####################################################################### 

@app.route('/comprar')
def comprar():
    dao_produto = ProdutoDao()
    produtos = dao_produto.select_produtos()    
    
    return render_template('compra.html', produtos = produtos)


@app.route('/comprar/salvar')#, methods=['POST']
def compra_salvar():

    try:
        dao_compra = CompraDao()    
        monta_ls = ItensCompra()
        compras = Compra()
        cliente_dao = ClienteDao()
        produtos_dao = ProdutoDao()
        dao_item_compra = ItemCompraDao()

        produtos_selecionados = monta_ls.monta_lista(request.form['processadores'], request.form['placa_mae'], request.form['memoria_ram'], request.form['placa_de_video'], request.form['hd'], request.form['gabinete'], request.form['fonte'])
        produtos_bd = []
        for i in produtos_selecionados:
            produtos_bd.append(produtos_dao.select_produto_por_id(i))

        valor_total = compras.calcula_total(produtos_bd)
            
        cliente_dict = json.loads(session['logado'])
        email_cliente = cliente_dict["_Cliente__email"]
        cliente = cliente_dao.select_por_email(email_cliente)
        id_cliente = cliente[0][0]

        id_compra = dao_compra.insert_compra(valor_total, id_cliente)

        dao_item_compra.salva_produtos_compra(produtos_bd, id_compra)
    
    except:
        print('Deu ruim!!!!!!!!!!!!!!!')
   
    return redirect('compra.html')

@app.route('/lista-compras')
def lista_compras():    

    #realizar um group by dos produtos pelo id da compra buscando pelo id do cliente
    return render_template('lista-compras.html')


@app.route('/alterar-cliente')
def alterar_cliente():
    
    cliente_dict = json.loads(session['logado'])
    email_cliente = cliente_dict["_Cliente__email"]
   

@app.route('/sair')
def sair():
    session['logado'] = None
    return redirect('/')


app.run()