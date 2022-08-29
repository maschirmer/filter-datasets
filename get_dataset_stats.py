## script to retrieve stats from the training dataset for futurebert
#  number of samples per source (should be equal for each source)
#  descriptive statistics of word count per text item (sentence) per source
# 


import pandas as pd
import numpy as np
import gc


if __name__ == "__main__":

    df = pd.read_csv("statements_static1.csv", index_col=0)

    n_counts = df.groupby("source")["text"].count()

    df_twitter = df[ df["source"] == "twitter" ]
    df_blogs = df[ df["source"] == "blogs_news" ]
    df_reddit = df[ df["source"] == "reddit" ]


    del df #delete df to free memory
    gc.collect()

    ## count number of words for each row for each source

    print(df_twitter.dtypes)
    print(df_blogs.dtypes)
    print(df_reddit.dtypes)

    twitter_texts = list(df_twitter["text"])
    twitter_word_counts = []
    for t in twitter_texts:
        try:
            twitter_word_counts.append( len( t.split() ) )
        except:
            twitter_word_counts.append( np.nan )

    #twitter_word_counts = [ len(x.split()) for x in twitter_texts ]
    print("computed word counts for twitter")
    print()


    blogs_texts = list(df_blogs["text"])
    blogs_word_counts = []
    for t in blogs_texts:
        try:
            blogs_word_counts.append( len( t.split() ) )
        except:
            blogs_word_counts.append( np.nan )
    #blogs_word_counts = [ len(x.split()) for x in blogs_texts ]
    print("computed word counts for blogs & news")
    print()

    reddit_texts = list(df_reddit["text"])
    reddit_word_counts = []
    for t in reddit_texts:
        try:
            reddit_word_counts.append( len( t.split() ) )
        except:
            reddit_word_counts.append( np.nan )
    #reddit_word_counts = [ len(x.split()) for x in reddit_texts ]
    print("computed word counts for reddit")
    print()

    w_count_df = pd.DataFrame( { "twitter": twitter_word_counts, "reddit": reddit_word_counts, "blogs": blogs_word_counts }, dtype=int )

    w_count_stats = w_count_df.describe()

    # save dataframes to csv
    print("storing dataframes as csv ...")

    n_counts.to_csv("training_set_counts.csv")
    w_count_df.to_csv("training_set_word_counts.csv")
    w_count_stats.to_csv("training_set_word_counts_statistics.csv")
