propuestas de ravi para el proyecto

#1. Entendimiento de la situación actual:



  El cliente requiere se determine las variables que influyen sobre el indicador: esperanza de vida al nacer y de que manera lo hacen. Para ello se parte de los datos del Banco Mundial la cual esta compuesta de 85 bases de datos. Tambien cuenta con una API que es un poco compleja y con una documentacion deficiente.

#2. Objetivos

  General: Producir un Dashboard que facilite al cliente la visualizacion de los datos que mas se relacionan con la esperanza de vida al nacer
  
  Especificos:
    1. Consumir los datos desde la API del Banco Mundial y de las APIS complementarias
      
      Actividad 1: Revisar y comprender la documentacion de la API del BM para determinar los endpoints que serán útiles para la adquisicion de los datos.

      Actividada 2: Desarrollar un script que permita conectar con la API del BM. 

      Actividad 3: Descargar los datos, decodificarlos y almacenarlos en df.

    2. Realizar el EDA

      Actividad 1: Revisar la calidad de los datos tomando criterios como por ejemplo: manejo de datos faltantes y outliers, normalización entre otros.

      Actividad 2: Realizar Ingeniería de características.

    3. Construir el Data Warehouse (ETL)

      Actividad 1: Construir la base de datos mediante postgreSQL

      Actividad 2: Realizar la carga de los datos 

    4. Desarrollar una API para desplegar los datos para los respectivos análisis.

      Actividad 1: Desarrollar el script de la API

      Actividad 2: Desplegar la API en algun servicio de nube

    5. Desarrollar las distintas visualizaciones

      Actividad 1: conectar con la API desarrollada desde el POWERBI (y/o streamlit)

      Actividad 2: diseñar el dashboard y con todos los elementos que faciliten la visualización.

    6. Presentar los resultados.

      Actividad 1: Diseñar el dashboard

      Actividad 2: Preparar la presentacion (dividir los contenidos)


#3. Alcance

  En cuanto al producto final el alcance se limita al desarrollo de una API bien documentada con los datos relevantes, un modelo predictivo y un dashboard que facilite su comprensión. Proceso que será desarrollado en el transcurso de 3 semanas a partir de la aprobacion de esta propuesta.

  En cuanto al análisis de los datos se propone cumplir en principio con el minimo requerido en cuanto al numero de datasets y de años incluidos.. aunque se puede ampliar a todos los paises y años exceptuando aquellos dataset con exceso de datos faltantes como por ejemplo paises con muy baja capacidad estadística.

#4. Fuera de Alcance

  Por el escaso tiempo detalles como desarrollo de alguna aplicacion para reunir todos los entregables seran dejados para una próxima etapa del proyecto

#5. Solucion Propuesta: (Stack tecnológico)

  detallado en la parte de objetivos

#6. Metodología de trabajo

  Se aplicará la metodologia scrum para darle seguimiento constante al desarrollo del proyecto con encuentros semanales con el PO y daylys con el scrum master para la evaluacion de los objetivos especificos

#7. Diseño detallado - Entragable

  Al final del proceso el cliente recibe el enlace y la documentacion de la API (ya desplegada en la nube) para el acceso a los datos requeridos asi como todos los scripts incluido el archivo de powerBI para la visualizacion y analisis de los datos (posiblemente un streamlit desplegado en la nube)

#8. Equipo de trabajo - Roles y responsabilidades 

  
  Ingenieria de Datos: Domingo Gutierrez

    El área de Ingeniería de Datos es responsable de la adquisición de los datos, el diseño del Data Warehouse, los Procesos de ETL, EDA y el despliegue de la API para el acceso a los datos preprocesados.

  Ciencia de datos: Jorge Alarcon

    El area de Ciencia de Datos es responsable de aplicar modelos de Machine Learning adecuados que describan el comportamiento de los datos y que permitan realizar predicciones a partir de los datos históricos.

  Analisis de Datos: Mariel Cochachi

    El Analisis de datos es fundamental para facilitar al resto de los stake holders la visualizacion y comprensión del comportamiento del fenómeno estudiado a partir de los datos, tanto los datos preprocesados durante el proceso de Ingeniería de datos como los producidos por el o los modelos predictivos.

  Analisis Funcional: Ravi Rojas

    Articular y conectar las diferentes entradas y salidas en cada uno de los pasos del proyecto y a su vez realizar un correcto relevamiento de los requerimientos a partir de la interacción con el PO es responsabilidad de éste departamento. 
#9. Cronograma General

  Semana 1: Elaboracion de la propuesta y reunion con el PO
  Semana 2: Construccion de la base de datos y la API con los procesos previos implicitos (EDA, ETL, despliegue)
  Semana 3: Desarrollo de un modelo de machine learning y validacion de las características.
  Semana 4: Desarrollo del tablero (o los tableros) y preparacion de la presentacion.




Descripcion del producto:

El mundo esta lleno de diversidad. El proceso de globalización a traido como consecuencia que se pretenda establecer patrones generales en todos los aspectos que forman parte de nuestras vidas.

Las variables que influyen sobre la esperanza de vida son muy diversas (El desarrollo económico o tecnológico no siempre impactan de manera positiva sobre la calidad de vida) pero no solo eso, varían. Pueden cambiar de un lugar a otro o durante el tiempo. Determinar estar particularidades es un arduo trabajo, pero gracias a la tecnología de Machine Learning se puede resolver de manera eficiente y precisa aportando calidad al resultado de las investigaciones. (estableciendo los parametros temporales y geograficos la plataforma te recomienda y te facilita los datos pertinentes)

Yupana Analitics provee herramientas para conectar de manera oportuna los datos precisos con quienes toman las decisiones.

Ofrecemos una plataforma inteligente que a partir de ciertos parametros indicados por el usuario devuelva en tiempo real los datos mas relevantes y ordenados segun su grado de influencia con características específicas para cada caso de estudio. 

Ademas la plataforma cuenta con herramientas que permiten visualizar los resultados y proyectar los cambios en la esperanza de vida cuando varian las caracteristicas influyentes. Esto permite simular escenarios pasados o futuros.

Es importante resaltar el valor que aporta nuestra plataforma a nuestros usuarios. Si se trata de investigaciones, estamos apoyando a nuestros usuarios en el uso eficiente del tiempo entregando datos adecuados y oportunos para cada caso de estudio. Cuando se trata de procesos de toma de decisiones contar con los datos indicados ayuda a la toma de decisiones acertadas y por lo tanto a un uso efectivo de los recursos económicos. (KPI de tiempo y de impacto de las politicas publicas)


Invitamos a organizaciones e individuos de todos los campos a unirse a nosotros!!







 