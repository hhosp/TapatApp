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
                return username
            else:
                return "no trobat"
            
daoUser = DAOUsers()

print(daoUser.getUserByUsername("notrobat"))
print(daoUser.getUserByUsername("usuari1"))

app = Flask(__name__)

@app.route('/llista', methods=['GET'])
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)