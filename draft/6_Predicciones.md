# 6. Predicciones
  La intención de ésta etapa del proyecto es desarrollar un Modelo de Machine Learning que permita, en primer lugar, describir, desde el punto de vista estadístico, el comportamiento de la variable objetivo (Esperanza de Vida al Nacer). Para ello se realiza un proceso que parte de lo que estadística se conoce como Análisis de Componentes Principales, que consiste en determinar cuales factores, de los estudiados, ejercen influencia sobre el valor de la variable objetivo. Con estos factores se construye un modelo matemático que además de describir el fenómeno estudiado permita realizar proyecciones a futuro.
  
## Preparacion de los Datos
![Imgur](https://i.imgur.com/y2DzIx3.png)
1. Descarga de los Datos. 
    Lo primero es descargar los datos desde el servicio de Linode con las siguientes credenciales:
    
      host = 'lin-10962-2858-pgsql-primary.servers.linodedb.net'
      port = '5432'
      dabase_name = 'postgres'
      password = '1my6fZf1Lh8R&n54'
      username = 'linpostgres'
    
    La conexion se realiza en un cuaderno de Jupyter con la librería de Pyhthon Psycopg2 y cada tabla de la base de datos se almacena temporalmente en un dataframe.
    
    ## Análisis Exploratorio de Datos
    
    Como los datos se encuentran normalizados en la base de datos es necesario juntarlos a través de estrategias como el merge o el join. Al final se tiene un dataframe con los datos de interés.
    
    A partir de los datos en estado "salvaje" lo primero que se hace es un Análisis Exploratorio para evaluar la calidad de los datos. Para este caso particular destaca el gran porcentaje de datos faltantes.
    
    Como estrategia para resolver el problema de datos faltantes, lo primero que haremos será dividir el dataset. Como estamos poniendo especial atención en la brecha existente entre los valores de la Esperanza de Vida al Nacer de los grupos extremos, usaremos ese criterio para dividir el dataset. Un dataframe para los paises de ingresos altos y otro para los de ingresos bajos.
   
      mask0 = (df_group['nivel_id']==0.0)
      df_n0 = df_group[mask0].reset_index()
      mask1 = (df_group['nivel_id']==1.0)
      df_n1 = df_group[mask1].reset_index()
      mask2 = (df_group['nivel_id']==2.0)
      df_n2 = df_group[mask2].reset_index()
      mask3 = (df_group['nivel_id']==3.0)
      df_n3 = df_group[mask3].reset_index()
      
    Ya que los datos en cada grupo tienen tendencias distintas, se aprovecha este comportamiento para imputar datos faltantes usando la estrategia de K vecinos cercanos.
    
      from sklearn.impute import KNNImputer
      knn = KNNImputer(n_neighbors=5)
      a = pd.DataFrame(knn.fit_transform(dfaux), columns=col)
      
## Reducción de Dimensionalidad
  
  Para continuar con el Analisis de Componente Principales es necesario someter a los datos a un análisis de correlación y someterlos a un test chi cuadrado para descartar aquellas carácterísticas con alta correlación entre si o con muy baja correlación con la variable objetivo y ademas descartar aquellas caraterísticas que tengas un p-value por encima de 0.05.
  
## Implementacion del Modelo
  
  Los valores de la esperanza de vida por cada país poseen una serie de características que dan luz para seleccionar el modelo. En primer lugar conocemos el valor historico de la variable objetivo por lo que reducimos las opciones a los modelos supervisados. En segundo lugar la variable es continua y observando su comportamiento podemos notar que es aproximandamente lineal. Por último los valores, para los diferentes grupos clasificatorios, se concentran alrededor del valor promedio generando una grafica acampanada.
  
  Con todas las evidencias estudiadas decidimos implementar un modelo de regresión lineal con los hiperparámetros predeterminados. Termino independiente distinto de cero y normalización.
  
    fit_intercept: True
    normalize: True
