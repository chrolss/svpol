import requests
import pandas as pd

def get_polling_data(data_sink: str):
    # Url från val.digital med alla mätningar
    url = "https://val.digital/Polls.csv"

    # Läs in i en dataframe
    df = pd.read_csv(url)

    # Melt till en ny tidy-data-variant
    tf = pd.melt(df, id_vars=['PublDate', "Company", "n", "collectPeriodFrom", "collectPeriodTo"], value_vars=["M", "L", "C", "KD", "S", "V", "MP", "SD", "FI", "Uncertain"], var_name='party', value_name='support')

    # Clean the dataframe before storing in local .csv-file
    tf["n"] = tf["n"].fillna(0)

    # Do some dtype conversions for dates
    # PublDate, collectPeriodFrom, collectPeriodTo
    date_cols = ["PublDate", "collectPeriodFrom", "collectPeriodTo"]
    for date_col in date_cols:
        tf[date_col] = tf[date_col].fillna("1900-01-01")
        tf[date_col] = pd.to_datetime(tf[date_col])

    tf.columns = [col.lower() for col in tf.columns]

    # Store the clean .csv-file 
    tf.to_csv(data_sink + "/data/partisympatier.csv", index=False)

    # Store as pickle in order to keep dtypes
    tf.to_pickle(data_sink + "/data/partisympatier.pkl")

    return True
