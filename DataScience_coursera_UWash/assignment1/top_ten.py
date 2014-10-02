import sys
import urllib
import json


def main():
    tweet_file = open(sys.argv[1])
    
    hashtags={}
    for line in tweet_file :
        pyresponse = json.loads(line)
        if "entities" in pyresponse.keys():
            if "hashtags" in pyresponse["entities"].keys():
                htlen = len(pyresponse["entities"]["hashtags"])
#                if htlen > 0:
 #                   print pyresponse["entities"]["hashtags"]
                for i in range(0,htlen):
#.encode('utf-8').lower()
                    ht = pyresponse["entities"]["hashtags"][i]["text"]

                    if ht in hashtags.keys():
                        hashtags[ht] += 1
                    else:
                        hashtags[ht] = 1
    i=0
    for w in sorted(hashtags, key=hashtags.get, reverse=True):
        print w, float(hashtags[w])
        i += 1
        if i == 10:
            return



if __name__ == '__main__':
    main()
