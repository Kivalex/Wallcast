import getpass
import os

import pyaudio
import wave
import keyboard

disk = os.getenv("SystemDrive")
user_login = getpass.getuser()
logo_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\logo_wallcast.png")
ava_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\ava_wallcast.png")
kolokol_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\kolokol_wallcast.png")
ava_kivalex = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\ava_kivalex.jpg")
open_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\open_eye.png")
closed_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\closed_eye.png")



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

    print("Нажмите клавишу для начала записи")
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
record_audio("my_audio.wav")