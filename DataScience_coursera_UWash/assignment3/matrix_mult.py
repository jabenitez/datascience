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
    if record[0] == "a":
        for i in range(5):
            key = record[1],i
            value = record[3]
            mr.emit_intermediate(key,(record[2],value))
    if record[0] == "b":
        for i in range(5):
            key = i,record[2]
            value = record[3]
            mr.emit_intermediate(key,(record[1],value))


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#    print key
#    print list_of_values
    sum = 0
    for i in range(len(list_of_values)):
        for j in range(i+1,len(list_of_values)):
            if list_of_values[i][0] == list_of_values[j][0]:
                sum = sum + list_of_values[i][1]*list_of_values[j][1]
    myemit = (key[0],key[1],sum)
    mr.emit(myemit)
#    total = 0
#    for v in list_of_values:
#      total += v
#    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
