import requests

class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"User(id={self.user_id}, username={self.username}, email={self.email})"

class Child:
    def __init__(self, child_id, child_name, sleep_average, treatment, time):
        self.child_id = child_id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"Child(id={self.child_id}, name={self.child_name}, sleep_average={self.sleep_average}, treatment={self.treatment}, time={self.time})"

class Tap:
    def __init__(self, tap_id, child_id, status, user_id, init, end):
        self.tap_id = tap_id
        self.child_id = child_id
        self.status = status
        self.user_id = user_id
        self.init = init
        self.end = end

    def __str__(self):
        return f"Tap(id={self.tap_id}, child_id={self.child_id}, status={self.status}, user_id={self.user_id}, init={self.init}, end={self.end})"

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