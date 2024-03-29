import pandas as pd
from langdetect import detect
from multiprocessing import Pool
import multiprocessing
import re
import gc

lang = []

PATH = "~/Datasets/"
CPUS = multiprocessing.cpu_count()

def getLang(text):
    try:
       l = detect(text)
    except:
        l = "none"
    return l

def collectres(l):
    lang.append(l)

if __name__ == "__main__":

    d = pd.read_csv(PATH + "reddit_may_2015/reddit_texts_split.csv", memory_map=True)
    
    try:
        d.drop(d.columns[0], axis=1, inplace=True)
        print("dropped col 0")
    except:
        print("columns ok!")
    ## compute the number of sentences per row
    num_sentences = []

    d.columns = ["body"]
    
    print(d.head())
    print(d.shape)
    
    split_body = d["body"]

    print("length of splitbody list is:" + str(len(split_body)))

    #split_body = split_body[:1000]
    #split_body = []

    # pattern = r'[.!?]'
    # print("splitting the reddit posts...")
    # for index, row in d.iterrows():
        
    #     string = str(row["body"])
    #     list = re.split(pattern, string)
    #     l2 = []

    #     for sentence in list:
    #         if len(sentence) > 3:
    #             l2.append(sentence)
    #             split_body.append(sentence)
        
    #     if index%10000==0:
    #         print(index)
        
    #     num_sentences.append(len(l2))
    n = len(split_body)
    
    for i in range(len(split_body)):
        try:
            lang.append(detect(split_body[i]))
        except:
            lang.append("none")
        if i%10000==0:
            print("processed: " + str(round((i/n)*100,3)))
    


    print(str(len(lang)))
    print( "is number of texts equal number of language annotations in lang: " + str( len(lang) == len(split_body) ) )
    
    
    # build dataframe and save to csv
    df_dict = {"text": split_body, "language":lang}
    df = pd.DataFrame(df_dict)
    df = df[ df["language"] == "en" ]
    
    df.to_csv(PATH + "temp_ds/" + "reddit_texts_language_seq.csv")