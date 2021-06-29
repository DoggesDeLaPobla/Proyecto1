import os

file=open("sudo nano /etc/xdg/lxsession/LXDE-pi/autostart","a")

file.write("Prueba")

file.close()

print(os.path.abspath(os.getcwd()))