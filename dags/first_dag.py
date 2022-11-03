from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule


def hello():
    print("tarea 4")


with DAG(
    dag_id="primer_dag_v7",
    description="Nestro primer dag",
    start_date=datetime(2022, 10, 26),
    end_date=datetime(2022, 10, 28),
    schedule_interval="@once",
    default_args={"depends_on_past": True},
    max_active_runs=1,
) as dag:
    t1 = EmptyOperator(
        task_id="hello_from_bash_1",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        depends_on_past=False,
    )
    t2 = BashOperator(
        task_id="hello_from_bash_2",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        bash_command="sleep 5 && echo 'tarea 2'",
        depends_on_past=True,
    )
    t3 = BashOperator(
        task_id="hello_from_bash_3",
        trigger_rule=TriggerRule.ALL_SUCCESS,
        retries=2,
        retry_delay=5,
        bash_command="sleep 5 && echo 'tarea 3'",
        depends_on_past=True,
    )
    t4 = PythonOperator(
        task_id="hello_from_bash_4",
        python_callable=hello,
        retries=2,
        retry_delay=5,
        trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True,
    )
    t5 = BashOperator(
        task_id="hello_from_bash_5",
        bash_command="sleep 2 && echo 'tarea 5'",
        retries=2,
        retry_delay=5,
        # trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=True,
    )

    t1 >> t2 >> t3 >> t4 >> t5
