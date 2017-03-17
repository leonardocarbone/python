# Example 1 - Super Simple Class
class Animal(object):
  def __init__(self):
    print "Animal Created!"
    
  def whoAmI(self):
    print "I'm a Animal"
    
  def eat(self):
    print "Eating..."
  
a = Animal()
a.eat()    
    
# Example 2 - Inheritance    

class Dog(Animal):
  
  def __init__(self):
    Animal.__init__(self)
    print "Dog created!"

  def whoAmI(self):
    print "I'm a dog!"
    
  def bark(self):
    print "woof!"

d = Dog()
d.whoAmI()
d.eat()
d.bark()
