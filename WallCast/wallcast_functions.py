import getpass
import os
import re

'''Путь к файлам'''
disk = os.getenv("SystemDrive")
user_login = getpass.getuser()
logo_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\logo_wallcast.png")
ava_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\ava_wallcast.png")
kolokol_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\kolokol_wallcast.png")
ava_kivalex = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\ava_kivalex.jpg")
open_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\open_eye.png")
closed_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\closed_eye.png")

'''Проверка пароля на наличие необходимых знаков'''
def validate_password(text):
    if not re.search(r'\d', text):  # Проверка наличия цифры
        return False
    if not re.search(r'[!@#^*]', text):  # Проверка наличия специального символа
        return False
    if not re.search(r'[a-zA-Z]', text):  # Проверка наличия латинской буквы
        return False
    if not re.search(r'[A-Z]', text):  # Проверка наличия латинской буквы
        return False
    if len(text) < 6 or len(text) > 18:
        return False
    return True

def validate_name(text):
    pass
