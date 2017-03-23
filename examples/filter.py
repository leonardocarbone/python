# Solution 1 - Filter even/odd numbers on the list using lambda expression

list = range(6)
print "Even numbers", filter(lambda n: n%2==0, list)
print "Odd numbers", filter(lambda n: n%2!=0, list)


# Solution 2 - Filter even/odd numbers on the list using classic method

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
