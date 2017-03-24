# Example - Use reduce to find  max and min values from a list
# Note. You can use built-in functions max e min to find these values
min_value = lambda v1,v2: v1 if (v1<v2) else v2
max_value = lambda v1,v2: v1 if (v1>v2) else v2

list = [1,3,4,3,6,2,10]
print reduce(min_value, list)
print reduce(max_value, list)

# Example 2 - Use reduce to take a list of digits and return the number that they correspond to
def digits_to_num(digits):
  return reduce(lambda x,y:x*10 +y, digits )

print digits_to_num([1,2,3])  
