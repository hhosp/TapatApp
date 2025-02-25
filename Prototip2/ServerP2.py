import dadesServer
from dadesServer import User,Child,Tap,Status,Role,Treatment
from flask import Flask, jsonify, request

#Bucle per comprovar que es llegeixen les dades de l'arxiu dadesServer.py
for user in dadesServer.users:
    print(user)

#Prova de la classe User
provaUser = User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(provaUser)

class DAOUsers:
    def __init__(self):
        self.users = dadesServer.users