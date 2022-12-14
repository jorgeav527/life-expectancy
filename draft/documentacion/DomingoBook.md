# Introducción
Mediante el siguiente analisis se pretende traer algo de luz sobre los distintos factores que impactan directamente en la experanza de vida al nacer en diferentes países del mundo. 

Se sabe que si bien la esperanza de vida al nacer sigue de cerca la esperanza de vida que tiene una persona, los cambios en la esperanza de vida al nacer son muy sencibles a los cambios en la mortalidad infantil. Cuando esta última es baja, el cálculo directo de la esperanza de vida al nacer, puede indicar cambios en la mortalidad de adultos.

Si bien se puede aproximar de forma indirecta, nos gustaría profundizar en aquellos factores que más impacto tienen sobre la mortalidad infantil para usarlos a modo de predictores en nuestro análisis.

# Alcance y limitaciones
A pesar de nuestra ambición por cubrir todos los aquellos elementos que podrian o tienen un impacto directo sobre la variable a analizar, por el corto tiempo de desarrollo del proyecto, nos quedaremos unicamente con aquellas que han probado tener algún impacto significativo sobre nuestra variable de estudio y dedicarnos a hacer un análisis cruzado de indicadores pára ver cuales impactan más sobre la esperanza de vida al nacer y cómo. Los indicadores bajo estudio serán:

```py
for i in indicadores
    print(i)
```
Mientras que el alcance en cuanto a países, nos pareció adecuado el seleccionar aquellos con mayor densidad poblacional y mayor extencion de territorio:

```py
for i in paises
    print(i)
```
El desarrollo de un modelo MachineLearning predictor de esperanza de vida también queda dentro del alcance del proyecto. El cual devolverá un número edad que indicará si bajo las condiciones propuestas la esperanza de vida al nacer se incrementó, se mantuvo igual o decrementó.

# Solución propuesta
Se propone la presentación de una  plataforma intuitiva y personalizada, rapida y facil de usar que permita realizar el seguimiento de un pais a lo largo del tiempo, para conocer de qué forma las variables seleccionadas han impactado en la esperanza de vida al nacer. El mismo permitirá, en base a los datos recavados, y mediante modelos predictivos, conocer qué variables sería recomendable optimizar para mejorar la esperanza de vida.

Se pretente que esta plataforma también sea capaz de mostrar qué hubiera ocurrido en años anteriores si el gobierno de turno hubiese implementado acciones en contra de la mortalidad infantil o el gobierno de paso se encontrará bajo un régimen democrático.

# Ideas no relacionadas
## Features que se podría analizar
- Desigualdad en el **ingreso**
	- Coeficiente de Gini [3.0.Gini]
	- Gini rural [3.1.Gini]
	- Porcentaje de la poblacion rural [SP.RUR.TOTL.ZS]
	- Gini urbano [3.2.Gini]
	- Porcentaje de la población urbana [SP.URB.TOTL.IN.ZS]
- Empoderamiento de las muyeres
	- Porcentaje población mujeres [SP.POP.TOTL.FE.ZS]
		-> .IN en lugar de .ZS indica cantidad
	- porcentaje población hombres [SP.POP.TOTL.MA.ZS]
		-> .IN en lugar de .ZS indica cantidad
	- Proporción sexos al nacer [SP.POP.BRTH.MF]
		-> Mujeres cada 1000 hombres
- Educación como predictor
	- Gasto público en educación, total (% del PIB) [SE.XPD.TOTL.GD.ZS]
	- Educación obligatoria, duración (años) [SE.COM.DURS]
- Obesidad, alcoholismo, tabaquismo
	- No encontré indicadores para esto ehe
- **gasto en servicios de salud del país**
	- Gasto en salud total (% del PBI) [SH.XPD.TOTL.ZS]

Para ver en detalle cada uno de estos indicadores, acceder al endpoint:
http://api.worldbank.org/v2/es/indicator/[indicador]?format=json

