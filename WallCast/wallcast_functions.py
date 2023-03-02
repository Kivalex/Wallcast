import getpass
import os
import re

from WallCast.wallcast_BD import *

import pyaudio
import wave
import keyboard

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
    if not re.search(r'[!@#^*]', text):  # Проверка наличия специального символа
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

'''Запись аудио'''
def record_audio(filename):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 600

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Нажмите клавишу enter для начала записи")
    keyboard.wait('enter')

    frames = []


    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('q'):
            print("Recording stopped.")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Saving recording...")

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Recording saved as", filename)

'''Добавление пользователя в базу данных'''
def new_user(username, password):
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()

    users = session.query(User).all()
    for user in users:
        print(user.username, user.password)

'''Проверка наличия имени пользователя в базе данных'''
def validate_name(text):
    if not re.search(r'[a-zA-Z]', text):  # Проверка наличия латинской буквы
        return False
    if re.search(r'[а-яА-Я]', text):    # Проверка наличия русских букв
        return False
    existing_user = session.query(User).filter_by(username=text).first()    #Проверка в БД
    if existing_user:
        return False
    else:
        return True

def delet_user(name):   # Удаляет пользователя из БД
    user_to_delete = session.query(User).filter_by(username=name).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f'Пользователь {user_to_delete.username} удален из базы данных')
    else:
        print('Пользователь с таким именем не найден в базе данных')
