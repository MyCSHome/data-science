import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_dic(sent_file):
    dic = {}
    for entry in sent_file:
        entry_list = entry.split()
        if len(entry_list) == 2:
            dic[entry_list[0]] = float(entry_list[1])
        else:
            entry_name = ""
            for i in range(0, len(entry_list) - 1):
                entry_name += entry_list[i]
            dic[entry_name] = float(entry_list[-1])
    return dic

def get_sec_dic(tweet_file, sent_dic):
    dic = {}
    for t in tweet_file:
        tweet = json.loads(t)
        if "text" in tweet:
            t_text = tweet["text"]
            words = t_text.split()
            score = 0
            for word in words:
                if word in sent_dic:
                    score += sent_dic[word]
            for word in words:
                if word not in sent_dic:
                    print word.encode("utf-8"), score
        
    
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dic = get_dic(sent_file)
    get_sec_dic(tweet_file, sent_dic)
    sent_file.close()
    tweet_file.close()
    

if __name__ == '__main__':
    main()
