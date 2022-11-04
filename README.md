Este es un desafío de data análisis propuesto en el bootcamp de Data Cience de Henry. El trabajo comprende desde la extracción hasta su presentación en un dashboard y un modelo predictivo.

El dashboard se encuentra operativo [en este link](https://app.powerbi.com/view?r=eyJrIjoiYTUzODVkN2EtMWVlZC00ODMxLTk5MjQtOTdiY2Q1ZjgzYTdlIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9), y todo el proyecto se encuentra corriendo en la nube en un servidor remoto de Linode. 

Para probarlo de manera local y experimentar con él, es necesario tener instalado docker y docker-compose en su computadora. Puedes verificar si lo tienes instalado con 

```bash
docker --version
docker-compose --version
```

Deberías ver una respuesta para cada uno de una linea. De lo contrario revisa la [documentación de docker](https://docs.docker.com/desktop/) para seguir los pasos de instalación según tu sistema operativo.

Una vez echo esto debes escribir el siguiente código para crear las variables de entorno que necesita Airflow para funcionar sin inconvenientes. Y las carpetas que serán utilizadas durante el flujo de trabajo

```bash
mkdir -p ./dags ./logs ./plugins ./data
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

El código creará el archivo .env y las carpetas de forma automática, de lo contrario puedes renombrar el archivo llamado .env.sampre a .env y crear las carpetas manualmene. Si te encuentras en un sistema operativo que no sea Linu ss posible que obtengas una advertencia al iniciar el contenedor, pero funcionará de todos modos. Si quieres deshacerte de ella debes cambiar la línea dentro del archivo .env por

```
AIRFLOW_UID=50000
```

Al estar usando una versión extendida de Airflow, es necesario correr el siguiente código 

```bash
docker build . --tag extending_airflow:latest
```

De esta forma el archivo YAML se ejecutará sin inconvenientes al crear el contenedor con el siguiente comando

```bash
docker-compose up airflow-init
```

Por último ya lo podremos correr de forma normal con 

```bash
docker-compose up -d
```

Esto iniciará los contenedores de Docker con el servicio de Airflow, el schedule más una base de datos Postgres en la que se almacena la información.

***

Si deseas conocer el desarrollo del código más a fondo siempre puedes revisar la documentación en [el wiki](https://github.com/jorgeav527/life-expectancy/wiki). O acceder a los archivos .ipynb en los que se desarrolla paso a paso el código.

