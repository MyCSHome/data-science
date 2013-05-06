import sys
import json


def get_dic(tweet_file):
    dic = {}
    count = 0.0
    for t in tweet_file:
        tweet = json.loads(t)
        if "text" in tweet:
            t_words = tweet["text"].split()
            for word in t_words:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
                count += 1
    return count, dic

def print_fre(count, dic):
    for word in dic:
        print word.encode("utf-8"), dic[word]/count

def main():
    tweet_file = open(sys.argv[1])
    count, dic = get_dic(tweet_file)
    print_fre(count, dic)
    tweet_file.close()

if __name__ == '__main__':
    main()