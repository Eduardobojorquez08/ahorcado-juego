from flask import Flask, render_template, request, session, redirect, url_for
import random
from database import get_db
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'Eduardoahorcado09'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jugar', methods=['POST'])
def jugar():
    db = get_db()
    palabras_base = db.execute("SELECT * FROM palabras").fetchall()
    db.close()

    palabra = random.choice(palabras_base)
    session['palabra'] = palabra['palabra']
    session['categoria'] = palabra['categoria']
    session['intentos'] = 6
    session['letras_usadas'] = []
    return redirect(url_for('partida'))

@app.route('/partida')
def partida():
    palabra = session['palabra']
    letras_usadas = session['letras_usadas']
    progreso = [letra if letra in letras_usadas else '_' for letra in palabra]
    gano = '_' not in progreso
    perdio = session['intentos'] == 0

    return render_template('partida.html',
    progreso=' '.join(progreso),
    intentos=session['intentos'],
    categoria=session['categoria'],
    letras_usadas=session['letras_usadas'],
    gano=gano,
    perdio=perdio
)

@app.route('/letra', methods=['POST'])
def letra():
    verificar = request.form['letra']
    palabra = session['palabra']
    letras_usadas = session['letras_usadas']

    if verificar in letras_usadas:       
        intentos = session['intentos']
        intentos -= 1
        session['intentos'] = intentos
    else:
        letras_usadas.append(verificar)  
        session['letras_usadas'] = letras_usadas

        if verificar not in palabra:     
            intentos = session['intentos']
            intentos -= 1
            session['intentos'] = intentos

    return redirect(url_for('partida'))
    

@app.route('/estado')
def estado():
    palabra = session['palabra']
    letras_usadas = session['letras_usadas']
    progreso = [letra if letra in letras_usadas else '_' for letra in palabra]
    gano = '_' not in progreso
    perdio = session['intentos'] == 0
    return jsonify(
        progreso=' '.join(progreso),
        intentos=session['intentos'],
        letras_usadas=letras_usadas,
        gano=gano,
        perdio=perdio,
        palabra=palabra
    )


if __name__ == '__main__':
    app.run(debug=True)