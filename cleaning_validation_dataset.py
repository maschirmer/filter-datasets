## sampling equally sized samples from each source to obtain a balanced dataset for 
# training of future bert classifier

import pandas as pd

TWITTER = "~/Datasets/temp_ds/clean_tweets_eng_old.csv"
REDDIT = "~/Datasets/reddit_may_2015/reddit_raw_texts.csv"
BLOGS = "~/Datasets/blogs_and_news/corpus.csv"

N = 1000


if __name__ == "__main__":

    twitter = pd.read_csv(TWITTER, index_col=0)
    
    reddit = pd.read_csv(REDDIT, index_col=0)
    reddit = reddit.rename(columns = {"body": "text"})
    
    blogs = pd.read_csv(BLOGS, index_col=0, encoding_errors="replace")
    blogs = blogs["body"].to_frame()
    blogs = blogs.rename(columns = {"body": "text"})

    t_small = twitter.sample(N,axis = 0, ignore_index=True)
    r_small = reddit.sample(N, axis = 0, ignore_index=True)
    b_small = blogs.sample(N, axis = 0, ignore_index=True)

    t_small["source"] = "twitter"
    r_small["source"] = "reddit"
    b_small["source"] = "blogsnews"

    print(list(twitter.columns))
    print(list(reddit.columns))
    print(list(blogs.columns))

    try:
        df = t_small.append(r_small).append(b_small)
        df = df.sample(frac=1.0, axis = 0, ignore_index=True).reset_index()

    except:
        print("Appending not possible")

    df.to_csv("./cleaning_eval_dataset.csv")
