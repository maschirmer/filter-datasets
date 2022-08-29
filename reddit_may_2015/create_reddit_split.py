import pandas as pd
from langdetect import detect
from multiprocessing import Pool
import multiprocessing
from nltk import sent_tokenize

lang = []

PATH = "~/Datasets/"
CPUS = multiprocessing.cpu_count()

def getLang(text):
    try:
       l = detect(text)
    except:
        l = "none"
    return l

def collectres(lang):
    lang.append(lang)

if __name__ == "__main__":

    d = pd.read_csv(PATH + "reddit_may_2015/reddit_raw_texts.csv")
    
    d.drop(["Unnamed: 0"], axis=1, inplace=True)

    df = d.sample(n=5000000, axis = 0, ignore_index=True)
    ## compute the number of sentences per row
    split_body = []
    
    # nltk tokenize
    for index, row in df.iterrows():
        try:
            split_body.extend(sent_tokenize(row["body"]))
        except:
            continue
        
        if index%10000==0:
            print(index)


    dataf = pd.DataFrame(split_body, columns=["body"])
    dataf.to_csv("./reddit_texts_split.csv")
    