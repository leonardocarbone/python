# Example 1 - Filter even/odd numbers on the list using lambda expression

list = range(6)
print "Even numbers", filter(lambda n: n%2==0, list)
print "Odd numbers", filter(lambda n: n%2!=0, list)


# Example 2 - Filter even/odd numbers on the list using classic method

def check_even(number):
  if number%2 == 0:
    return True
  else:
    return False
    
def check_odd(number):
  if number%2 != 0:
    return True
  else:
    return False    
    
list = range(22)
print "Even numbers", filter(check_even, list)
print "Odd numbers", filter(check_odd, list)


# Example 3 - Use filter to return the words form a list of words which start with a target letter
def filter_words(word_list, letter):
  return filter(lambda x: x[0] == letter, word_list)

list = ["hello", "are", "cat", "dog", "ham", "hi", "go", "to", "heart"]
print filter_words(list, "h")  
