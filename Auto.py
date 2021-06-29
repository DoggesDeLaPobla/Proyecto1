import os

file=open("/etc/xdg/lxsession/LXDE-pi/autostart","a")

file.write("@lxterminal -e sh "+os.path.abspath(os.getcwd())+"/iniciar.sh")

file.close()

file=open(os.path.abspath(os.getcwd())+"/iniciar.sh","w")

file.write("#!/bin/bash\n")
file.write("lxterminal -e python3 "+os.path.abspath(os.getcwd())+"/Bot.py\n")
file.write("lxterminal -e python3 "+os.path.abspath(os.getcwd())+"/Deteccion.py\n")

file.close()
