from flask import Flask, request, jsonify

class User:
    def __init__(self, id, user, password, email):
        self.id = id
        self.user = user
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + ", Username: " + self.user + ", Password: " + self.password + ", Email: " + self.email

listUsers = [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2, "usuari2", "123", "user2@proven.cat"),
    User(3, "usuari3", "12", "admin@proven.cat")
]

class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def getUserByUsername(self,username):
        for u in listUsers:
            if (u.user == username):
                return u.__dict__
        else:
            return None
            
daoUser = DAOUsers()

app = Flask(__name__)


@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n=str(request.args.get('name'))
    email = str(request.args.get('email'))
    return "Hello World: Nom: " + n + " : email: " + email

@app.route('/prototip/getuser/', defaults={'username': None}, methods=['GET'])
@app.route('/prototip/getuser/<string:username>', methods=['GET'])
def prototipGetUser(username):
    try:
        user = daoUser.getUserByUsername(username)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error":f"User '{username}' not found"}), 404
    except Exception as e:
        return jsonify({"error": "Error inesperat", "details": str(e)}),500

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port="10050")



