# Example 1
def apply_decorator(func):
  
  def wrap_func():
    print "Inside wrap_func"
    func()
    print "Exiting wrap_func"
    
  
  return wrap_func
  

def some_func():
  print "I'm a function"
  
some_func = apply_decorator(some_func)
some_func()
