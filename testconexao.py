from flask import Flask, render_template, request, redirect
import MySQLdb

##produto

def imagem_produto_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae11", passwd="grupo06", database="zuplae11")
    cursor = conexao.cursor()
    img_produto = cursor.execute("SELECT Imagem FROM zuplae11.Produto WHERE ID=1;")    
    conexao.close()
    return img_produto



