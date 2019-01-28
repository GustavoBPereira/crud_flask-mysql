from flask import Flask, render_template, url_for, redirect, request
import mysql.connector
from dao import LivroDao

cnx = mysql.connector.connect(user='gustavo', password='',
                                 database='altar_dos_livros')
livros = LivroDao(cnx)

app = Flask(__name__)
app.secret_key = 'phi'

@app.route('/')
def index():
	lista = livros.read_all()
	return render_template('index.html', lista=lista)

@app.route('/delete/<int:id>')
def delete(id):
	livros.delete(id)
	return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST',])
def create():
	return render_template('create.html')

@app.route('/generate', methods=['POST',])
def generate():
	titulo  = request.form['titulo']
	autor   = request.form['autor']
	editora = request.form['editora']
	livros.create(titulo,autor,editora)
	return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
	lista = livros.read_one(id)
	return render_template('edit.html', lista=lista)

@app.route('/change', methods=['POST',])
def change():
	titulo  = str(request.form['titulo'])
	autor   = str(request.form['autor'])
	editora = str(request.form['editora'])
	id   	= str(request.form['id'])
	livros.update(id,titulo,autor,editora)
	return redirect(url_for('index'))
	
app.run(debug=True)
