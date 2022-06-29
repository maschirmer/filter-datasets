import json
import pandas as pd

class StaticFilter:
    
    '''instantiate with csv dataset, which needs to be with columns [text]\n

        filter() returns a dict of style:\n

        text : list of texts
        future : list of integers from {0,1})\n
        0 --> not future related\n
        1 --> future related '''

    ##
    ## load the filter keywords from json file
    ## filter is working as following:
    ## if one of [timerefs] or one of [refs] or [verbs] in so stage1 == 1
    ## for these pass through [stage2]
    # stemming has to be considered due to conjugation

    def __init__(self, dataset, keywords):
        
        with open(keywords, "r", encoding="utf8") as f:
            d = json.load(f)
        f.close()
        
        self.stage1 = []
        
        self.stage1.extend( d["stage1"]["timerefs"] )
        self.stage1.extend( d["stage1"]["verbs"] )
        self.stage1.extend( d["stage1"]["refs"] )

        # not really stemmed but consider stemming based on performance of the filter
        self.stage2 = d["stage2"]["stemmed_verbs"] 

        self.dataset = dataset

    def filter(self):
        # takes the dataset as input and outputs a dictionary {text:future}, where: 
        # 1 for future related
        # 0 for for not future related

        
        df = pd.read_csv(self.dataset, index_col=0)
        
        texts = df["text"]
        print(len(texts))
        futures = []
        k = 0
        for i in range(len(texts)):
            
            s1 = False
            s2 = False

            for keyword in self.stage1:
                if keyword in texts[i]:
                    s1 = True
            
            if s1 == False:
                futures.append(0)
            
            else:    
                
                for keyword in self.stage2:
                    if keyword in texts[i]:
                        s2 = True
                
                if s1 == True and s2 == True:
                    futures.append(1)
                else:
                    futures.append(0)
            print(k)
            k += 1
        if len(texts) == len(futures):
            df["tense"] = futures

            return df
        
        else:

            return pd.DataFrame(columns=["text"])



if __name__ == "__main__":
    

    filter = StaticFilter("./english_tweets/cleaned_tweets_eng.csv", keywords="./english_tweets/keywords.json")

    df = filter.filter()

    df.to_csv("twitter_statements_tenses.csv")




