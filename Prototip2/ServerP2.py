import dadesServer
from dadesServer import User, Child, Tap, Status, Role, Treatment
from flask import Flask, jsonify, request

# Bucle per comprovar que es llegeixen les dades de l'arxiu dadesServer.py
for user in dadesServer.users:
    print(user)

# Prova de la classe User
provaUser = User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(provaUser)
# Prova de la classe Child
provaChild = Child(id="1", child_name="Mohamed", sleep_average="8", treatment_id="1", time="0")
print(provaChild)

class DAOUser:
    def __init__(self):
        self.users = dadesServer.users

    def getUserById(self, user_id):
        for user in self.users:
            if user_id == user.id:
                return user
        return None

    def getUserByCredentials(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

class DAOChild:
    def __init__(self):
        self.children = dadesServer.children

    def getChildByUserId(self, user_id):
        child_ids = [rel["child_id"] for rel in dadesServer.relation_user_child if rel["user_id"] == int(user_id)]
        children = [child for child in self.children if child.id in child_ids]
        return children
        
    def getTapByChildId(self, child_id):
        taps = [tap for tap in dadesServer.taps if tap.child_id == int(child_id)]
        return taps

app = Flask(__name__)
DAOUser = DAOUser()
DAOChild = DAOChild()

@app.route('/tapatapp/getUserByCredentials', methods=['GET'])
def getUserByCredentials():
    username = request.args.get('username')
    password = request.args.get('password')
    user = DAOUser.getUserByCredentials(username, password)
    if user:
        return jsonify(user.__dict__)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/tapatapp/getChildByUserId', methods=['GET'])
def getChildByUserId():
    user_id = request.args.get('user_id')
    children = DAOChild.getChildByUserId(user_id)
    if children:
        return jsonify([child.__dict__ for child in children])
    else:
        return jsonify({"error": "Children not found"}), 404

@app.route('/tapatapp/getTapByChildId', methods=['GET'])
def getTapByChildId():
    child_id = request.args.get('child_id')
    taps = DAOChild.getTapByChildId(child_id)
    if taps:
        return jsonify([tap.__dict__ for tap in taps])
    else:
        return jsonify({"error": "Taps not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)