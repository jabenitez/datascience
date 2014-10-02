import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=10")
pyresponse = json.load(response)

print type(pyresponse)

print pyresponse.keys()

print pyresponse["results"]

results = pyresponse["results"]

print "***********"
print type(results[0])
print results[0]

print "***********"
for i in range(10) :
    print results[i]["text"]
