import pickle

from wallcast_functions import *

def save_account_data(username, password):
    open('user_data.pickle', 'w+')
    user_data = {'username': username, 'password': password}

    with open('user_data.pickle', 'wb') as f:
        pickle.dump(user_data, f)
    show_account_data()

def show_account_data():
    with open('user_data.pickle', 'rb') as f:
        user_data = pickle.load(f)

    username = user_data['username']
    password = user_data['password']
    print(username, password)
    if session.query(User).filter_by(username=username, password=password).first():
        return username
    else:
        return False
