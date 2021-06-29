import os

file=open("/etc/xdg/lxsession/LXDE-pi/autostart","a")

file.write("Prueba")

file.close()

print(os.path.abspath(os.getcwd()))