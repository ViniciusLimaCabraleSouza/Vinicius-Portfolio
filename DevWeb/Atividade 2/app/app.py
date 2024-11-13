from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

#config do BD
db_config = {
    'user': os.environ.get('root'),
    'password': os.environ.get('admin'),
    'host': os.environ.get('localhost:3306'),
    'database': 'pagina_contatos' #meu banco lindo maravilhoso
}

#conecta o banco
def get_db_connection():
    return mysql.connector.connect(**db_config)

#salvar dados de contato
@app.route('listar_contatos.html', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contatos (nome, email, assunto, mensagem) VALUES (%s, %s, %s, %s)",(nome, email, assunto, mensagem)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('listar_contatos.html'))

#listar registros
@app.route('listar_contatos.html')
def listar_contatos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contato")
    contatos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('listar_contatos.html', contatos=contatos)

#executar o servidor
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)