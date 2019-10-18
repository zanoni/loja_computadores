from flask import Flask, render_template, request, redirect
import MySQLdb

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

app.run()