from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'danielliwag',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    description= 'This is my first dag',
    start_date= datetime(2025, 5, 9, 21),
    schedule= '@hourly'
) as dag:
    task1 = BashOperator(
        task_id= 'first_task',
        bash_command= 'echo hello world, this is my first task!'
    )

    task2 = BashOperator(
        task_id= 'second_task',
        bash_command= 'echo im the second task'
    )

    task3= BashOperator(
        task_id= 'third_task',
        bash_command= 'echo im the third task'
    )

    task1 >> [task2, task3]