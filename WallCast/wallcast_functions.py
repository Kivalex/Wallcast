import os
import re

from wallcast_BD import *

os.path.abspath('logo_wallcast.png')

'''Получение пути к файлам'''
logo_wallcast = str(os.path.abspath('logo_wallcast.png'))
ava_wallcast = str(os.path.abspath('ava_wallcast.png'))
kolokol_wallcast = str(os.path.abspath('kolokol_wallcast.png'))
ava_kivalex = str(os.path.abspath('ava_wallcast.png'))
open_eye = str(os.path.abspath('open_eye.png'))
closed_eye = str(os.path.abspath('closed_eye.png'))

'''Проверка пароля на наличие необходимых знаков'''
def validate_password(text):
    if not re.search(r'\d', text):  # Проверка наличия цифры
        return False
    if not re.search(r'[a-zA-Z]', text):  # Проверка наличия латинской буквы
        return False
    if re.search(r'[а-яА-Я]', text):    # Проверка наличия русских букв
        return False
    if not re.search(r'[A-Z]', text):  # Проверка наличия латинской буквы
        return False
    if len(text) < 6 or len(text) > 18:
        return False
    return True


def wallcast_log_in_name_check(text):
    nicname_in_BD = session.query(User).filter_by(username=text).first()
    if nicname_in_BD:
        return True
    else:
        return False

'''Проверка имени пользователя на правильность'''
def validate_name(text):
    if text == None:
        return False
    if re.search('[@_!#$%^&*()<>?/\|}{~:]', text):  # Проверка на наличие специальных символов
        return False
    if not re.search(r'[a-zA-Z]', text):  # Проверка наличия латинской буквы
        return False
    if re.search(r'[а-яА-Я]', text):    # Проверка наличия русских букв
        return False
    existing_user = session.query(User).filter_by(username=text).first()    #Проверка в БД
    if existing_user:
        return False
    else:
        return True

'''Функции Базы Данных'''
def new_user(username, password):   #Добавление нового пользователя в БД
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()

    users = session.query(User).all()
    for user in users:
        print(user.username, user.password)

def delet_user(name):   # Удаляет пользователя из БД
    user_to_delete = session.query(User).filter_by(username=name).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f'Пользователь {user_to_delete.username} удален из базы данных')
    else:
        print('Пользователь с таким именем не найден в базе данных')
