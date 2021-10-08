from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'colsson',
    'depends_on_past': False,
    'retries': 2,  # Maximum retries per scheduled instance
    'retry_delay': timedelta(minutes=5),  # Waittime between retries
}

dag = DAG(dag_id="hashtag_extractor",
          default_args=default_args,
          schedule_interval="0 3 * * *",
          start_date=datetime(2021, 9, 30)
          )

dag.doc_md = """
## Hashtag extractor
This job extracts and accumulates the hashtags found in all #svpol tweets.

Serves as a basis for further analysis in the dash application.
"""

start = DummyOperator(task_id="Start", dag=dag)
run_script = BashOperator(task_id="extract_and_store_hashtags",
                          bash_command="python3 /home/chrolss/PycharmProjects/svpol/analysis.py",
                          dag=dag)

start >> run_script