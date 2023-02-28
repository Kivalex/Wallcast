import getpass
import os
path = "\\\\PycharmProjects\\\\pythonProject\\\\WallCast\\\\"
disk = os.getenv("SystemDrive")
user_login = getpass.getuser()
logo_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path +"logo_wallcast.png")
ava_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path + "ava_wallcast.png")
kolokol_wallcast = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path + "kolokol_wallcast.png")
ava_kivalex = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path + "ava_kivalex.jpg")
open_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path + "open_eye.png")
closed_eye = str(str(disk) + "\\\\" + "Users" + "\\\\" + str(user_login) + path + "closed_eye.png")
print(closed_eye)
