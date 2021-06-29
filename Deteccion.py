######## Camara Detector de mascotas #########
#       By: DoggesDeLaPobla
#
#
#

#paquetes a utlizar
import os
import argparse
import cv2
import numpy as np
import sys
import time
from threading import Thread
import importlib.util
import telebot
from tensorflow.lite.python.interpreter import Interpreter

f = open("bot.key", "r")
key=f.read()
f.close()
bot = telebot.TeleBot(key)

categorias={"dog":"Perro","cat":"Gato"}

class VideoStream:
    """Controlador de camara"""
    def __init__(self,resolution=(640,480),framerate=30):
        #Inicializamos el stream de la camara
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3,resolution[0])
        ret = self.stream.set(4,resolution[1])
            
        # Leemos el primer frame
        (self.grabbed, self.frame) = self.stream.read()

	# Controlo si hay que detener la camara
        self.stopped = False

    def start(self):
	# Inicializar la camara
        Thread(target=self.update,args=()).start()
        return self

    def update(self):
        # Loop infinito hasta que se de la instrucción de detener
        while True:
            # Si hacemos stop liberamos la camara
            if self.stopped:
                # Cerramos por por completo la camara
                self.stream.release()
                return

            # Capturamos un fotograma desde la camara
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
	# devolvemos el frame ultimo
        return self.frame

    def stop(self):
	# Indicamos que queremos detener la camara
        self.stopped = True

# Define parametros de inicio
parser = argparse.ArgumentParser()
parser.add_argument('--Desarrollador', help='Activar modo desarrollador',
                    default='')

args = parser.parse_args()

Estado = bool(args.Desarrollador)
print(Estado)

MODEL_NAME = "Sample_TFLite_model"#carpeta del modelo
GRAPH_NAME = "detect.tflite"#los pesos del modelo
LABELMAP_NAME = "labelmap.txt"#labels del modelo
min_conf_threshold = 0.5 #Sensibilidad de configuración

imW, imH = 1280, 720 #resolución de la imagen
use_TPU = False



# Optenemos el path del directorio actual
CWD_PATH = os.getcwd()

# Sacamos el path del modelo lite
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,GRAPH_NAME)

# Sacamos el PATH de las etiquetas
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_NAME,LABELMAP_NAME)

# Cargamos las etiquetas
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# Eliminamos la etiqueta ??? de la primera linea
if labels[0] == '???':
    del(labels[0])

#Cargamos el modelo de Tensorflow Lite

interpreter = Interpreter(model_path=PATH_TO_CKPT)

interpreter.allocate_tensors()

# Extraemos los detalles del modelo
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

floating_model = (input_details[0]['dtype'] == np.float32)


input_mean = 127.5
input_std = 127.5

# Calculamops el framerate
frame_rate_calc = 1
freq = cv2.getTickFrequency()

# Inicializamos la camara
videostream = VideoStream(resolution=(imW,imH),framerate=30).start()
time.sleep(1)
a=100
try:
    while True:
        #abrimos el archivo con los usuarios
        f = open("usuarios.codec", "r")
        copia = f.readlines()
        f.close
        if a<100:
            a+=1
            print(a)

        t1 = cv2.getTickCount()

        # extraemos un frame
        frame1 = videostream.read()
        cv2.imwrite("frame1.jpg", frame1)

        # lo clonamos y le ajustamos la resolucion
        frame = frame1.copy()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized, axis=0)

        # Analizamos para determinar la red
        interpreter.set_tensor(input_details[0]['index'],input_data)
        interpreter.invoke()

        # Retrieve detection results
        boxes = interpreter.get_tensor(output_details[0]['index'])[0] # EL cuadrado de la posisión del objeto
        classes = interpreter.get_tensor(output_details[1]['index'])[0] # La clase del objeto
        scores = interpreter.get_tensor(output_details[2]['index'])[0] # Porcentaje de seguridad de la red
        #num = interpreter.get_tensor(output_details[3]['index'])[0]  #Total  de objetos detectados

        # Loop para recorrer todos los elementos encontrados
        for i in range(len(scores)):
            if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
                object_name = labels[int(classes[i])] # Extra el nombre del objeto
                if 'dog'==object_name or 'cat' == object_name:
                    

                    # Crea el rectangulo del objeto identificado
                    ymin = int(max(1,(boxes[i][0] * imH)))
                    xmin = int(max(1,(boxes[i][1] * imW)))
                    ymax = int(min(imH,(boxes[i][2] * imH)))
                    xmax = int(min(imW,(boxes[i][3] * imW)))
                    
                    cv2.rectangle(frame, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)

                    # dibuja el rectangulo
                    
                    label = '%s: %d%%' % (categorias[object_name], int(scores[i]*100)) # Pone el porcentaje de coincidencia
                    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # establece el tamaño de la letra
                    label_ymin = max(ymin, labelSize[1] + 10) # crea el tamaño del rectangulo
                    cv2.rectangle(frame, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Dibujamos el cuadrado finalmente
                    cv2.putText(frame, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # pone el texto en el rectangulo
                    
                    for i in copia:
                        if len(i.split(" "))>=6:
                            if i.split(" ")[5]=="Ambos" or  str(i.split(" ")[5]).count(categorias[object_name])>0 and a>99:
                                bot.send_message(i.split(" ")[3], "Hey "+i.split(" ")[1]+" creo que tu "+categorias[object_name]+" desea entrar, te mando foto")
                                cv2.imwrite("frame.jpg", frame)
                                bot.send_photo(i.split(" ")[3], open('frame.jpg','rb'))
                                a=0

        
        if Estado:
            # Contador de FPS
            cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
            # Mostramos los resultados
            cv2.imshow('Object detector', frame)

        # calculamos los FPS
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc= 1/time1

        if Estado:
            # Salimos con la letra e
            if cv2.waitKey(1) == ord('e'):
                cv2.destroyAllWindows()
                break
except:
    # Limpiamos
    videostream.stop()
videostream.stop()
cv2.destroyAllWindows()
