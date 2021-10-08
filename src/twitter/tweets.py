import twint

c = twint.Config()

def store_svpol_tweets(folder:str, since: str, last_date: str):
    # Function for scraping twitter for hashtag svpol
    c.Search = "#svpol"
    c.Store_json = "True"
    c.Output = folder + "/data/tweets/svpol/{0}.json".format(last_date)
    c.Since = since
    twint.run.Search(c)


def store_politician_tweets(folder: str, since: str, username: str):
    # Function for collecting all tweets from a specific user
    c.Username = username
    c.Store_json = "True"
    c.Output = folder + "/data/tweets/politicians/{0}.json".format(username)
    c.Since = since
    twint.run.Search(c)
