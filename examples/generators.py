# Example 1
def gen(value):
  
  for x in range(value):
    print "I have",
    yield x
    print 'car '
    
for y in gen(10):
  if y == 5:
    break
  else:
    print y,

  
# Example 2  
def example():
  for x in range(5):
    yield x
    
ex = example()
print next(ex)
print next(ex)
print next(ex)
    
# Example 3 - Generator that generates the squares of numbers up to some number N
def gensquares(n):
  for x in range(n):
    yield x**2
    
for x in gensquares(10):
  print x
