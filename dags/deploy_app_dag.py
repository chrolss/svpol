from airflow.decorators import task, dag
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

from datetime import datetime
@dag(start_date=datetime(2021,12,1), schedule_interval="0 5 * * *", catchup=False)
def docker_dag():
    t1 = DummyOperator(
        task_id="Start"
    )

    t2 = BashOperator(
        task_id="build_push",
        bash_command="cd ~/PycharmProjects/svpol-dash; heroku container:push web -a svpol-analytics"
    )

    t3 = BashOperator(
        task_id="release_deploy",
        bash_command="cd ~/PycharmProjects/svpol-dash; heroku container:release web -a svpol-analytics"
    )

    t1 >> t2 >> t3

dag = docker_dag()

dag.doc_md = """
This dag will build the svpol-dash project and update its docker container, and if successful it will deploy
it to the Heroku cloud.
"""

