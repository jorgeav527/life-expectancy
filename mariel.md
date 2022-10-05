# Entendimiento de la situacion actual

Para entrar en contexto definamos que es esperanza de vida. 

La ONU establece la siguiente definición: **"Cantidad de años que un recién nacido puede esperar vivir si los patrones de mortalidad por edades imperantes en el momento de su nacimiento siguieran siendo los mismos a lo largo de toda su vida"**.

La esperanza de vida caracteriza la mortalidad a lo largo de la vida, en otras palabras podriamos  tomarlo como la edad promedio de muerte en una población.

Actualmente la esperanza de vida aumentó sustancialmente con respecto al siglo pasado, hoy por hoy estamos con una esperanza de vida promedio de 72.6 años (ONU - 2019).

Bajo esta premisa, nos preguntamos ¿cuáles fueron los factores que influyeron a este crecimiento?, ¿esta esperanza aumentará en los próximos años?, ¿qué paises se encuentran por debajo del promedio?, ¿que otras factores podrían mejorar la esperanza de vida? 

Todas estas preguntas las absolveremos a lo largo de este proyecto. 

# Objetivos

Identificar y realizar un analisis estadistico a los factores principales del crecimiento de la esperanza de vida durante los ultimos 30 anos en N países.

# Alcance
`Esta sección lo dividiremos en dos etapas. En la primera realizaremos un análisis descriptivo (haciendo uso de la técnica de correlación de Pearson y los diagramas de dispersión) y en la segunda parte un análisis econométrico para el desarrollo de nuestro objetivo.`

Nota: leer este informe https://sci-hub.se/https://www.jstor.org/stable/40376184
# No alcance

# Solución propuesta 

- Escoger 15 factores que influyen en el crecimiento de la esperanza de vida de acuerdo a paper y/o tesis encontradas en la red.

- Usar API's para importar los dataset

- Análizar estadisticamente los factores, con la finalidad de seleccionar los 10 factores con mayor relevancia.

- Clasificar a los paises de acuerdo a los factores seleccionados y su influencia en la esperanza de vida.

## *Stack tecnológicos*
 
- PostgreSQL como almacenamiento y procesamiento de la base de datos. 
- Python para la conexión con las API'S
- Power BI para la vizualización de los datos
- AWS?

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
