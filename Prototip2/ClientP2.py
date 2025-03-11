import requests
from dadesServer import User, Child, Tap

class DAOUser:
    @staticmethod
    def getUserById(user_id):
        response = requests.get(f"http://localhost:5000/tapatapp/getUserById?user_id={user_id}")
        if response.status_code == 200:
            data = response.json()
            return User(data['id'], data['username'], data['password'], data['email'])
        else:
            return None

class DAOChild:
    @staticmethod
    def getChildByUserId(user_id):
        response = requests.get(f"http://localhost:5000/tapatapp/getChildByUserId?user_id={user_id}")
        if response.status_code == 200:
            children = []
            for data in response.json():
                children.append(Child(data['id'], data['child_name'], data['sleep_average'], data['treatment_id'], data['time']))
            return children
        else:
            return None

    @staticmethod
    def getTapByChildId(child_id):
        response = requests.get(f"http://localhost:5000/tapatapp/getTapByChildId?child_id={child_id}")
        if response.status_code == 200:
            taps = []
            for data in response.json():
                taps.append(Tap(data['id'], data['child_id'], data['status_id'], data['user_id'], data['init'], data['end']))
            return taps
        else:
            return None

class View:
    @staticmethod
    def requestUsername():
        return input("Enter username: ")

    @staticmethod
    def requestPassword():
        return input("Enter password: ")

    @staticmethod
    def login(username, password):
        response = requests.get(f"http://localhost:5000/tapatapp/getUserByCredentials?username={username}&password={password}")
        if response.status_code == 200:
            data = response.json()
            return User(data['id'], data['username'], data['password'], data['email'])
        else:
            print("Login failed")
            return None

    @staticmethod
    def showUserInfo(user):
        print(user)

    @staticmethod
    def showChildInfo(child):
        print(child)

    @staticmethod
    def showTapInfo(tap):
        print(tap)

# Ejemplo de uso
if __name__ == "__main__":
    username = View.requestUsername()
    password = View.requestPassword()
    user = View.login(username, password)
    if user:
        View.showUserInfo(user)
        children = DAOChild.getChildByUserId(user.user_id)
        if children:
            for child in children:
                View.showChildInfo(child)
                taps = DAOChild.getTapByChildId(child.child_id)
                if taps:
                    for tap in taps:
                        View.showTapInfo(tap)
                else:
                    print("No taps found for this child")
        else:
            print("No children found for this user")