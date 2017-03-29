# Example - Using @ (at) symbol

def apply_decorator(func):
  
  def wrap_func():
    print "Inside wrap_func"
    func()
    print "Exiting wrap_func"
    
  
  return wrap_func
  
@apply_decorator
def some_func():
  print "I'm a function"
  
some_func()  
