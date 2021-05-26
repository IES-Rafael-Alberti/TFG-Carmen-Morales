# Andalucía COVID Dashboard
## _Proyecto de fin de ciclo de DAW_ 

[![N|Solid](https://www.djangoproject.com/m/img/badges/djangomade124x25.gif)](https://nodesource.com/products/nsolid)

## Índice
- [1. Introducción](#introduccion) 						 
- [2. Objetivos](#objetivos)  												  
- [3. Tecnologías escogidas y justificación](#tecnologías)			 
  - [3.1. Frameworks seleccionados](#framework)
  - [3.2. Motor de bases de datos](#bbdd)
  - [3.3. Librerías](#librerias)					    		 	 
- [4. Instalación en local](#instalacion_local)
- [5. Instalación en docker](#instalacion_docker)
- [6. Fuentes](#fuentes)
- [7. Work in Progress](#WIP) 
  
# :sparkles: Introducción
<a name="introduccion"></a>	

Aplicación web realizada para el trabajo de fin de ciclo de Desarrollo de Aplicaciones Web sobre la evolución del COVID en Andalucía.

# :checkered_flag: Objetivos
<a name="objetivos"></a>
El objetivo es desarrollar una aplicación web donde se puedan consultar los datos epidemiológicos de la pandemia del SARS-CoV19 en Andalucía para consultar la situación de cada territorio y/o consultar el estado de la pandemia.

## :computer: Tecnologías utilizadas y justificación
<a name="tecnologías"></a>	

La aplicación se desarrolla en su mayor parte usando lenguaje `python` :snake:

## Framework
<a name="framework"></a>	
El framework escogido es `Django framework` por diversas razones:
Los motivos principales para usar Django son:

 - [x]  Es muy rápido: Si tenéis una startup, tenéis prisa por terminar vuestro proyecto o, simplemente, queréis reducir costes, con Django se puede construir una aplicación muy buena en poco tiempo.
 - [x] Viene bien cargado de funcionalidades: Cualquier cosa que se necesite realizar, ya estará implementada, sólo hay que adaptarla a las necesidades del proyecto.
  - [x] Es seguro: Implementa por defecto algunas medidas de seguridad, las más clásicas, para que no haya SQL Injection, no haya Cross site request forgery (CSRF) o no haya Clickjacking por JavaScript. Django se encarga de manejar todo esto de una manera realmente sencilla.
  - [x]   Es muy escalable: Podemos pasar desde muy poco a una aplicación enorme perfectamente, una aplicación que sea modular, que funcione rápido y sea estable.
  - [x]   Es increíblemente versátil: Se puede utilizar para aplicaciones multipropósito.
  - [x] Tiene una documentación muy completa y una gran comunidad muy colaborativa.

## Motor de base de datos
<a name="bbdd"></a>	
El motor de base de datos elegido es PostgreSQL:
  - [x]  Instalación ilimitada y gratuita
  - [x]  Es multiplataforma para Windows, Linux y Mac (los sistemas operativos más extendidos) con lo cual se podrá disponer él en cualquiera de estos.
  - [x]   Es un motor con un uso muy extendido en la comunidad de desarrolladores, con lo que conseguir ayuda es muy sencillo.
  - [x] Potencia y Robustez
  - [x] Es escalable, lo cual nos da una ventaja con vistas al futuro.

## :book: Librerías  
<a name="librerias"></a>	
  - [x] `[Twitter Bootstrap]` - Bootstrap es una biblioteca multiplataforma o conjunto de herramientas de código abierto para diseño de sitios y aplicaciones web
  - [x] `[Pandas]` - Es una librería de Python especializada en el manejo y análisis de estructuras de datos.
  - [x] `[Charts.js]` - Chart.js es una biblioteca JavaScript gratuita de código abierto para la visualización de datos, que admite 8 tipos de gráficos: barra línea área circular burbuja radar polar dispersión
  - [x] `[jQuery]` - jQuery es una biblioteca multiplataforma de JavaScript, creada inicialmente por John Resig, que permite simplificar la manera de interactuar con los documentos HTML.

## :house: Instalación en local
<a name="instalacion_local"></a>	

**Instalar las dependencias.**
```
pip install -r requirements.txt 
```

**Actualizar los datos**

```
python .\manage.py get_acumulated --territorio [parámetro]
```
Ejemplos de uso 
```
python .\manage.py get_acumulated --territorio -all  # Datos acumulados de Andalucía
python .\manage.py get_acumulated --territorio -mun  # Datos acumulados de municipios
python .\manage.py get_acumulated --territorio -pro  # Datos acumulados de provincias
```

**Obtener el histórico de datos del COVID19 en Andalucía**
```
python .\manage.py get_historic   
```

## Instrucciones para desplegar el docker
<a name="instalacion_docker"></a>	
```
docker-compose up -d --build
```
## Hacer las migraciones necesarias

```
docker-compose exec web python3 manage.py set_territories
docker-compose exec web python3  manage.py get_historics
docker-compose exec web python3 manage.py get_acumulated --territorio -mun
docker-compose exec web python3 manage.py get_acumulated --territorio -pro
docker-compose exec web python3  manage.py get_acumulated --territorio -all
```

Ir a `http://localhost:8000`

## :chart_with_upwards_trend: Fuentes de los datos
<a name="fuentes"></a>	
Los datos recogidos en esta aplicación web son de uso público y de fuentes oficiales.
- Datos de @Pakillo19 - https://github.com/Pakillo/COVID19-Andalucia/blob/master/datos/
- IECA - https://www.juntadeandalucia.es/institutodeestadisticaycartografia/salud/

## :pencil: WIP
<a name="wip"></a>	
  - [x]  Añadir modo oscuro
  - [ ]  Corregir diseño responsive
  - [ ]  Añadir HTTPS al despliegue
  - [x] Añadir tarea cron para actualización automática
 
## License
[MIT](https://choosealicense.com/licenses/mit/)