# Exapmle 1 - Zip, combine two list
l1 = ["a", "b", "c"]
l2 = [10 , 20, 30]

zipped = zip(l1,l2)
print "Zipped tuples =>",zipped

for z in zipped:
  print "{0} => {1}".format(z[0],z[1])
  

# Example 2 - Unzip a list  
x2, y2 = zip(*zipped)
print "Unzipped tubles", x2, y2

# Example 3 - Use zip and list comprehension to return a list of the same length where each value
# is the two strings from L1 and L2 concatenated together with connector between them
def concatenate(list1, list2, connector):
  return [x+connector+y for x,y in zip(list1, list2)]
  
print concatenate(["A","B"],["a","b"], "=>")  
