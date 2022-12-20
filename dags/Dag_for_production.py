from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


from prod_dir_creation import *
from prod_extraction import *
from prod_transformation import *
from prod_load import *
from prod_local_to_S3 import *
from prod_read_json import upload_datos_injectados_S3_bucket

default_arg = {"owner": "yupana", "retries": 3, "retry_delay": timedelta(minutes=5)}

with DAG(
    default_args=default_arg,
    dag_id="ETL_production_v6",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@once",
) as dag:
    # Extraction
    dirs_creation = PythonOperator(
        task_id="folders_creation",
        python_callable=creacion_directorios,
    )
    upload_S3_datos_inyectados = PythonOperator(
        task_id="upload_from_datos_inyectados_to_S3_bucket",
        python_callable=upload_datos_injectados_S3_bucket,
    )
    creation_df_contry_twb = PythonOperator(
        task_id="creation_of_df_contry_from_twb",
        python_callable=country_twb,
    )
    creation_df_contry_unpd = PythonOperator(
        task_id="creation_of_df_contry_from_unpd",
        python_callable=country_unpd,
    )
    extraction_twb = PythonOperator(
        task_id="twb_indice_extraction",
        python_callable=extraccion_twb,
    )
    extraction_unpd = PythonOperator(
        task_id="unpd_indice_extraction",
        python_callable=extraccion_unpd,
    )
    upload_S3_datos_brutos = PythonOperator(
        task_id="upload_from_datos_brutos_to_S3_bucket",
        python_callable=upload_datos_brutos_S3_bucket,
    )
    # Transformation
    transformation_twb_unpd = PythonOperator(
        task_id="read_and_transformation_for_twb_unpd",
        python_callable=read_and_transformation,
    )
    final_transformations_twb_unpd = PythonOperator(
        task_id="final_transformations_for_twb_unpd",
        python_callable=final_transformations,
    )
    rename = PythonOperator(
        task_id="rename_country_columns",
        python_callable=renombrar_columnas_paises,
    )
    new_columns_temp_tables = PythonOperator(
        task_id="create_new_columns_for_temp_tables",
        python_callable=crear_columnas_indicadores,
    )
    upload_S3_datos_pre_procesados = PythonOperator(
        task_id="upload_from_datos_pre_procesados_to_S3_bucket",
        python_callable=upload_datos_pre_procesados_S3_bucket,
    )
    # Load
    table_ingresos = PythonOperator(
        task_id="create_df_table_ingreso",
        python_callable=crear_ingresos,
    )
    table_paises = PythonOperator(
        task_id="create_df_table_pais",
        python_callable=crear_paises,
    )
    table_niveles = PythonOperator(
        task_id="create_df_table_nivel",
        python_callable=crear_niveles,
    )
    table_indices = PythonOperator(
        task_id="create_df_table_indice",
        python_callable=crear_indices,
    )
    remove_temp_table = BashOperator(
        task_id="remove_temporal_tables",
        bash_command="rm /opt/airflow/data/datos_pre_procesados/temp*.parquet",
    )
    upload_S3_datos_procesados = PythonOperator(
        task_id="upload_from_datos_procesados_to_S3_bucket",
        python_callable=upload_datos_procesados_S3_bucket,
    )
    load_to_db = PythonOperator(
        task_id="load_to_postgres_db_clusters",
        python_callable=cargar_base_de_datos,
    )

    (
        dirs_creation
        >> upload_S3_datos_inyectados
        >> [creation_df_contry_twb, creation_df_contry_unpd]
        >> extraction_twb
        >> extraction_unpd
        >> upload_S3_datos_brutos
        >> transformation_twb_unpd
        >> final_transformations_twb_unpd
        >> rename
        >> new_columns_temp_tables
        >> upload_S3_datos_pre_procesados
        >> [table_ingresos, table_paises, table_niveles, table_indices]
        >> remove_temp_table
        >> upload_S3_datos_procesados
        >> load_to_db
    )
