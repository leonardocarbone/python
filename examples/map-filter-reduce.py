# Example 1 - Use map to convert a list of string numbers in a list of integers
a = ["1","2","3"]
print a
a = map(int, a)
print a

# Example 2 - Use map to apply some function to a value
def hello(name):
  print "Hello", name
  
names = ["Leo","Jon","Arthur"]
map(hello, names)

# Example 3 - Use map to combine two lists
def say_my_name(name, surname):
  print "Say my name -> {0} {1}".format(name,surname)
  
surnames = ["Carbone","Hurht","Max"]
map(lambda x,y: say_my_name(x,y), names, surnames)

# Example 4 - Use reduce to find  max and min values from a list
# Note. You can use built-in functions max e min to find these values
min_value = lambda v1,v2: v1 if (v1<v2) else v2
max_value = lambda v1,v2: v1 if (v1>v2) else v2

list = [1,3,4,3,6,2,10]
print reduce(min_value, list)
print reduce(max_value, list)
