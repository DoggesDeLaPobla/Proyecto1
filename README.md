# ๐ฃ๐ฟ๐ผ๐๐ฒ๐ฐ๐๐ผ ๐๐ผ๐ด๐ด๐ฒ๐๐๐ฒ๐๐ฎ๐ฃ๐ผ๐ฏ๐น๐ฎ๐๐ฆด
โข Repositorio creado por el grupo "DoggesDeLaPobla"<br>

โข Este proyecto utiliza diferente documentaciรณn y programas para su desarrollo 
Para etiquetar las imagenes que conforman el dataset nos basamos en el programa deasarrollado por: tzutalin
Github del programa: https://github.com/tzutalin/labelImg

โข Donde procesamos el data set:<br>
  ๐ Colab: https://colab.research.google.com/drive/1IaU5PR17KPp7z8Un1mfJLWBqYHGwD7sP?usp=sharing ๐
  
<------- Nube con mรกs informaciรณn e instrucctivos -------><br>
โ https://usmcl-my.sharepoint.com/:f:/g/personal/ethan_leiva_usm_cl/ErvVWQQnTvZCmqCxm3eJ1PQB6-HL0ac2BCV6Gb5vJfv85Q?e=fD5lE9
  
# ๐๐ป๐๐ฒ๐ด๐ฟ๐ฎ๐ป๐๐ฒ๐ ๐ ๐ฟ๐ผ๐น๐ฒ๐


โข Fabian Palacios    ๐   202030017-8

โข Ana Gonzalez   ๐   202130009-0

โข Ethan Leiva    ๐   202129866-5

โข Alicia Pereira ๐   202130002-3



# ๐ข๐ฟ๐ถ๐ด๐ฒ๐ป

โข Nuestro proyecto tuvo origen al momento de encontrar una encuesta realizada a las personas en el aรฑo 2019, donde el 73% de los chilenos asegura tener un promedio de 2 mascotas en su hogar. Despuรฉs de esto hicimos una lluvia de ideas sobre que inconvenientes o complicaciones se les proporcionan en su vida cotidiana, a lo que concluimos que una de las mรกs grandes preocupaciones son cuando las mascotas salen fuera del hogar, debido a que elimina bastante tiempo el estar pendiente de ellos cuando se ecuentran en su momento de recreacion. Ademรกs concluimos que los perros y los gatos son las mascotas mรกs frecuentes que salen sin supervisiรณn constante por lo cual son los que predominaran en nuestro proyecto. 

# ๐๐ผ๐ด๐ด๐ฒ๐๐๐ฒ๐๐ฎ๐ฃ๐ผ๐ฏ๐น๐ฎ

โข Proyecto realizado por nuestro equipo para la asignatura IWG101 que consiste en una red neuronal capaz de identificar perros y gatos, con la finalidad de integrarse a una raspberry pi 4 modelo B asociada a una cรกmara y a un bot de telegram para poder genenrar un sistema de alerta inteligente (o automatizaciรณn de una puerta en caso de ser posible) para darle mรกs libertad a nuestras mascotas de movilizarse por la entradas del hogar. 

# ยฟ๐๐ผฬ๐บ๐ผ ๐ณ๐๐ป๐ฐ๐ถ๐ผ๐ป๐ฎ? 

โข La cรกmara captura la imagen que es enviada a la raspberry pi 4 con el programa integrado, esta es analizada y en caso de reconocer a tu mascota enviara un aviso mediante un bot de telegram para que puedas abrir la puerta a tu mascota o en su defecto, si la puerta esta automatizada, se abra y cierre de forma automatica en el momento que la mascota entre. 

# ๐๐ป๐๐๐ฎ๐น๐ฎ๐ฐ๐ถ๐ผฬ๐ป ๐ ๐ณ๐๐ป๐ฐ๐ถ๐ผ๐ป๐ฎ๐บ๐ถ๐ฒ๐ป๐๐ผ ๐ฑ๐ฒ๐น ๐ฝ๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ๐ฎ

โข ๐ฃ๐ฟ๐ถ๐บ๐ฒ๐ฟ๐ผ ๐  ๐ฐ๐น๐ผ๐ป๐ฎ๐บ๐ผ๐ ๐ฒ๐น ๐ฟ๐ฒ๐ฝ๐ผ๐๐ถ๐๐ผ๐ฟ๐ถ๐ผ :
```
git clone https://github.com/DoggesDeLaPobla/Proyecto1.git
```

โข ๐ฆ๐ฒ๐ด๐๐ป๐ฑ๐ผ ๐  ๐ฒ๐ป๐๐ฟ๐ฎ๐ฑ๐ผ๐ ๐ฎ๐น ๐ฟ๐ฒ๐ฝ๐ผ๐๐ถ๐๐ผ๐ฟ๐ถ๐ผ ๐ฐ๐น๐ผ๐ป๐ฎ๐ฑ๐ผ :
```
cd Proyecto1/
```
โข ๐ง๐ฒ๐ฟ๐ฐ๐ฒ๐ฟ๐ผ ๐  ๐๐ท๐ฒ๐ฐ๐๐๐ฎ๐บ๐ผ๐ "๐ฟ๐ฒ๐พ๐๐ฒ๐ฟ๐ถ๐บ๐ถ๐ฒ๐ป๐๐ผ๐.๐๐ต" :
```
sh requerimientos.sh
```
โข ๐๐ถ๐ป๐ฎ๐น๐บ๐ฒ๐ป๐๐ฒ ๐  ๐ฝ๐ผ๐ฑ๐ฒ๐บ๐ผ๐ ๐ฒ๐ท๐ฒ๐ฐ๐๐๐ฎ๐ฟ ๐ฒ๐น ๐ฝ๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ๐ฎ :
```
sh iniciar.sh
```
โข ๐ฆ๐ถ ๐ฑ๐ฒ๐๐ฒ๐ฎ๐ ๐ฐ๐ฟ๐ฒ๐ฎ๐ฟ ๐ฒ๐น ๐ถ๐ป๐ถ๐ฐ๐ถ๐ผ ๐ฎ๐๐๐ผ๐บ๐ฎ๐๐ถ๐ฐ๐ผ ๐ฑ๐ฒ๐น ๐ฝ๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ๐ฎ ๐ฝ๐๐ฒ๐ฑ๐ฒ๐ ๐๐๐น๐ถ๐๐ฎ๐ฟ :
```
sudo python3 Auto.py
```
โข ๐ฌ ๐ฝ๐ฎ๐ฟ๐ฎ ๐ฒ๐น๐ถ๐บ๐ถ๐ป๐ฎ๐ฟ ๐ฒ๐น ๐ถ๐ป๐ถ๐ฐ๐ถ๐ผ ๐ฎ๐๐๐ผ๐บ๐ฎ๐๐ถ๐ฐ๐ผ :
```
sudo python3 DelAuto.py
```
