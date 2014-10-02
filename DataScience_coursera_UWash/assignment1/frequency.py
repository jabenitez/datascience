import sys
import urllib
import json


def updatecounter(counter,mydict):
    try:
        if not mydict['text'] :
             raise
        for word in mydict['text'].split():
            word = word.encode('utf-8').lower()
            if word in counter.keys():
                counter[word] += 1
            else:
                counter[word] = 1
            
    except:
        pass

def calculatefrequency(counter):
    total=0
    for key in counter.keys():
        total += counter[key]
    print "total" , total
    for key in counter.keys():
        print key,"" , float(float(counter[key])/float(total))

    
def main():
    tweet_file = open(sys.argv[1])

    counter={}
    for line in tweet_file :
        pyresponse = json.loads(line)
        updatecounter(counter,pyresponse)

    calculatefrequency(counter)
#    print counter
if __name__ == '__main__':
    main()
