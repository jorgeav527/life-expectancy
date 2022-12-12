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
    
    <kbd><img src="https://i.imgur.com/vBQixZT.png" width="700"></kbd>

* In production, it will use an EC2 for the airflow pipeline, an Object Storage (S3 bucket) for storing the parquet files, and an RDB for the data warehouse and backups, all on Linode Cloud platform because it is less expensive and simpler than AWS, Azure, or Google Cloud.

    <kbd><img src="https://i.imgur.com/UBn8qkn.png" width="700"></kbd>

### 2. DevOps

* In development mode, we use docker-compose to orchestrate the airflow pipeline and the Postgres database; because there will be large files, We will save them as binary parquet files using GIT LFS (Large File System). The remote parquet files from GitHub will be used for connections with PowerBI or Streamlit.

* In production mode, the EC2 instance will pull any changes from the development environment, save and retrieve data from the S3 bucket manually or automatically, and ingest the clean data into a Postgres data warehouse. PowerBI and Streamlit will be able to access this data warehouse and display dashboards in realtime.

    <kbd><img src="https://i.imgur.com/bbpSy6n.png" width="700"></kbd>

### 3. Extraction

* ToDo

### 4. Transformation

* ToDo

### 5. Load

* ToDo

### 6. EDA

* ToDo

### 7. Machine Learning

* ToDo

## Products

### 1. PowerBI

The dashboard in PowerBI is in this [**LINK**](https://app.powerbi.com/view?r=eyJrIjoiYTUzODVkN2EtMWVlZC00ODMxLTk5MjQtOTdiY2Q1ZjgzYTdlIiwidCI6IjBlMGNiMDYwLTA5YWQtNDlmNS1hMDA1LTY4YjliNDlhYTFmNiIsImMiOjR9). Some screenshots:

* Image 1: Show the income disparity between countries with low, mid-low, mid-high, and high incomes. A dynamic map displaying the average life expectancy in each country:

    <kbd><img src="https://i.imgur.com/O9lUDk0.png" width="700"></kbd>

* Image 2: A record of the behavior of life expectancy at birth according to year and income level:

    <kbd><img src="https://i.imgur.com/YAGbFwb.png" width="700"></kbd>

* Image 2: A record about the behavior of the 7 factors that have the greatest influence on life expectancy:

    <kbd><img src="https://i.imgur.com/ZvoDa6Y.png" width="700"></kbd>

### 2. Streamlit

ToDo

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

* ToDo

## How to ...

### 1. Contribute

* If you want to learn more about the code's development, check out the documentation on [**WIKI**](https://github.com/jorgeav527/life-expectancy/wiki) (Sorry, but the documentation for the KPI we want to demonstrate is in Spanish). 

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

## *Licence GNU GPLv3*
