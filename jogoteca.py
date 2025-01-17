from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo: 
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

class Usuario:
     def __init__(self, nome, nickname, senha):
        self.nome = nome 
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario('joao', "jj", 'alohomora')
usuario2 = Usuario('kamila', 'mila', 'paozinho')
usuario3 = Usuario('guilherme', 'cake', 'python')

usuarios = { usuario1.nickname: usuario1, usuario2.nickname: usuario2, usuario3.nickname: usuario3 }

jogos1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogos2 = Jogo('God of War', 'rack n slash', 'PS2')
jogos3 = Jogo('mortal kombat', 'luta', 'PS2')

lista = [jogos1, jogos2, jogos3]


app = Flask(__name__)
app.secret_key = 'willian'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
     
     if request.form['usuario'] in usuarios:
         usuario = usuarios[request.form['usuario']]
         if request.form['senha'] == usuario.senha:
             session['usuario_logado'] = usuario.nickname
             flash (usuario.nickname + ' logado com sucesso!')
             return redirect(url_for('novo'))
     else:
          flash('Usuário não logado ')
          return redirect(url_for('login'))

@app.route('/logout')
def logout():
     session['usuario_logado'] = None
     flash('Logout efetuado com sucesso!')
     return redirect(url_for('index'))

app.run(debug=True)