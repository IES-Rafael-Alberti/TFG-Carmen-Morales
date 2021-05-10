# Descripción

Proyecto de fin de ciclo de Desarrollo de aplicaciones Web

## Instalación

Instalar las librerías necesarias.

```
pip install -r requirements.txt 
```

## Inicializar la base de datos

Añadir los datos

* Añadir los territorios 

```
python .\manage.py set_territories
```

* Actualizar los datos

```
python .\manage.py get_acumulated --territorio [parámetro]
```

```
-p Provincias
-all Región de Andalucía
-mun Municipios de Andalucía
```

* Obtener los históricos (hastael 30/04/2021)

```
python .\manage.py get_historic   
```

## License
[MIT](https://choosealicense.com/licenses/mit/)