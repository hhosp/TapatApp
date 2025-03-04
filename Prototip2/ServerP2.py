import dadesServer
from dadesServer import User,Child,Tap,Status,Role,Treatment
from flask import Flask, jsonify, request

#Bucle per comprovar que es llegeixen les dades de l'arxiu dadesServer.py
for user in dadesServer.users:
    print(user)

#Prova de la classe User
provaUser = User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(provaUser)
#Prova de la classe Child
provaChild = Child(id=1, child_name = "Mohamed", sleep_average = 8, treatment_id = 1, time = 0)
print(provaChild)

class DAOUser:
    def __init__(self):
        self.users = dadesServer.users

    def getUserById(self,user_id):
        for user in self.users:
            if user_id == user.id:
                return user
            return None

class DAOChild:
    def __init__(self):
        self.children = dadesServer.children

    def getChildByUserId(self, user_id):
        child_ids = [rel["child_id"] for rel in dades.relation_user_child if rel["user_id"] == user_id]
        return [child for child in self.children if child.id in child_ids]
        
    def getTapByChild(self, child_id):
        pass 