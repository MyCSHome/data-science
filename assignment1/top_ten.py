﻿import sys
import json
from collections import Counter
       
def get_tags(tweet_file):
    hash_tag = Counter()
    for line in tweet_file:
        t = json.loads(line)
        if "entities" in t:
            entity = t["entities"]
            tags = entity["hashtags"]
            if tags != []:
                for tag in tags:
                    text = tag["text"]
                    if text in hash_tag:
                        hash_tag[text] += 1.0
                    else:
                        hash_tag[text] = 1.0
    #print text
    # if len(hash_tag) == 0:
        # print "none"
    
    results = hash_tag.most_common(10)
    #print len(results), type(results)
    for result in results:
        key = result[0].encode('utf-8')
        print key, result[1]
            
    
def main():
    tweet_file = open(sys.argv[1])
    get_tags(tweet_file)
    tweet_file.close()
 

if __name__ == '__main__':
    main()