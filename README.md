# ℙ𝕣𝕠𝕪𝕖𝕔𝕥𝕠 𝔻𝕠𝕘𝕘𝕖𝕤𝔻𝕖𝕃𝕒ℙ𝕠𝕓𝕝𝕒🐕🦴
• Repositorio creado por el grupo "DoggesDeLaPobla"<br>

• Este proyecto utiliza diferente documentación y programas para su desarrollo 
Para etiquetar las imagenes que conforman el dataset nos basamos en el programa deasarrollado por: tzutalin
Github del programa: https://github.com/tzutalin/labelImg

• Donde procesamos el data set:<br>
  👉 Colab: https://colab.research.google.com/drive/1IaU5PR17KPp7z8Un1mfJLWBqYHGwD7sP?usp=sharing 👈
  
<------- Nube con más información e instrucctivos -------><br>
☁ https://usmcl-my.sharepoint.com/:f:/g/personal/ethan_leiva_usm_cl/ErvVWQQnTvZCmqCxm3eJ1PQB6-HL0ac2BCV6Gb5vJfv85Q?e=fD5lE9
  
# 𝕀𝕟𝕥𝕖𝕘𝕣𝕒𝕟𝕥𝕖𝕤 𝕪 𝕣𝕠𝕝𝕖𝕤


• Fabian Toro    🠒  202030017-8

• Ana Gonzalez   🠒  202130009-0

• Ethan Leiva    🠒  202129866-5

• Alicia Pereira 🠒  202130002-3



# 𝕆𝕣𝕚𝕘𝕖𝕟

• Nuestro proyecto tuvo origen al momento de encontrar una encuesta realizada a las personas en el año 2019, donde el 73% de los chilenos asegura tener un promedio de 2 mascotas en su hogar. Después de esto hicimos una lluvia de ideas sobre que inconvenientes o complicaciones se les proporcionan en su vida cotidiana, a lo que concluimos que una de las más grandes preocupaciones son cuando las mascotas salen fuera del hogar, debido a que elimina bastante tiempo el estar pendiente de ellos cuando se ecuentran en su momento de recreacion. Además concluimos que los perros y los gatos son las mascotas más frecuentes que salen sin supervisión constante por lo cual son los que predominaran en nuestro proyecto. 

# 𝔻𝕠𝕘𝕘𝕖𝕤𝔻𝕖𝕃𝕒ℙ𝕠𝕓𝕝𝕒

• Proyecto realizado por nuestro equipo para la asignatura IWG101 que consiste en una red neuronal capaz de identificar perros y gatos, con la finalidad de integrarse a una raspberry pi 4 modelo B asociada a una cámara y a un bot de telegram para poder genenrar un sistema de alerta inteligente (o automatización de una puerta en caso de ser posible) para darle más libertad a nuestras mascotas de movilizarse por la entradas del hogar. 

# ¿ℂ𝕠𝕞𝕠 𝔽𝕦𝕟𝕔𝕚𝕠𝕟𝕒?

• La cámara captura la imagen que es enviada a la raspberry pi 4 con el programa integrado, esta es analizada y en caso de reconocer a tu mascota enviara un aviso mediante un bot de telegram para que puedas abrir la puerta a tu mascota o en su defecto, si la puerta esta automatizada, se abra y cierre de forma automatica en el momento que la mascota entre. 

# 𝕀𝕟𝕤𝕥𝕒𝕝𝕒𝕔𝕚ó𝕟 𝕪 𝕗𝕦𝕟𝕔𝕚𝕠𝕟𝕒𝕞𝕚𝕖𝕟𝕥𝕠 𝕕𝕖𝕝 𝕡𝕣𝕠𝕘𝕣𝕒𝕞𝕒

• 𝗣𝗿𝗶𝗺𝗲𝗿𝗼 🠒 𝗰𝗹𝗼𝗻𝗮𝗺𝗼𝘀 𝗲𝗹 𝗿𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝗶𝗼 :
```
git clone https://github.com/DoggesDeLaPobla/Proyecto1.git
```

• 𝗦𝗲𝗴𝘂𝗻𝗱𝗼 🠒 𝗲𝗻𝘁𝗿𝗮𝗱𝗼𝘀 𝗮𝗹 𝗿𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝗶𝗼 𝗰𝗹𝗼𝗻𝗮𝗱𝗼 :
```
cd Proyecto1/
```
• 𝗧𝗲𝗿𝗰𝗲𝗿𝗼 🠒 𝗘𝗷𝗲𝗰𝘂𝘁𝗮𝗺𝗼𝘀 "𝗿𝗲𝗾𝘂𝗲𝗿𝗶𝗺𝗶𝗲𝗻𝘁𝗼𝘀.𝘀𝗵" :
```
sh requerimientos.sh
```
• 𝗙𝗶𝗻𝗮𝗹𝗺𝗲𝗻𝘁𝗲 🠒 𝗽𝗼𝗱𝗲𝗺𝗼𝘀 𝗲𝗷𝗲𝗰𝘂𝘁𝗮𝗿 𝗲𝗹 𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗮 :
```
sh iniciar.sh
```
• 𝗦𝗶 𝗱𝗲𝘀𝗲𝗮𝘀 𝗰𝗿𝗲𝗮𝗿 𝗲𝗹 𝗶𝗻𝗶𝗰𝗶𝗼 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗼 𝗱𝗲𝗹 𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗮 𝗽𝘂𝗲𝗱𝗲𝘀 𝘂𝘁𝗹𝗶𝘇𝗮𝗿 :
```
sudo python3 Auto.py
```
• 𝗬 𝗽𝗮𝗿𝗮 𝗲𝗹𝗶𝗺𝗶𝗻𝗮𝗿 𝗲𝗹 𝗶𝗻𝗶𝗰𝗶𝗼 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗰𝗼 :
```
sudo python3 DelAuto.py
```
