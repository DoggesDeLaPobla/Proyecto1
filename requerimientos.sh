#!/bin/bash

# Paquetes requeridos para opencv

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools libatlas-base-dev

# Instalamos la version de opencv 3.4
pip3 install opencv-python==3.4.6.27
#instalamos telegram y telegram bot para generar el bot que procesa y envia los mensajes
pip3 install python-telegram-bot --upgrade
pip3 install pyTelegramBotAPI

#instalamos tensorflow la versión 1.14
pip3 install tensorflow==1.14

