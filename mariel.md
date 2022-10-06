# Entendimiento de la situacion actual

Para entrar en contexto definamos que es esperanza de vida. 

La ONU establece la siguiente definición: **"Cantidad de años que un recién nacido puede esperar vivir si los patrones de mortalidad por edades imperantes en el momento de su nacimiento siguieran siendo los mismos a lo largo de toda su vida"**.

La esperanza de vida caracteriza la mortalidad a lo largo de la vida, en otras palabras podriamos  tomarlo como la edad promedio de muerte en una población.

Actualmente la esperanza de vida aumentó sustancialmente con respecto al siglo pasado, hoy por hoy estamos con una esperanza de vida promedio de 72.6 años (ONU - 2019).

Bajo esta premisa, nos preguntamos ¿cuáles fueron los factores que influyeron a este crecimiento?, ¿esta esperanza aumentará en los próximos años?, ¿qué paises se encuentran por debajo del promedio?, ¿que otras factores podrían mejorar la esperanza de vida? 


Todas estas preguntas las resolveremos a lo largo de este proyecto. 

# Objetivos

Identificar y realizar un analisis estadistico a los factores principales del crecimiento de la esperanza de vida durante los ultimos 30 anos en N países.

# Alcance

Analisis de los factores relevantes de N paises en los ultimos 30 anos.


Nota: leer este informe https://sci-hub.se/https://www.jstor.org/stable/40376184

# No alcanceain

# Solución propuesta 

Esta sección lo dividiremos en tres etapas. 

 - Realizar una ingenieria de los datos.

 -  Analisis descriptivo de los factores (técnica de correlación de Pearson, diagramas de dispersión entre otros)
 
 - Análisis de machine learning para inferir la esperanza de vida en años venideros

## *Stack tecnológicos*
 
-  Python para la extraccion y transfromacion de los datos 
- PostgreSQL para el almacenamiento de los datos. 
- Power BI para la vizualización de los datos
- AWS?

# Metodología de trabajo

Se trabajará a través de la metodología SCRUM para lo cual usaremos Trello como herramienta de seguimiento.  

<img src = "https://i.imgur.com/VB2yYJe.jpg" height = 300>

# Notas extras
- The Covid-19 pandemic is the primary cause of the decline the life expectancy, but we are ignoring another statistic. An Oxford University research found that moderate obesity, which is now common, reduces life expectancy by about three years, and severe obesity, which is still uncommon, can shorten a person’s life by ten years. *(Extreme obesity may shorten life expectancy by up to 14 years)*  - buscar datos

- De acuerdo a James C. Raley en su libro *Rising Life Expectancy* los ingresos como tal no tienen mucha relevancia en cuanto la esperanza de vida, es en realidad el como se distribuye esa riqueza lo que impacta sobre la esperanza `Tomar al PBI como uno de los factores, PBI usado para el sector salud` 
- Segun las naciones unidad en los paises menos desarrollados la esperanza de vida es menor por los niveles de *mortalidad infantil y materna* - `2do factor`
- Investigaciones por parte del Banco Mundial concluyen que `el progreso tecnologico, la educacion femenina y los ingresos en los paises son factores importantes para la esperanza de vida. `(analizar esots factores)s
- Impacto de las pandemias a la esperanza de vida : se `se podria analizar las tres más cercanas como COVID, gripe A-H1N1, el dengue`
- De acuerdo al paper *Determinants of health status in Chile*, en Chile se mejoró la esperanza de vida porque satisfizo la demanda sanitaria y aumentó el presupuesto social en salud. (`Factores a analizar`)

**NOTA** Para el analisis de los factores que influyeron en la esperanza de vida en Chile usaron el modelo de regresión múltiple con series temporales

- Del mismo paper se extrae la sigueinte informacion:
los países fueron agrupados según su esperanza de vida baja, media y alta. El estudio determinó que, contrariamente a lo que se esperaba, en el caso de los países desarrollados las variables estudiadas, es decir el ingreso per cápita, el gasto en salud, el acceso al agua potable, la ingesta de calorías, no resultaron ser estadísticamente significativas.


Entendimiento del problema 

Qué es la esperanza de vida al nacer? 

La ONU establece la siguiente definición: **"Cantidad de años que un recién nacido puede esperar vivir si los patrones de mortalidad por edades imperantes en el momento de su nacimiento siguieran siendo los mismos a lo largo de toda su vida"**, en otras palabras, la esperanza de vida es la edad promedio de muerte en una población.

Por qué escoger la esperanza de vida al nacer como proyecto?

Porque es parte de los indicadores que muestran el nivel de desarrollo de un país en el transcurso de los anios, 
está ligada a la economía, la educacion y la salud de un país. La esperanza de vida nos da conocer numerosas caracteristicas de una sociedad que pueden ser analizadas durante distintos periodos de tiempo. En definitiva, es una medida sencilla que puede aportar mucho valor a distintos paises.

Siguiendo con esta premisa lo que deseamos es proporcionar una herramienta para analizar facilmente informacion acerca de los factores que influyen a la esperanza de vida de un determinado pais, asi como el acceso a una data más prolija de estos factores.


