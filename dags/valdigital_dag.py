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

dag = DAG(dag_id="val_digital_update",
          default_args=default_args,
          schedule_interval="0 12 * * *",
          start_date=datetime(2021, 8, 31)
          )

dag.doc_md = """
## Val.digital updater
This job downloads the latest political party polling data from val.digital
"""

start = DummyOperator(task_id="Start", dag=dag)
run_script = BashOperator(task_id="val.digital",
                          bash_command="python3 /home/chrolss/PycharmProjects/svpol/download_valdigital.py",
                          dag=dag)

start >> run_script