import pandas as pd
from pandas import DataFrame
import re
import glob

def load_tweets(path: str) -> DataFrame:
    df = pd.concat([pd.read_json(f, lines=True) for f in glob.glob(path + "/*.json")])

    return df

#TODO: Combined the extract functions into one
def extract_and_count_hashtags(df: DataFrame):
    # Goes through all tweets and extracts the hashtags, then counts them (aggregate somehow?)
    result = dict()
    for tweet in df["tweet"]:
        hashtags = re.findall(r"#\w+", tweet)
        if hashtags:
            for hashtag in hashtags:
                if hashtag in result.keys():
                    result[hashtag] += 1
                else:
                    result[hashtag] = 1


    output = pd.DataFrame(columns=["hashtag", "count"])
    output["hashtag"] = result.keys()
    output["count"] = result.values()
    output = output.sort_values(by="count", ascending=False)
    return output

def extract_and_count_mentions(df: DataFrame):
    # Goes through all tweets and extracts the mentions, then counts them (aggregate somehow?)
    result = dict()
    for tweet in df["tweet"]:
        hashtags = re.findall(r"@\w+", tweet)
        if hashtags:
            for hashtag in hashtags:
                if hashtag in result.keys():
                    result[hashtag] += 1
                else:
                    result[hashtag] = 1


    output = pd.DataFrame(columns=["user_mention", "count"])
    output["user_mention"] = result.keys()
    output["count"] = result.values()
    output = output.sort_values(by="count", ascending=False)
    return output
