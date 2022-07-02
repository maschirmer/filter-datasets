import pandas as pd

PATH = "~/Datasets/"

if __name__ == "__main__":

    d1 = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_1.csv")
    d2 = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_2.csv")
    d3 = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_3.csv")
    d4 = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_4.csv")
    d5 = pd.read_csv(PATH + "temp_ds/" + "reddit_texts_language_5.csv")

    res = pd.concat([d1, d2, d3, d4, d5], axis=0, ignore_index=True)

    print(res.head())

    res.to_csv(PATH + "temp_ds/" + "reddit_texts_language_5.csv")