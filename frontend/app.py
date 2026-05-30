from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'

# Banco de dados em memória simples
users_db = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email and email in users_db:
            session['user_email'] = email
            session['user_nome'] = users_db[email]['nome']
            session['user_mat'] = users_db[email]['matricula']
            return redirect(url_for('home'))
        else:
            error = "Email não encontrado. Faça seu cadastro primeiro!"
            
    if 'user_email' in session:
        return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        nome_completo = request.form.get('nome')
        curso = request.form.get('curso')
        
        if not nome_completo or not curso:
            error = "Todos os campos são obrigatórios."
        else:
            # Pegar primeiro nome e ultimo nome (sobrenome)
            partes = nome_completo.strip().split()
            nome = partes[0].lower()
            sobrenome = partes[-1].lower() if len(partes) > 1 else "sobrenome"
            
            # Gerar o email
            email = f"{nome}.{sobrenome}@{curso.lower()}.inatel.br"
            
            if email in users_db:
                error = f"O e-mail {email} já existe. Por favor, faça login."
            else:
                # Salvar no BD simulado
                users_db[email] = {
                    'nome': nome_completo,
                    'curso': curso.upper(),
                    'matricula': f"123 {curso.upper()}"
                }
                
                # Loga o usuário automaticamente
                session['user_email'] = email
                session['user_nome'] = nome_completo
                session['user_mat'] = users_db[email]['matricula']
                
                return redirect(url_for('home'))
            
    return render_template('register.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user_nome', None)
    session.pop('user_mat', None)
    session.pop('user_email', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', nome=session.get('user_nome'), matricula=session.get('user_mat'), email=session['user_email'])

@app.route('/about')
def about():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return render_template('about.html', nome=session.get('user_nome'), matricula=session.get('user_mat'), email=session['user_email'])

@app.route('/contact')
def contact():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html', nome=session.get('user_nome'), matricula=session.get('user_mat'), email=session['user_email'])

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
