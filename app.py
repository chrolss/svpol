import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from src.analysis.twitter_nlp import extract_and_count_mentions, extract_and_count_hashtags, load_tweets

# Load data
df = pd.read_pickle("data/partisympatier.pkl")
tweets = load_tweets("data/tweets")
hashtags = extract_and_count_hashtags(tweets)

# Hashtag stuff
#TODO: Can't get this bar chart to work...
nr_of_tags = st.slider(label="# of tags", min_value=1, max_value=20, value=10, step=1)
hash_fig = st.bar_chart(data=hashtags["count"])

# Polling stuff
sample = df[df["company"] == "Demoskop"]
sample = sample[sample["publdate"] != "1900-01-01"]
sample.sort_values("publdate", inplace=True)

# Dropdown select widget
options = st.multiselect(label="Parti", options=sample["party"].unique().tolist())
date_input = st.date_input("Choose time period", [])

if options:
    sample = sample[sample["party"].isin(options)]

fig = px.line(data_frame=sample, x="publdate", y="support", hover_data=df[["party", "publdate", "support"]], color="party")
st.plotly_chart(fig, use_container_width=True)
