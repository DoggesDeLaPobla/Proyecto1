# ℙ𝕣𝕠𝕪𝕖𝕔𝕥𝕠 𝔻𝕠𝕘𝕘𝕖𝕤𝔻𝕖𝕃𝕒ℙ𝕠𝕓𝕝𝕒🐕🦴
• Repositorio creado por el grupo "DoggesDeLaPobla"<br>

• Este proyecto utiliza diferente documentación y programas para su desarrollo 
Para etiquetar las imagenes que conforman el dataset nos basamos en el programa deasarrollado por: tzutalin
Github del programa: https://github.com/tzutalin/labelImg

• Donde procesamos el data set:<br>
  👉 Colab: https://colab.research.google.com/drive/1IaU5PR17KPp7z8Un1mfJLWBqYHGwD7sP?usp=sharing 👈
  
<------- Nube con más información e instrucctivos -------><br>
☁ https://usmcl-my.sharepoint.com/:f:/g/personal/ethan_leiva_usm_cl/ErvVWQQnTvZCmqCxm3eJ1PQB6-HL0ac2BCV6Gb5vJfv85Q?e=fD5lE9
  
# Intregrantes y roles


• Fabian Toro    🠒 202030017-8

• Ana Gonzalez   🠒 202130009-0

• Ethan Leiva    🠒 202129866-5

• Alicia Pereira 🠒 202130002-3



# Origen

• Nuestro proyecto tuvo origen al momento de encontrar una encuesta realizada a las personas en el año 2019, donde el 73% de los chilenos asegura tener un promedio de 2 mascotas en su hogar. Después de esto hicimos una lluvia de ideas sobre que inconvenientes o complicaciones se les proporcionan en su vida cotidiana, a lo que concluimos que una de las más grandes preocupaciones son cuando las mascotas salen fuera del hogar, debido a que elimina bastante tiempo el estar pendiente de ellos cuando se ecuentran en su momento de recreacion. Además concluimos que los perros y los gatos son las mascotas más frecuentes que salen sin supervisión constante por lo cual son los que predominaran en nuestro proyecto. 

# DoggesDeLaPobla

• Proyecto realizado por nuestro equipo para la asignatura IWG101 que consiste en una red neuronal capaz de identificar perros y gatos, con la finalidad de integrarse a una raspberry pi 4 modelo B asociada a una cámara y a un bot de telegram para poder genenrar un sistema de alerta inteligente (o automatización de una puerta en caso de ser posible) para darle más libertad a nuestras mascotas de movilizarse por la entradas del hogar. 

# Como Funciona 

• La cámara captura la imagen que es enviada a la raspberry pi 4 con el programa integrado, esta es analizada y en caso de reconocer a tu mascota enviara un aviso mediante un bot de telegram para que puedas abrir la puerta a tu mascota o en su defecto, si la puerta esta automatizada, se abra y cierre de forma automatica en el momento que la mascota entre. 

# Instalación y funcionamiento del programa

• Primero clonamos el repositorio
```
git clone https://github.com/DoggesDeLaPobla/Proyecto1.git
```

• Segundo entrados al repositorio clonado
```
cd Proyecto1/
```
• Tercero

• Ejecutamos "requerimientos.sh"
```
sh requerimientos.sh
```
• Finalmente podemos ejecutar el programa
```
sh iniciar.sh
```
• Si deseas crear el inicio automatico del programa puedes utlizar
```
sudo python3 Auto.py
```
• Y para eliminar el inicio automatico
```
sudo python3 DelAuto.py
```
