# svpol project

Data gathering and ETL repo of my #svpol project. This project contains all data download and manipulation scripts
as well as the airflow dags.

## Data Gathering
Daily pull of tweets containing #svpol hastag. Stored in `data/tweets` on format `yyyy-mm-dd.json`

Weekly check of new polling numbers from val.digital website. 

## ETL
Raw storage of tweets in json-format

Party support numbers are transformed on-download to a melted data modell stored in .pkl format. The file is overwritten at every run.

## Analysis
1. Run through tweets and store daily hashtag mentions

## Dashboarding
1. Timeseries plot of party polling numbers
2. Number of tweets for common hashtags
3. Trending hashtags displayed


## Random stuff
1. Start airflow in "one line" by writing `setsid airflow webserver` and `setsid airflow scheduler`
2. Run streamlit by `streamlit run app.py`