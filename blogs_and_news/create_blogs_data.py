import pandas as pd
import re


FILEPATH = "~/Datasets/"


if __name__ == "__main__":
    
    
    df = pd.read_csv(FILEPATH + "blogs_and_news/corpus.csv", encoding_errors="replace")
    lbody = list(df["body"])

    # split strings to sentences by "!?."
    sentences = []
    for text in lbody:
        sentences.extend( re.split(r'[.!?]', text) )


    # remove split' sentences that are just a few characters
    n = len(sentences)

    for i in range(len(sentences)):
        
        if len(sentences[i]) < 4:
            sentences.remove(sentences[i])
        
        if i%100000 == 0:
            print( round( str((i/n) * 100), 2 ) )


    # count any left empty strings
    count = 0
    for i in range(len(sentences)):
        if sentences[i] == "":
            count += 1 

    print( "number of left empty strings: " + str(count) )
    print( "number of sentences: " + str(len(sentences)) )
    print( "percentage of empty strings: " + str( (count / len(sentences)) *100 ) )


    # make df an reset the indices for later use
    sen = pd.DataFrame(sentences, columns=["text"])
    sen = sen.reset_index()
    sen.drop("index", axis="columns", inplace=True)


    # save to csv
    sen.to_csv(FILEPATH + "temp_ds/blogs_news_single_sentences.csv", encoding="utf8")



    ##### END #####