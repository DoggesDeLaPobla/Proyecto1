# Proyecto DoggesDeLaPobla🐕🦴
Repositorio creado por el grupo "DoggesDeLaPobla"<br>

Este proyecto utiliza diferente documentación y programas para su desarrollo 
Para etiquetar las imagenes que conforman el dataset nos basamos en el programa deasarrollado por: tzutalin
Github del programa: https://github.com/tzutalin/labelImg

Donde procesamos el data set:<br>
  👉 Colab: https://colab.research.google.com/drive/1IaU5PR17KPp7z8Un1mfJLWBqYHGwD7sP?usp=sharing 👈
  

<------- Nube con más información e instrucctivos -------><br>
☁ https://usmcl-my.sharepoint.com/:f:/g/personal/ethan_leiva_usm_cl/ErvVWQQnTvZCmqCxm3eJ1PQB6-HL0ac2BCV6Gb5vJfv85Q?e=fD5lE9

# Origen

Nuestro proyecto tuvo origen al momento de investigar y encontrar una encuesta realizada a las personas en el año 2019, donde el 73% de los chilenos asegura tener un promedio de 2 mascotas en su hogar. Luego de esto hicimos una lluvia de ideas sobre que problemas o complicaciones se les dan en su cotidiano vivir, a lo cual concluimos que una de las mayores preocupaciones son cuando la mascota sale fuera del hogar, ya que quita bastante tiempo el estar pendiente de la entrada al momento en que su compañero esté de vuelta. Además concluimos que los perros y los gatos son las mascotas más comunes que salen sin supervisión constante. Por lo tanto, para esto llegamos a la conclusión de crear una red neuronal, la cual a través de mensajes por "Telegram" le dará aviso al dueño que su mascota se encuentra en la entrada esperando.

# DoggesDeLaPobla

Proyecto realizado para la asignatura Introducción a la ingeniería telemática en el que nosotros, grupo uno, desarrollamos una red neuronal capaz identificar perros y gatos, esto con la finalidad de integrarse a una raspberry pi 4 modelo B asociada a una cámara y a un bot de telegram para poder genenrar un sistema de alerta inteligente (o automatización de una puerta en caso de ser posible) para darle más libertad a nuestras mascotas de movilizarse por la entradas del hogar. En resumidas cuentas, la cámara captura la imagen que es enviada a la raspberry pi con el programa integrado, esta es analizada y en caso de reconocer a tu mascota enviara un aviso mediante un bot de telegam para que puedas abrir la puerta a tu mascota o en su defecto, si la puerta esta automatizada, se abra y cierre de forma automatica en el momento que la mascota entre. 

# Instalación y funcionamiento del programa

Primero clonamos el repositorio

git clone https://github.com/DoggesDeLaPobla/Proyecto1.git

Segundo entrados al repositorio clonado

cd cd Proyecto1/

Tercero

Ejecutamos "requerimientos.sh"

sh requerimientos.sh

Finalmente podemos ejecutar el programa