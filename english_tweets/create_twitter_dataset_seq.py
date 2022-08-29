
import pandas as pd
import json
import os
import re

PATH_TO_DATA = "./twitter_stream_data"
CPUS = 64
results = []

PATTERNS = {
    "url" : 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    "timestamp" : '\'\D{3}\s\D{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\s\\+\d{4}\s\d{4}\'',
    "at" : "@[a-zA-Z:]+",
    #"multi" : '([.?!/\\\\:]{2,})'
}



def parseTweet(list):
    
    temp_results = []

    for i in range(len(list)):
        
        row = []
        
        try:

            if list[i]["lang"] == "en":
                
                try:
                    
                    row.append(list[i]["text"])
                    row.append(list[i]["created_at"])
                    
                    temp_results.append(row)

                except:  
                    print("no text or timestemp info")
        
        except:
            continue
    
    return  temp_results

def unpackJFile(filepath):
    with open(filepath, "rt", encoding="utf8") as jsoninput:
        lines = []
        for i, line in enumerate(jsoninput):
            tweets = json.loads(line)
            lines.append(tweets)
    return lines

def computeFilepaths_json(folder):
    
    res = []
    res2 = []
    
    print(PATH_TO_DATA)
    print(os.path.isdir(folder))
    print(os.listdir("./twitter_stream_data"))
    

    f1_names = [name for name in os.listdir(folder)]
    
    print(f1_names)


    for folder1 in f1_names:
        path = folder + "/" + folder1
        subfolder_names = [name for name in os.listdir(path)]
        for subfolder in subfolder_names:    
            subpath = path + "/" + subfolder
            # get filenames
            filenames = [name for name in os.listdir(subpath) ]  # if os.path.isdir(subpath)
            for file in filenames:
                filepath = subpath + "/" + file
                res.append(filepath)

    return res

def collectResults(res):
    results.extend(res)



if __name__ == '__main__':


    # paths of all unpacked jsonfiles
    print("computing filepaths ...")
    jsonpaths = computeFilepaths_json( PATH_TO_DATA )

    n = len(jsonpaths)
    k = 0

    print("starting extraction of english tweets...")
    for file in jsonpaths:

        for i in range(len(file)):
            try:
                if file[i]["lang"] == "en":    
                    try:
                        results.append(file[i]["text"])
                    except:  
                        print("no text or timestemp info")
            except:
                continue


        print("processed: " + str( round( (k/n)*100, 2 )) + "%")
        k += 1
    
    ## clean texts from timestamp

    cleaned_list = []
    print("cleaning the list from regex patterns ...")
    ## cleaning the texts
    for r in results:
        val = r
        for p in list(PATTERNS.keys()):
         val = re.sub(PATTERNS[p], "", val)
        
        cleaned_list.append(val)
    
    
    clean_df = pd.DataFrame(cleaned_list, columns=["text"])

    clean_df.to_csv("~/Datasets/temp_ds/clean_tweets_eng.csv")


########  End of Programme   #########
            


