import pandas as pd
import re

PATTERNS = {
    "url" : 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    "timestamp" : '\'\D{3}\s\D{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\s\\+\d{4}\s\d{4}\'',
    "at" : "@[a-zA-Z:]+",
    #"multi" : '([.?!/\\\\:]{2,})'
}


if __name__ == "__main__":
    
    df = pd.read_csv("./clean_tweets_eng_old.csv")
    try:
        df.drop(["Unnamed: 0"], axis = 1, inplace=True)
    except:
        print("columns ok")


    texts = df["text"]
    cleaned_list = []
    print("cleaning the list from regex patterns ...")
    ## cleaning the texts
    for r in texts:
        val = r
        for p in list(PATTERNS.keys()):
         val = re.sub(PATTERNS[p], "", val)
        
        cleaned_list.append(val)
    
    out_df = pd.DataFrame(cleaned_list, columns=["text"])

    out_df.to_csv("./cleaned_old_tweets_eng.csv")