import sys
import urllib
import json

states = {'ALASKA': 'AK', 'ALABAMA': 'AL', 'ARKANSAS': 'AR', 'AMERICAN SAMOA': 'AS', 'ARIZONA': 'AZ', 'CALIFORNIA': 'CA', 'COLORADO': 'CO', 'CONNECTICUT': 'CT', 'DISTRICT OF COLUMBIA': 'DC', 'DELAWARE': 'DE', 'FLORIDA': 'FL', 'GEORGIA': 'GA', 'GUAM': 'GU', 'HAWAII': 'HI', 'IOWA': 'IA', 'IDAHO': 'ID', 'ILLINOIS': 'IL', 'INDIANA': 'IN', 'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 'MASSACHUSETTS': 'MA', 'MARYLAND': 'MD', 'MAINE': 'ME', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 'MISSOURI': 'MO', 'NORTHERN MARIANA ISLANDS': 'MP', 'MISSISSIPPI': 'MS', 'MONTANA': 'MT', 'NATIONAL': 'NA', 'NORTH CAROLINA': 'NC', 'NORTH DAKOTA': 'ND', 'NEBRASKA': 'NE', 'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEVADA': 'NV', 'NEW YORK': 'NY', 'OHIO': 'OH', 'OKLAHOMA': 'OK', 'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 'PUERTO RICO': 'PR', 'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC', 'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 'UTAH': 'UT', 'VIRGINIA': 'VA', 'VIRGIN ISLANDS': 'VI', 'VERMONT': 'VT', 'WASHINGTON': 'WA', 'WISCONSIN': 'WI', 'WEST VIRGINIA': 'WV', 'WYOMING': 'WY', 'AK': 'AK', 'AL': 'AL', 'AR': 'AR', 'AS': 'AS', 'AZ': 'AZ', 'CA': 'CA', 'CO': 'CO', 'CT': 'CT', 'DC': 'DC', 'DE': 'DE', 'FL': 'FL', 'GA': 'GA', 'GU': 'GU', 'HI': 'HI', 'IA': 'IA', 'ID': 'ID', 'IL': 'IL', 'IN': 'IN', 'KS': 'KS', 'KY': 'KY', 'LA': 'LA', 'MA': 'MA', 'MD': 'MD', 'ME': 'ME', 'MI': 'MI', 'MN': 'MN', 'MO': 'MO', 'MP': 'MP', 'MS': 'MS', 'MT': 'MT', 'NA': 'NA', 'NC': 'NC', 'ND': 'ND', 'NE': 'NE', 'NH': 'NH', 'NJ': 'NJ', 'NM': 'NM', 'NV': 'NV', 'NY': 'NY', 'OH': 'OH', 'OK': 'OK', 'OR': 'OR', 'PA': 'PA', 'PR': 'PR', 'RI': 'RI', 'SC': 'SC', 'SD': 'SD', 'TN': 'TN', 'TX': 'TX', 'UT': 'UT', 'VA': 'VA', 'VI': 'VI', 'VT': 'VT', 'WA': 'WA', 'WI': 'WI', 'WV': 'WV', 'WY': 'WY'}

def calculate_sentiment(mylist,mydict):
    sum=0
    try:
        if mydict['lang'] != 'en':
             return 0
        if not mydict['text'] :
             return 0
        return calculatescore(mylist,mydict['text'])
    except:
        return 0

def find_state(mydict):
    try:
        place = mydict["place"]
        user = mydict["user"]
        if place["country_code"] == 'US':
            statefound = place["full_name"].split(", ")[1].encode('utf-8').upper()
            if statefound in states.keys():
                return states[statefound]
            else:
                return "none"
        else:
            userloc=user["location"].split(", ")[1].encode('utf-8').upper()
            if userloc in states.keys():
                return states[statefound]
            else:
                return "none"
            raise
        print user["location"]
    except:
        return "none"

    return "none"    

def findhappy(mydict):
    max_happy=0
    max_state="NY"
    for state in mydict.keys():
        if mydict[state] > max_happy:
            max_happy = mydict[state]
            max_state = state

    print max_state


def calculatescore(mylist,text):
    sum=0
    for word in text.split():
        word = word.encode('utf-8').lower()
        if word in mylist.keys():
            sum = sum + mylist[word]
    return sum

def lines(fp):
    print str(len(fp.readlines()))
    fp.seek(0)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores={}
    for line in sent_file.readlines():
        term, score = line.split("\t")
        scores[term] = int(score)
    
    statessent={}
    for line in tweet_file :
        #        print line
        pyresponse = json.loads(line)
        sentiment = calculate_sentiment(scores,pyresponse)
        state = find_state(pyresponse)
        if state != "none": 
            if state in statessent.keys():
                statessent[state] += sentiment
            else:
                statessent[state] = sentiment
    findhappy(statessent)
if __name__ == '__main__':
    main()
