# Life Expentancy

<kbd><img src="https://i.imgur.com/5PxDz2P.png" width="500"></kbd>

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
      * [2. DevOps](#2-devops)
      * [3. Extraction](#3-extraction)
      * [4. Transformation](#4-transformation)
      * [5. Load](#5-load)
      * [6. EDA](#6-eda)
      * [7. Machine Learning](#7-machine-learning)
   * [Products](#products)
      * [1. Airflow](#1-airflow)
      * [2. Streamlit](#2-streamlit)
      * [3. PowerBI](#3-powerbi)
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
<!-- Added by: jorgeav527, at: Tue 20 Dec 13:21:50 -05 2022 -->

<!--te-->

## Parts of the Project

### 1. Architecture

* We are building a pipeline with Apache-airflow. It begins by **Extracting** raw data from the World Bank, World Health Organization, and United Nations via their respective APIs. Second, we **Transform** this raw using a bucket to save and retrieve data in parquet format. Third, we **Load** this clean data into a Postgres Data Warehouse so that it is ready for any PowerBI or Streamlit connections.
    
    <kbd><img src="https://i.imgur.com/fFoGl3d.png" width="700"></kbd>

* In production, it will use an EC2 for the airflow pipeline, an Object Storage (S3 bucket) for storing the parquet files, and an RDB for the data warehouse and backups, all on Linode Cloud platform because it is less expensive and simpler than AWS, Azure, or Google Cloud.

    <kbd><img src="https://i.imgur.com/UBn8qkn.png" width="700"></kbd>

### 2. DevOps

* In development mode, we use docker-compose to orchestrate the airflow pipeline and the Postgres database; because there will be large files, We will save them as binary parquet files using GIT LFS (Large File System). The remote parquet files from GitHub will be used for connections with PowerBI or Streamlit.

* In production mode, the EC2 instance will pull any changes from the development environment, save and retrieve data from the S3 bucket manually or automatically, and ingest the clean data into a Postgres data warehouse. PowerBI and Streamlit will be able to access this data warehouse and display dashboards in realtime.

    <kbd><img src="https://i.imgur.com/bbpSy6n.png" width="700"></kbd>

### 3. Extraction

* First, we will select the indices that we will request from the APIs and add them to the corresponding json file.
    
   ```json
    data/datos_inyectados/naciones_unidas.json
    {
        "22": ["mort", "tasa_mortalidad_infantil"],
        "54": ["pop", "densidad_población_por_kilómetro_cuadrado)"],
        "65": ["imigrt", "migración_neta_total"],
        "49": ["pop", "población_total_por_sexo"],
        "60": ["mort", "total_muertes_por_sexo"],
        "53": ["pop", "tasa_bruta_cambio_natural_población"],
        "66": ["imigrt", "tasa_bruta_migración_neta"],
        "72": ["pop", "proporción_sexos_población_total"],
        "1": ["fam", "prevalencia_anticonceptivos_porcentaje"],
        "67": ["pop", "mediana_edad_población"],
        "59": ["mort", "tasa_bruta_mortalidad_por_1000_habitantes"],
        "51": ["pop", "tasa_bruta_variación_total_población"],
        "50": ["pop", "cambio_de_la_población"],
        "41": ["pop", "población_femenina_edad_reproductiva_(15-49 años)"],
        "24": ["mort", "tasa_mortalidad_menores_cinco_años"],
        "52": ["pop", "cambio_natural_población"],
        "19": ["fert", "tasa_fertilidad"],
        "42": ["marstat", "estado_civil_casado_porcentaje"]
    }
    ```

    ```json
    data/datos_inyectados/banco_mundial.json
    {
        "SP.DYN.LE00.IN": "esperanza_vida_total",
        "SP.DYN.LE00.FE.IN": "esperanza_vida_mujeres",
        "SP.DYN.LE00.MA.IN": "esperanza_vida_varones",
        "SI.POV.GINI": "índice_gini",
        "SE.XPD.TOTL.GD.ZS": "gasto_púb_educacion_pje",
        "SE.COM.DURS": "duración_educ_obligatoria",
        "NY.GDP.PCAP.CD": "pib_pc_usd_actuales",
        "NY.GDP.MKTP.PP.CD": "pib_ppa_prec_inter",
        "IQ.SCI.OVRL": "capacidad_estadística",
        "SP.POP.TOTL.FE.ZS": "población_mujeres_pje",
        "SP.POP.TOTL.MA.ZS": "población_hombres_pje",
        "NY.GDP.PCAP.PP.CD": "pib_pc_prec_inter",
        "AG.LND.FRST.ZS": "porcentaje_de_bosque",
        "EN.ATM.CO2E.PC": "emisiones_co2",
        "SH.XPD.CHEX.PC.CD": "inversion_salud_percapita",
        "SH.MED.BEDS.ZS": "camas_hospitales_c/1000personas",
        "SP.DYN.IMRT.IN": "mortalidad_infantil_c/1000nacimientos",
        "SH.H2O.BASW.ZS": "acceso_agua_potable(%)",
        "SH.STA.BASS.ZS": "acceso_servicios_sanitarios(%)",
        "SH.STA.SUIC.P5": "tasa_mortalidad_suicidio_c/100.000",
        "SL.UEM.TOTL.ZS": "tasa_desempleo",
        "SP.URB.TOTL.IN.ZS": "tasa_poblacion_urbana",
        "NY.GNP.PCAP.CD": "INB_percapita",
        "PV.EST": "estabilidad_política"
    }
    ```

    ```json
    data/datos_inyectados/mundial_salud.json
    {
       "M_Est_cig_curr": "df_OMS_M_Est_cig_curr",
       "NCD_BMI_30A": "df_OMS_NCD_BMI_30A",
       "NUTRITION_ANAEMIA_CHILDREN_PREV": "df_OMS_NUTRITION_ANAEMIA_CHILDREN_PREV",
       "NUTRITION_ANAEMIA_REPRODUCTIVEAGE_PREV": "df_OMS_NUTRITION_ANAEMIA_REPRODUCTIVEAGE_PREV",
       "SA_0000001688": "df_OMS_SA_0000001688"
    }        
    ```

* So, in this first section, we create the folders called "datos brutos", "datos pre procesados", and "datos procesados" where we will save and retrieve data.
* Next, from The World Bank and The United Nations API raw data will then be used to generate a countries dataframe.
* We will generate raw data from the previously chosen indices in the injected json data files.

    | Development | Production |
    | --- | ----------- |
    | folders_creation | folders_creation |
    | creation_of_df_contry_from_twb | upload_from_datos_inyectados_to_S3_bucket |
    | creation_of_df_contry_from_unpd | creation_of_df_contry_from_twb |
    | twb_indice_extraction | creation_of_df_contry_from_unpd |
    | unpd_indice_extraction | twb_indice_extraction |
    | | unpd_indice_extraction |
    | | upload_from_datos_brutos_to_S3_bucket |

 

### 4. Transformation

* For the transformation state, we will create a table dataframe with all indices extracted previously.
* Rename all columns with the extracted indices in Spanish.
* We also create new temporal tables dataframes for each table in the database that we will create in the following step.

    | Development | Production |
    | --- | ----------- |
    | read_and_transformation_for_twb_unpd | read_and_transformation_for_twb_unpd |
    | final_transformations_for_twb_unpd | final_transformations_for_twb_unpd |
    | rename_country_columns | rename_country_columns |
    | create_new_columns_for_temp_tables | create_new_columns_for_temp_tables |
    | | upload_from_datos_pre_procesados_to_S3_bucket |

### 5. Load

* Finally, we create each data table for the data warehouse for this project. We chose two fact tables "ingreso" and two describe tables "pais" and "nivel."
* The data is then loaded into a Postgres database.

    | Development | Production |
    | --- | ----------- |
    | create_df_table_ingreso | create_df_table_ingreso |
    | create_df_table_pais | create_df_table_pais |
    | create_df_table_nivel | create_df_table_nivel |
    | create_df_table_indice | create_df_table_indice |
    | remove_temporal_tables | remove_temporal_tables |
    | load_to_postgres_db | upload_from_datos_procesados_to_S3_bucket |
    | | load_to_postgres_db_clusters |

### 6. EDA

* ToDo

### 7. Machine Learning

* ToDo

## Products

### 1. Airflow

**In development**

* we use Git-LFS to track, save, and retrieve data from the data/ folder.
* We use notebooks in draft/folders to connect to API sources, perform exploratory data analysis on the extracted raw data, transform the extracted raw data, and load it into various data bases.

* Extraction

    <kbd><img src="https://i.imgur.com/ZdLV4OM.png" width="700"></kbd>

* Transformation

    <kbd><img src="https://i.imgur.com/gUBJEjz.png" width="800"></kbd>

* Load

    <kbd><img src="https://i.imgur.com/Qgwo8gz.png" width="700"></kbd>

**In production**

* We use an EC2 instance on Linode to handle the Airflow, which is connected to an S3 bucket on Linode Object Storage to track, save, and retrieve data, and the data-warehouse is finally stored in Database Clusters on Linode's platform.

* Extraction

    <kbd><img src="https://i.imgur.com/xWg2LlV.png" width="700"></kbd>

* Transformation

    <kbd><img src="https://i.imgur.com/xWg2LlV.png" width="700"></kbd>

* Load

    <kbd><img src="https://i.imgur.com/SBvKHVE.png" width="700"></kbd>

### 2. Streamlit

ToDo

### 3. PowerBI

The dashboard in [**PowerBI**](https://app.powerbi.com/view?r=eyJrIjoiYTUzODVkN2EtMWVlZC00ODMxLTk5MjQtOTdiY2Q1ZjgzYTdlIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9). Some screenshots:

* This is the data warehouse connection from Linode's Database Clusters to PowerBI.

    <kbd><img src="https://i.imgur.com/TL6aQnd.jpg" width="700"></kbd>

* Image 1: Show the income disparity between countries with low, mid-low, mid-high, and high incomes. A dynamic map displaying the average life expectancy in each country:

    <kbd><img src="https://i.imgur.com/O9lUDk0.png" width="700"></kbd>

* Image 2: A record of the behavior of life expectancy at birth according to year and income level:

    <kbd><img src="https://i.imgur.com/YAGbFwb.png" width="700"></kbd>

* Image 2: A record about the behavior of the 7 factors that have the greatest influence on life expectancy:

    <kbd><img src="https://i.imgur.com/ZvoDa6Y.png" width="700"></kbd>

## How to Install and Run the Project

### 1. Localy

* To experiment with it locally, you must have docker and docker-compose installed on your computer. You can check if you have it installed by using

    ```bash
    docker --version
    docker-compose --version
    ```

* If not, consult the [**Docker**](https://docs.docker.com/desktop/) for installation instructions specific to your operating system.

* To create the environment variables and folders that will be used during the Airflow workflow.

    ```bash
    mkdir -p ./dags ./logs ./plugins ./data
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
* For Linux, this code will automatically generate the .env file and folders; alternatively, create the folders manually and rename the file.env.sample to.env and add the following line.

    ```
    AIRFLOW_UID=50000
    ```

* When using an extended version of Airflow, the following code must be executed to extend the Airflow Docker Image.

    ```bash
    docker build . --tag extending_airflow:latest
    ```

* When creating the container with the following command, the docker-compose YAML file will be executed without error.

    ```bash
    docker-compose up airflow-init
    ```

* This will start the Docker containers with the Airflow service, the schedule, and a Postgres database to store the data.

* Finally we can run it with

    ```bash
    docker-compose up -d
    ```

### 2. Production

* So we're launching Ubuntu 22.04.1 LTS. Say yes to the fingerprint and add the password on a Linode instance, which is very similar to an EC2 AWS instance.
* Install [**docker**](https://docs.docker.com/engine/install/ubuntu/#install-from-a-package) & [**docker compose**](https://docs.docker.com/compose/install/linux/)
* Make a [**ssk-key**](https://vitux.com/ubuntu-ssh-key/) for GitHub

    ```bash
    ssh-keygen -t ed25519 -b 4096
    ```

* We clone and add the corresponding .env file with the S3 bucket and Postgres database keys.
* Remember to change the third line of the Dockerfile because we are no longer using jupyter or black.

    ```docker
    # FROM apache/airflow:2.4.2
    # COPY /requirements/ /requirements/
    # RUN pip install --user --upgrade pip
    RUN pip install --no-cache-dir --user -r /requirements/production.txt
    ```

* Extend version of Airflow, create the container with the docker-compose YAML, start the Docker containers with the Airflow service.

    ```bash
    docker build . --tag extending_airflow:latest
    docker-compose up airflow-init
    docker-compose up -d
    ```
* Open 8080 port and run the *Dag_for_production*.

## How to ...

### 1. Contribute

* If you want to learn more about the code's development, check out the documentation on [**Wiki**](https://github.com/jorgeav527/life-expectancy/wiki) (Sorry, but the documentation for the KPI we want to demonstrate is in Spanish). 

* Alternatively, you can access the notebooks in the draft file in which the code is developed step by step.

### 2. Use the Project

* You can learn from the architecture we designed and the pipeline we implemented.

* You can play around with the PowerBI dashboard or get your own conclusions using the machine learning models we use. The links can be found in the Produce section.

## Test

ToDo

## + Info

- [helper link](https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django)
- [helper link](https://forum.djangoproject.com/t/items-are-not-being-added-in-the-cart/10564/26)
- [helper link](https://stackoverflow.com/questions/1194737/how-to-update-manytomany-field-in-django)
- [helper link](https://pythonspeed.com/articles/alpine-docker-python/)
- [dependency resolver and version conflicts](https://codingshower.com/pip-dependency-resolver-and-version-conflicts/)
- [add border to image in github markdown](https://stackoverflow.com/questions/37349314/is-it-possible-to-add-border-to-image-in-github-markdown/63827723#63827723)
- [linode object-storage guides for python](https://www.linode.com/docs/products/storage/object-storage/guides/aws-sdk-for-python/)
- [delete multiple files and specific pattern in s3 boto3](https://stackoverflow.com/questions/65175454/how-to-delete-multiple-files-and-specific-pattern-in-s3-boto3)
- [linode urls](https://www.linode.com/docs/products/storage/object-storage/guides/urls/)

## *Licence GNU GPLv3*
