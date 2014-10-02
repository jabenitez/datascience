import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
#    print record
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

myfriends={}
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#    testme = set(list_of_values)
#    print testme
#    total = 0
#    for v in list_of_values:
#      total += v
#    print
#    myfriends[key]=list_of_values
#    print "friends"
#    print "key"
#    print key
#    print "values"
#    print list_of_values
#    print "friends"
#    print myfriends
#    print "friends"
#    print
    for v in list_of_values:
        if list_of_values.count(v) == 1 :
            mr.emit((key, v))
#    for v in list_of_values:
#        try:
#            tocheck = myfriends[v]
#            if key not in tocheck:
#                print "key"
#                print key 
#                print "is not"
#                print tocheck
#                print "MISSING", key, v
#                toemit=str(key), str(v)
#                mr.emit(toemit)
#        except:
#            continue
#        print "tocheck"
#        print "tocheck"
#        print tocheck
#        print


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
