from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'danielliwag',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(name, age):
    print(f'hello airflow! my name is {name} and i am {age} yrs old')



with DAG(
    default_args= default_args,
    dag_id= 'dag_python',
    description = 'my first DAG using python operator',
    start_date= datetime(2025, 5, 10),
    schedule= '@daily'
) as dag:
    task1= PythonOperator(
        task_id= 'first_task',
        python_callable= greet,
        op_kwargs= {'name':'Daniel', 'age':26}
    )

    task1