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

dag = DAG(dag_id="svpol_miner_dag",
          default_args=default_args,
          schedule_interval="1 0 * * *",
          start_date=datetime(2021, 9, 1)
          )

dag.doc_md = """
## svpol twitter miner
## svpol twitter miner updater
This job gets the latest tweets by searching for #svpol
"""

start = DummyOperator(task_id="Start", dag=dag)
run_script = BashOperator(task_id="mine_tweets",
                          bash_command="python3 /home/chrolss/PycharmProjects/svpol/miner.py",
                          dag=dag)

start >> run_script