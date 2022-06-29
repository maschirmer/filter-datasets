import pandas as pd
import static_filter


filter = static_filter.StaticFilter("./english_tweets/clean_tweets_eng.csv")

df = filter.filter()


df.to_csv("twitter_statements_tenses.csv")