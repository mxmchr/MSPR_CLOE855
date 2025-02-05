import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('database.db')

# Exécution du script de création du schéma (s'il y en a un)
with open('schema.sql') as f:
    connection.executescript(f.read())

# Création de la table pour les logs des connexions
cur = connection.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS logs_connexions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    date_connexion DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Insertion de données dans la table clients
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# Insertion de données dans la table des logs de connexions (log fictif pour l'exemple)
cur.execute("INSERT INTO logs_connexions (username, ip_address) VALUES (?, ?)", ('admin', '192.168.1.1'))
cur.execute("INSERT INTO logs_connexions (username, ip_address) VALUES (?, ?)", ('admin', '192.168.1.2'))
cur.execute("INSERT INTO logs_connexions (username, ip_address) VALUES (?, ?)", ('admin', '192.168.1.3'))

# Commit des changements
connection.commit()

# Fermeture de la connexion
connection.close()
