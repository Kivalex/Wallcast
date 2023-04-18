import pickle
from wallcast_functions import *

"""Все аккаунты"""
def save_account_data(username, password):  # Проверка наличия данных в файле
    search_data = {'username': username, 'password': password}

    with open('user_data.pickle', 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                print(data)
                print(search_data)
                if data == search_data:
                    return False
        except EOFError:
            return load_user_data(username, password)

def load_user_data(username, password):
    user_data = {'username': username, 'password': password}

    with open('user_data.pickle', 'ab') as f:
        pickle.dump(user_data, f)
    show_account_data()


def show_account_data():
    try:
        with open('user_data.pickle', 'rb') as file:
            try:
                while True:
                    data = pickle.load(file)
                    print(data["username"], data["password"])
            except EOFError:
                pass
    except:
        open('user_data.pickle', 'x')



"""Прошлый вход"""
def save_last_log_in(username, password):
    data = {'username': username, 'password': password}
    with open('last_user.pickle', 'wb') as file:
        pickle.dump(data, file)
    if username and password != ' ':
        save_account_data(username, password)
    show_last_log_in()

def show_last_log_in():
    with open('last_user.pickle', 'rb') as file:
        try:
            while True:
                data = pickle.load(file)
                return  data['username']
        except EOFError:
            return False

print('All Logs')
show_account_data()
print('------------------\n', 'Last Log')
print(show_last_log_in())