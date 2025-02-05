from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import time

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour enregistrer un log de connexion
def enregistrer_log(ip_address, username, status):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (ip_address, username, status, timestamp) VALUES (?, ?, ?, ?)", 
                   (ip_address, username, status, int(time.time())))
    conn.commit()
    conn.close()

# Fonction pour compter les échecs récents en BDD (même IP + même utilisateur)
def nombre_echecs_recents(ip_address, username, periode=300):  # 300 secondes = 5 minutes
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    temps_limite = int(time.time()) - periode
    cursor.execute("""
        SELECT COUNT(*) FROM logs 
        WHERE ip_address = ? 
        AND username = ? 
        AND status = 'failure' 
        AND timestamp > ?
    """, (ip_address, username, temps_limite))
    
    nombre_echecs = cursor.fetchone()[0]
    conn.close()
    return nombre_echecs

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    ip_address = request.remote_addr  # Récupérer l'IP du client

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vérifier si l'utilisateur + IP ont trop d'échecs récents
        if nombre_echecs_recents(ip_address, username) >= 3:
            return "Trop de tentatives de connexion échouées. Veuillez réessayer plus tard.", 403

        if username == 'admin' and password == 'password':  # Remplace par une vraie vérification en BDD
            session['authentifie'] = True
            enregistrer_log(ip_address, username, 'success')
            return redirect(url_for('lecture'))
        else:
            enregistrer_log(ip_address, username, 'failure')
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)



if __name__ == "__main__":
    app.run(debug=True)
