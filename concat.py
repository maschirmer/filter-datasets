# this script combines the datasets from twitter, reddit and blogs to a single dataset,
# where each portion has the same size, its balanced. the datset further gets shuffled
# and finally exported as csv file

import pandas as pd

PATH = "~/Datasets/"

if __name__ == "__main__":

    dt = pd.read_csv(PATH + "temp_ds/" + "cleaned_old_tweets_eng.csv")
    dt.drop(["Unnamed: 0"], axis = 1, inplace=True)
    dt["source"] = "twitter"
    print("size of twitter ds: " + str( dt.shape[0] ))

    db = pd.read_csv(PATH + "temp_ds/" + "blogs_news_single_sentences.csv")
    db.drop(["Unnamed: 0"], axis = 1, inplace=True)
    db["source"] = "blogs_news"
    print("size of blogs ds: " + str( db.shape[0] ))
    
    dr = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_seq.csv")
    dr.drop(["Unnamed: 0"], axis = 1, inplace=True)
    dr.drop(["language"], axis=1, inplace=True)
    dr["source"] = "reddit"
    print("size of reddit ds: " + str( dr.shape[0] ))

    blogs_n = db.shape[0]

    dt_s = dt.sample(n=blogs_n)
    dr_s = dr.sample(n=blogs_n)


    # sample from datasets to get the distributed sizes

    res = pd.concat([dt_s, db, dr_s], axis=0, ignore_index=True)

    shuffled = res.sample(frac=1).reset_index()

    print(shuffled.head())
    try:
        shuffled.drop(["Unnamed: 0"], axis=1, inplace=True)
    except:
        print("Columns OK")

    try:
        shuffled.drop(["index"], axis=1, inplace=True)
        print("removed index column")
    except:
        print("couldnt remove index col!")

    print("saving df ...")
            
    shuffled.to_csv(PATH + "temp_ds/" + "statements_shuffled_balanced.csv")