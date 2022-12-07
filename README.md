# Life Expentancy

<img src="https://i.imgur.com/5PxDz2P.png" width="500">

## Project Description

**What it is?** 💡 To generate insights about Life Expectancy, we created a pipeline from the ETL to create a data warehouse using APIs from the World Bank, World Health Organization, and United Nations. With this clean data, we created stunning dashboards and predictions based on machine learning models. **Why did you build this project?** 💡 This is the final project for Henry's Data Science Bootcamp.

**What was my motivation?** 💡 Reduce the gap by three years between developed and underdeveloped countries in the next 10 years!. **What did you learn?** 💡 Agile methodologies (SCRUM) and a GitHub flow to collaborate as a team. The pipeline was built using the architectures of "ETL with Airflow running as a web service," "Data Analytics with simple Notebooks," "Data Lake and Data Warehouse as a Service in Linode Cloud" "Interactive Dashboards using PoweBI and Streamlit for ML predictions," and "Docker for development and production environments".

## Table of Contents

<!--ts-->
* [Life Expentancy](#life-expentancy)
   * [Project Description](#project-description)
   * [Table of Contents](#table-of-contents)
   * [Parts of the Project](#parts-of-the-project)
      * [1. Architecture](#1-architecture)
      * [2. DevOs](#2-devos)
      * [3. Extraction](#3-extraction)
      * [4. Transformation](#4-transformation)
      * [5. Load](#5-load)
      * [6. EDA](#6-eda)
      * [7. Machine Learning](#7-machine-learning)
   * [Products](#products)
      * [1. PowerBI](#1-powerbi)
      * [2. Streamlit](#2-streamlit)
   * [How to Install and Run the Project](#how-to-install-and-run-the-project)
      * [1. Localy](#1-localy)
      * [2. Production](#2-production)
   * [How to ...](#how-to-)
      * [1. Contribute](#1-contribute)
      * [2. Use the Project](#2-use-the-project)
   * [Test](#test)
   * [+ Info](#-info)
   * [<em>Licence GNU GPLv3</em>](#licence-gnu-gplv3)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: jorgeav527, at: Thu  1 Dec 23:48:28 -05 2022 -->

<!--te-->

## Parts of the Project

### 1. Architecture

* We are building a pipeline with Apache-airflow. It begins by **Extracting** raw data from the World Bank, World Health Organization, and United Nations via their respective APIs. Second, we **Transform** this raw using a bucket to save and retrieve data in parquet format. Third, we **Load** this clean data into a Postgres Data Warehouse so that it is ready for any PowerBI or Streamlit connections.
    
    <img src="https://i.imgur.com/vBQixZT.png" width="700">

* In production, it will use an EC2 for the airflow pipeline, an Object Storage (S3 bucket) for storing the parquet files, and an RDB for the data warehouse and backups, all on Linode Cloud platform because it is less expensive and simpler than AWS, Azure, or Google Cloud.

    <img src="https://i.imgur.com/UBn8qkn.png" width="700">

### 2. DevOps

* In development mode, we use docker-compose to orchestrate the airflow pipeline and the Postgres database; because there will be large files, We will save them as binary parquet files using GIT LFS (Large File System). The remote parquet files from GitHub will be used for connections with PowerBI or Streamlit.

* In production mode, the EC2 instance will pull any changes from the development environment, save and retrieve data from the S3 bucket manually or automatically, and ingest the clean data into a Postgres data warehouse. PowerBI and Streamlit will be able to access this data warehouse and display dashboards in realtime.

    <img src="https://i.imgur.com/bbpSy6n.png" width="700">

### 3. Extraction

### 4. Transformation

### 5. Load

### 6. EDA

### 7. Machine Learning

## Products

### 1. PowerBI

The dashboard in PowerBI is in this [**LINK**](https://app.powerbi.com/view?r=eyJrIjoiYTUzODVkN2EtMWVlZC00ODMxLTk5MjQtOTdiY2Q1ZjgzYTdlIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9). Some screenshots:

* Image 1: Show the income disparity between countries with low, mid-low, mid-high, and high incomes. A dynamic map displaying the average life expectancy in each country:

    <img src="https://i.imgur.com/O9lUDk0.png" width="700">

* Image 2: A record of the behavior of life expectancy at birth according to year and income level:

    <img src="https://i.imgur.com/YAGbFwb.png" width="700">

* Image 2: A record about the behavior of the 7 factors that have the greatest influence on life expectancy:

    <img src="https://i.imgur.com/ZvoDa6Y.png" width="700">

### 2. Streamlit

## How to Install and Run the Project

### 1. Localy

* Para probarlo de manera local y experimentar con él, es necesario tener instalado docker y docker-compose en su computadora. Puedes verificar si lo tienes instalado con 

    ```bash
    docker --version
    docker-compose --version
    ```

* Deberías ver una respuesta para cada uno de una linea. De lo contrario revisa la [documentación de docker](https://docs.docker.com/desktop/) para seguir los pasos de instalación según tu sistema operativo.

* Una vez echo esto debes escribir el siguiente código para crear las variables de entorno que necesita Airflow para funcionar sin inconvenientes. Y las carpetas que serán utilizadas durante el flujo de trabajo

    ```bash
    mkdir -p ./dags ./logs ./plugins ./data
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```

* El código creará el archivo .env y las carpetas de forma automática, de lo contrario puedes renombrar el archivo llamado .env.sampre a .env y crear las carpetas manualmene. Si te encuentras en un sistema operativo que no sea Linu ss posible que obtengas una advertencia al iniciar el contenedor, pero funcionará de todos modos. Si quieres deshacerte de ella debes cambiar la línea dentro del archivo .env por

    ```
    AIRFLOW_UID=50000
    ```

* Al estar usando una versión extendida de Airflow, es necesario correr el siguiente código 

    ```bash
    docker build . --tag extending_airflow:latest
    ```

* De esta forma el archivo YAML se ejecutará sin inconvenientes al crear el contenedor con el siguiente comando

    ```bash
    docker-compose up airflow-init
    ```

* Por último ya lo podremos correr de forma normal con 

    ```bash
    docker-compose up -d
    ```

* Esto iniciará los contenedores de Docker con el servicio de Airflow, el schedule más una base de datos Postgres en la que se almacena la información.

### 2. Production

## How to ...

### 1. Contribute

Si deseas conocer el desarrollo del código más a fondo siempre puedes revisar la documentación en [el wiki](https://github.com/jorgeav527/life-expectancy/wiki). O acceder a los archivos .ipynb en los que se desarrolla paso a paso el código.

### 2. Use the Project

## Test

ToDo

## + Info

- [helper link](https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django)
- [helper link](https://forum.djangoproject.com/t/items-are-not-being-added-in-the-cart/10564/26)
- [helper link](https://stackoverflow.com/questions/1194737/how-to-update-manytomany-field-in-django)
- [helper link](https://pythonspeed.com/articles/alpine-docker-python/)

## *Licence GNU GPLv3*
