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

# Example 3 - Use map to create a function which finds the length of each word in the phrase
def word_lengths(phrase):
  return map(lambda x: len(x), phrase.split(" "))
  
print word_lengths("How long are the words in this phrase")
