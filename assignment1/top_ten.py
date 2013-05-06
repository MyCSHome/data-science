import sys
import json
from collections import Counter



def find_state(dic, tweet_file):
    hash_state = Counter()
    for line in tweet_file:
        t = json.loads(line)
        if "text" in t:
            place = t["place"]
            if place != None:
                if place["country_code"] == "US":
                    state = place["full_name"][-2:]
                    score = get_score(t, dic)
                    if state in hash_state:
                        hash_state[state] += score
                    else:
                        hash_state[state] = score
    if len(hash_state) == 0:
        print "none"
    results = hash_state.most_common(10)
    for result in results:
        print result[0], result[1]
    
        
                    
def get_tags(tweet_file):
    hash_tag = {}
    for line in tweet_file:
        t = json.loads(line)
        if "entities" in t:
            entity = t["entities"]
            tag = entity["hashtags"]
            if tag != []:
                text = tag[0]["text"]
                if text in hash_tag:
                    hash_tag[text] += 1.0
                else:
                    hash_tag[text] = 1.0
    #print text
    if len(hash_tag) == 0:
        print "none"
    max = -100000
    hap = ""
    for text in hash_tag:
        if hash_tag[text] > max:
            max = hash_tag[text]
            hap = text
    print hap
            
    
def main():
    tweet_file = open(sys.argv[1])
    get_tags(tweet_file)
    tweet_file.close()
 







if __name__ == '__main__':
    main()