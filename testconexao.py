from flask import Flask, render_template, request, redirect
from models.produto import Produto
import MySQLdb

##produto
app = Flask(__name__)
img_produto = []
def imagem_produto_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae11", passwd="grupo06", database="zuplae11")
    cursor = conexao.cursor()
    cursor.execute('SELECT Imagem FROM Produto') 
    img_produto = []
    for i in cursor.fetchall():
        produto = Produto()
        produto.img = i
        img_produto.append(produto.img)
    conexao.close()
    return img_produto


@app.route('/form/test')
def imagem_test():
    img_test = imagem_produto_db()
    return render_template('teste.html',img_test = img_test)

    









































app.run()







