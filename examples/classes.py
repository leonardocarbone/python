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
    
# Example 2 - Inheritence    
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

# Example - Special methods
class Book(object):
  
  # Initializer, constructor
  def __init__(self, title, author, pages):
    print "A book has been created!"
    self.title = title
    self.author = author
    self.pages = pages
    
  
  # Equivalent to toString on java. Used with built-in function 'print'
  def __str__(self):
    return "Title: {0} - Author: {1} - Pages: {2}".format(self.title, self.author, self.pages)
    
  # Used in conjunction with built-in function 'len'
  def __len__(self):
    return self.pages
    
  # Used in conjunction with built-in function 'del'
  def __del__(self):
    print "Book Deleted!"
    
b = Book("Python for Dummies","Someone",1254)
print(b)
print len(b)

del b
b.title # NameError. B is not defined
  
