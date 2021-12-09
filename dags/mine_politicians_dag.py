from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'colsson',
    'depends_on_past': False,
    'retries': 1,  # Maximum retries per scheduled instance
    'retry_delay': timedelta(minutes=15),  # Waittime between retries
}

dag = DAG(dag_id="mine_politicians_dag",
          default_args=default_args,
          schedule_interval="0 2 * * *",
          start_date=datetime(2021, 10, 20)
          )

dag.doc_md = """
## Mine Politicians Updater
This job downloads the latest tweet from a lost of Swedish political twitter accounts
"""

start = DummyOperator(task_id="Start", dag=dag)
run_script = BashOperator(task_id="mine_politicians",
                          bash_command="python3 /home/chrolss/PycharmProjects/svpol/mine_politicians.py",
                          dag=dag)

start >> run_script