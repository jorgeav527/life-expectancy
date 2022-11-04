# 4. Desarrollo

## Stack tecnológico
![Imgur](https://i.imgur.com/y2DzIx3.png)
1. Sistema de control de Versiones 
    * Git
    * GitHub
    * Git LFS
3. Lenguaje de programación
    * Python
    * SQL
4. Librerias
    * Numpy 
    * Pandas
    * Scikit-learn
    * Conda
    * Mathplotlib
    * FastAPI
    * Streamlit
5. Frameworks
    * Apache-airflow
    * Jupyter
6. Bases de datos
    * PostgreSQL
    * Mongo
7. Virtualización
    * Docker
    * venv & conda
## Servicios (Linode)
1. Data Lake: Object Storage
2. Data warehouse: Database Clusters
3. Servidor: Lino cloud-based virtual machine
## Arquitectura
La extracción de los datos ...
![Imgur](https://i.imgur.com/QTDVyHy.png)
La transformación de los datos al data lake y luego al data warehouse, para que esten listos para ser consumidos por el PowerBI y el Streamlit ...
![Imgur](https://i.imgur.com/dYGGiiW.png)
## DevOs
![Imgur](https://i.imgur.com/BM4r9ML.png)
![Imgur](https://i.imgur.com/9y7ewOs.png)
## Extracción

Los datos fueron directamente extraídos de las APIs de las Naciones Unidas, el Banco Mundial y la Organización Mundial de la Salud. Para hacerlo simplemente se usó la librería request de python y se consultaron los distintos endpoints de interés a través de funciones que hacían un recorrido por indicadores previamente seleccionados.

Para conocer más sobre los posibles endpoints y distintas configuraciones de las APIs consulta su documentación:
- [Banco Mundial](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information)
- [Naciones Unidas](https://population.un.org/dataportal/about/dataapi)
- [OMS](https://www.who.int/data/gho/info/gho-odata-api)

Las APIs de las distintas fuentes tardan mucho en responder es por eso, que para poder contar con ellas de forma offline y garantizar un flujo de trabajo más agil, es que se guardaron las mismas en formato parquet en la carpeta data/datos_brutos de forma íntegra, una vez convertidas a dataframe

## Transformación

Para el proceso de transformación se leyeron las distintas tablas y se seleccionaron únicamente aquellas columnas que contenían información relevante, aquellas que contienen el dato per sé por el que se estaba consultando al endpoint desde un principio.

En el caso de la respuesta del Banco Mundial vemos que todas aquellas columnas que se encuentran luego del la columna Value (que corresponde al valor de la información por la que estamos consultando) contienen información que no nos interesa o información reduntante. Algo muy similar ocurre con las respuestas de las Naciones Unidas y la OMS

![Imgur](https://i.imgur.com/XchSIPs.png)

Se decidió utilizar el código ISO3 de cada país y la fecha brindada en la columna _date_ para crear un índice múltiple (del tipo \[countryiso3code, date\]) que servirá merger la información de distintas tablas en  una sola y de esa forma poder realizar un análisis de correlación que cubriremos en la parte de [EDA]. 

_En este apartado únicamente nos concentramos en las transformaciónes correspondientes para crear las distintas tablas en la base de datos._ 

Una vez creadas las tablas con todos los indicadores se guardan en formato parquet en la carpeta data/datos_pre_procesados para ser retomadas por la siguiente tarea.



## Carga

Para el proceso de carga nos ayudamos de el motor create_engine de la librería sqlalchemy. para establecer una conexión a la base de datos Postgres que se encuentra online en Linode.

```python
DATABASE_URL = "Ubicación del recurso online"
engine = create_engine(DATABASE_URL)
connection = engine.connect()
```

Luego solamente era cuestión de usar el método to_sql de cada dataframe de la siguiente manera para ingestar los datos directamente a la base de datos.

```python
# tabla ingreso (hecho)
df_indices.to_sql(
"indice", con=engine, index=False, if_exists="replace", index_label="id"
)
```

Por supuesto al finalizar el proceso hay que cerrar la conexión a la base de datos

```python
connection.close()
```

## Performance