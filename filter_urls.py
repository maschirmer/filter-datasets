# this script cleanes all texts in the future bert training dataset from urls

import pandas as pd
import re

FILEPATH = "./Datasets/temp_ds/statements_sh_bal_cleaned.csv"
COLUMN = "text"

def clean_urls():
    url_pat = "http[s]?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    df = pd.read_csv(FILEPATH)

    texts = df[COLUMN]
    clean_texts=[]

    for text in texts:
        clean_texts.append( re.sub(url_pat, "", text) )

    df[COLUMN] = clean_texts

    return df

if __name__=="__main__":
    
    df = clean_urls()

    df.to_csv("./statements_sh_bal_cleaned_no_url.csv")

