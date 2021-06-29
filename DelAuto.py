import os

file=open("/etc/xdg/lxsession/LXDE-pi/autostart","r").readlines()

copy=""
for i in file:
    if i.count(os.path.abspath(os.getcwd()))<1:
        copy+=i
        
file=open("/etc/xdg/lxsession/LXDE-pi/autostart","w")

file.write(copy)

file.close()