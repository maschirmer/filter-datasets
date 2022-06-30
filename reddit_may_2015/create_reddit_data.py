import pandas as pd
from langdetect import detect
from multiprocessing import Pool
import multiprocessing
import re

lang = []

PATH = "~/Datasets/"

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


    ## compute the number of sentences per row
    
    num_sentences = []
    split_body = []

    pattern = r'[.!?]'
    
    for index, row in d.iterrows():
        
        string = str(row["body"])
        list = re.split(pattern, string)
        l2 = []

        for sentence in list:
            if len(sentence) > 3:
                l2.append(sentence)
                split_body.append(sentence)
        
        num_sentences.append(len(l2))


    # body = list(d["body"])
    body = split_body

    print("no of cpus to use: " + str(multiprocessing.cpu_count()))
    
    pool = Pool(processes=multiprocessing.cpu_count())

    for i in range(len(body)):
        pool.apply_async(getLang, args=(body[i], ), callback=collectres)
        print(i)
    
    pool.close()
    pool.join()


    print(str(len(lang)))
    print( "is number of texts equal number of language annotations in lang: " + str(len(lang) == len(split_body) ) )
    
    
    # build dataframe and save to csv
    df_dict = {"text": split_body, "language":lang}
    df = pd.DataFrame(df_dict)
    df = df[ df["language"] == "en" ]

    df.to_csv(PATH + "temp_ds/" + "reddit_texts_language.csv")