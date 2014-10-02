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
    table = record[0]
    order_id = record[1]

#    if table == "line_item" :
#    value = record
#    if table == "order" :
#      processorder
#    words = value.split()
#    for w in words:
    key = order_id
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    allitems = []
    for v in list_of_values:
      if v[0] == "order":
        myorder = v
      if v[0] == "line_item":
        allitems.append(v)

    for item in allitems:
      mr.emit((myorder + item))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
