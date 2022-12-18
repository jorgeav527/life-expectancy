from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


from dev_dir_creation import *
from dev_extraction import *
from dev_transformation import *
from dev_load import *

default_arg = {"owner": "yupana", "retries": 3, "retry_delay": timedelta(minutes=5)}

with DAG(
    default_args=default_arg,
    dag_id="extraccion_datos_v5",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@once",
    max_active_runs=1,
) as dag:
    dirs_creation = PythonOperator(
        task_id="creation_of_folders",
        python_callable=creacion_directorios,
    )
    creation_df_contry_twb = PythonOperator(
        task_id="creation_df_contry_twb",
        python_callable=country_twb,
    )
    creation_df_contry_unpd = PythonOperator(
        task_id="creation_df_contry_unpd",
        python_callable=country_unpd,
    )
    extraction_twb = PythonOperator(
        task_id="extraction_twb_indices",
        python_callable=extraccion_twb,
    )
    extraction_unpd = PythonOperator(
        task_id="extraction_unpd_indices",
        python_callable=extraccion_unpd,
    )
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
    load_to_db = PythonOperator(
        task_id="load_to_postgres_db",
        python_callable=cargar_base_de_datos,
    )

    (
        dirs_creation
        >> [creation_df_contry_twb, creation_df_contry_unpd]
        >> extraction_twb
        >> extraction_unpd
        >> transformation_twb_unpd
        >> final_transformations_twb_unpd
        >> rename
        >> new_columns_temp_tables
        >> [table_ingresos, table_paises, table_niveles, table_indices]
        >> remove_temp_table
        >> load_to_db
    )
