# Example 1
list = range(2,7)
print list

for index, value in enumerate(list):
  print "Index {0}, Value {1}".format(index, value)

  
# Example 2 - Use enumerate to return a dictionary which has the values of list as keys and the index
# as the value.
def to_dict(list):
  return {key:value for value, key in enumerate(list)}

print to_dict(["a" ,"b", "c"])  