# Cualquiera de estos nombres con Analitica al final XD
**Gyan:** Es de origen hindú y sánscrito, y el significado de Gyan es "la sabiduría, la iluminación".
**Solin:** [Nombre griego masculino](https://www.todopapas.com/nombres/nombres-de-nino/nombres-de-origen-griego) con dos significados: “sabiduría; grave”.
**Sofía:** Sofía significa, gracias a su origen griego, "sabiduría". Se interpreta como la mujer sabia, la audaz e inteligente.
**Daina:** Daina fue la reina griega de las montañas, llena de sabiduría.
**Atenea:** Evoca la figura de Palas Atenea, diosa protectora de los atenienses, diosa griega de la sabiduría. Hija de Zeus y de Juno.
**Apolo**: la luz de la [verdad](https://es.wikipedia.org/wiki/Verdad "Verdad").
**Dru:** Significa "visión", el que todo lo ve con claridad.
#### Alden
Significado: Defensor  
Origen: Anglosajón  
Género: Niño
#### Ailfrid
Significado: Sabio  
Origen: Irlandés  
Género: Niño
#### Aldrick
Significado: Viejo o sabio gobernante  
Origen: Francés  
Género: Niño
#### Cate
Significado: Sabio  
Origen: Latín  
Género: Chica
#### Conan
Significado: Sabio  
Origen: Celta  
Género: Niño
#### Drew
Significado: Sabio  
Origen: Anglosajón  
Género: Niño
#### Alden
Significado: viejo y sabio amigo
origen: inglés
Género: Niño
### Ismene
Significado: conocedor
Origen: griego
Género: Niña
[nombres piolas](https://www.revistadelbebe.com/nombres-que-significan-sabio/)

# Presentación primera semana

Buenas tardes, buenos días. Estamos muy contentos de estar aquí. Sabemos que tienen una filosofía muy similar a la nuestra. Y nos encantará trabajar juntos. Somos Yupana Analytics una división dedicada a ofrecer servicios de data analisis para organizaciones humanitarias. Contamos con 4 años de experiencia brindando datos que ayudan a simplificar el trabajo de las distintas organizaciones

Nos dedicamos a la recopilación y analisis de datos para para que los proyectos humanitarios no tengan que dedicarse a ello y puedan emplear su tiempo en acciones y decisiones que mejoren la calidad de vida de las personas desde el minuto uno.

Desde nuestro lugar entendemos el miedo y la creencia negativa de que la tecnología nos deshumaniza y distancia. Es por eso que estamos comprometidos más que nunca en mostrar información relevante que ayude a humanizar, a convertir esos números y porcentajes abstractos en algo sólido. Con la esperanza de que los años de vida que ayudemos a ganar sean años que ayuden a cambiar la visión que se tiene de la teconología.

Nuestro equipo esta conformado de la siguiente manera:
- En el área de Ciencias de Datos, se encuentra Jorge Alarcón. Responsable de aplicar modelos predictivos adecuados que describan el comportamiento de los datos.
- En el área de Análisis de Datos Mariel Cochachi. Llevando un trabajo fundamental para facilitar la visualización y comprensión de los datos, tanto durante el preprocesamiento como en la presentación final del producto.
- En en área de Anális Funcional, Ravi Rojas. Encargado de articular y conectar con nuestros potenciales beneficiarios. Haciendo especial énfasis en la interacción de las diferentes áreas del proyecto.
- En el área de Ingeniería de datos, su servidor, quien les habla Domingo Gutierrez. Responsable de la adquisición de los datos, diseño del Data Warehouse, EDA y procesos de ETL necesarios para poder trabajar sobre los datos.

Ahora le doy la palabra a nuestra compañera Mariel quien les va a contar porque elegimos enfocarnos en algo tan bonito y tan importante como es la esperanza de vida al nacer.

## Devoluciones
Dedicar siempre unos minutos a contar el progreso que tuvimos. Lo que hicimos, lo que no hicimos, las dificultades que tuvimos. 

Contar la parte de cómo vendemos el producto, el progreso que tuvimos y enfocar el desarrollo en el staf tecnológico. 

Gant, flujo de datos, 
Mostrar avances,

Debe existir la parte académica, que hicimos durante la semana. No dejar de lado la párte académica.
Debe existir la parte financiera, porque por un lado debe estar la parte académica.

## KPIs
Objetivo reducir el tiempo de 2 meses el trabajo el de organizaciónes
Aumentar la esperanza de vida en 0.2 años en un año siguiendo las recomendaciónes que indica el producto

Velocidad en la que se hacen cargas incrementales

# Presentación semana 2

Estos contenían un montón de información irrelevante para nuestro análisis. Con **columnas con valores repetidos, y redundantes**. Así que lo que se hizo fue quedarse con las columnas de interés.

En este caso seleccionamos el código del país en formato iso3, el año y el valor de cada  tabla que cargamos. 

A la columa de valor, hubo que cambiarle el nombre porque en todas las tablas se llamaba igual: "value", a uno más relevante y significativo. Algo que estuviera directamente relacionado con el endpoint.

Una vez conseguidas esos **pequeños dataframes, lo siguiente era fusionarlo** en uno más grande que tuviera el valor de nuestra variable objetivo "esperanza de vida al nacer". Para ello nos valimos del código **iso3 de cada país y el año, que se usaron como identificadores únicos.**

Una vez conseguido esto se pasó a **automatizar todo ese proceso siguiendo reglas específicas** para cada archivo parquet leído según un **diccionario en el que se encontraba el nombre del archivo como clave y el nombre de la columna como valor.** Se leyeron los nombres de los archivos parquets en el directorio de forma automática y según el tratamiento que necesitaran se fueron trabajando.

Ahora si es cuando comienza la parte más complicada. Pasamos a evaluar la cantidad de faltantes que existían en cada columna de este dataset masivo y descubrimos que había columnas con alto porcentaje de valores faltantes, así que aquellas que tuvieran más de un **35% de faltantes las eliminamos.** Puesto que sería más de un tercio de la información total que se disponía.

Durante esta segunda etapa es también que se descubrió, sin ninguna sorpresa por parte del equipo, que cuanto más alejados nos encontraramos del presente, mayor porcentaje de valores faltantes.

**Siguiendo los lineamientos de la tesis propuesta en la lectura es que dividimos los países según un grupo clasificatorio de ingreso.** En alto, medio alto, medio bajo, y bajo. Y pudimos comprobar que el pbi influye más en la esperanza de vida para países con menor ingreso que con mayor ingreso, comprobando así una de las hipotesis de la tesis.

Para finalizar se aplicó un poco de preprosesamiento a modo de dejar los datos casi listos para la semana siguiente. Aplicando tecnicas de correlación decidimos quedarnos únicamente con aquellas features que tuviesen más correlación con la variable objetivo.

Esperamos que el modelo de machine learning nos ayude a traer más luz a la calidad de los datos que hemos seleccionado.

