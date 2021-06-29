import os

file=open("/etc/xdg/lxsession/LXDE-pi/autostart","a")

file.write("lxterminal -e sh "+os.path.abspath(os.getcwd())+"/iniciar.sh")

file.close()