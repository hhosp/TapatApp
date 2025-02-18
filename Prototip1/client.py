import requests

class User:
    def __init__(self, id, user, password, email):
        self.id = id
        self.user = user
        self.password = password
        self.email = email

    def __str__(self):
        return "Id: " + str(self.id) + ", Username: " + self.user + ", Password: " + self.password + ", Email: " + self.email

class DaoUser:
    def __init__(self, username):
        self.username = username
    
    def getUserByUsername(self, username):
        response = requests.get(f'http://localhost:10050/prototip1/getuser?username={username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None

class View:
    def __init__(self, username):
        self.username = username

    def getUsernameByConsole():
        username = str(input("ENTER USERNAME: "))
        return username
    def showInfoUser(username):
        user = DaoUser.getUserByUsername(username)
        if user:
            print(f"User Info: {user}")
        else:
            print(f"User with username {username} not found")
    def showInfoError(error):
        return error

class Error:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return "ERROR, Code: " + str(self.code) + ". Description: " + self.description

error1 = Error(404, "Not found")
print(View.showInfoError(error1))

